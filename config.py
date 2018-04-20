"""
    为了让配置方式更灵活且更安全，某些配置可以从环境变量中导入。例如， SECRET_KEY 的值，
    这是个敏感信息，可以在环境中设定，但系统也提供了一个默认值，以防环境中没有定义。
"""
import os
import base64

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
        配置类可以定义 init_app() 类方法，其参数是程序实例。在这个方法中，可以执行对当前
        环境的配置初始化。现在，基类 Config 中的 init_app() 方法为空。
    """
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # 很难猜字符串
    MAIL_SERVER = 'smtp.sina.cn'
    MAIL_PORT = '25'
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    # 数据交换
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USERNAME = 'gtian0122@sina.cn'
    MAIL_PASSWORD = 'gou01tian22'
    # 邮件主题前缀 [幸福的饺子]
    FLASKY_MAIL_SUBJECT_PREFIX = '[幸福的饺子（Happiness the dumplings）]'
    # 邮件地址
    FLASKY_MAIL_SENDER = '幸福的饺子 <gtian0122@sina.cn>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    # 邮件服务器
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        app.debug = True


# 开发配置
class DevelopmentConfig(Config):
    """
        在 3 个子类中， SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。这样程序就可在不同
        的配置环境中运行，每个环境都使用不同的数据库。
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


"""
    config 字典中注册了不同的配置环境，而且还注册了一个默认配置
"""
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}