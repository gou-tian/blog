from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm
from ..email import send_email


# 登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('无效的用户名或密码。')
    return render_template('default/auth/login.html', form=form)


# 注销
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('成功注销。')
    return redirect(url_for('main.index'))


# 新用户注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '确认你的账户', 'default/auth/email/confirm', user=user, token=token)
        flash('一封确认邮件已通过电子邮件发送给你。')
        return redirect(url_for('main.index'))
    return render_template('default/auth/register.html', form=form)


# 确认用户账户
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('你的帐号已经确认。谢谢!')
    else:
        flash('确认链接无效或已过期.')
    return redirect(url_for('main.index'))


# 过滤未确认账户
@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.'\
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


# 重发却邮件
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '确认你的账户', 'default/auth/email/confirm', user=current_user.email, token=token)
    flash('一封确认邮件已通过电子邮件发送给你。')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('default/auth/unconfirmed.html')


