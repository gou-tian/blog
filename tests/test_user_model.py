import unittest
from app.models import User, AnonymousUser, Role, Permission
from app import create_app, db


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='123')
        self.assertTrue(u.password_hash is not None)

    def test_on_password_getter(self):
        u = User(password='123')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='123')
        self.assertTrue(u.verify_password('123'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='123')
        u2 = User(password='123')
        self.assertTrue(u.password_hash != u2.password_hash)

    # 角色和权限的单元测试
    def test_roles_and_permissions(self):
        # Role.insert_roles()
        u = User(email='gtian0122@sina.cn', password='123')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))