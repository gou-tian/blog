from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('default/index.html',
                           form=form, name=session.get('name'),
                           konwn=session.get('known', False),
                           current_time=datetime.utcnow())