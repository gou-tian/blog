# 学习笔记
### 工程目录结构
```text
├─migrations        数据库迁移脚本
├─static            静态文件
├─templates         页面模版
└─tests             单元测试

app.py              运行主程序
requirements.txt    列出了所有依赖包
config.py           存储配置
manage.py           用于启动程序以及其他的程序任务
```
### 依赖软件包管理
   > 生成命令
   
``` text
    pip freeze >requirements.txt
```
  > 软件包部署
```text
    pip install -r requirements.txt
```
### 程序功能说明
```text
    数据库模型              app/models.py
    电子邮件支持函数         app/email.py
    注册蓝本                app/_init_.py
    错误处理程序            app/main/errors.py
    蓝本定义程序路由         app/main/views.py
```
### 获取环境变量
```python
import os
# environ是在os.py中定义的一个dict environ = {}
# 读取环境变量两种方法
# 1.os.environ 
# 2. os.getenv('MAIL_USERNAME')
env_dist = os.environ 
os.getenv('MAIL_USERNAME')

print(env_dist.get('JAVA_HOME'))
print(env_dist['JAVA_HOME'])

# 打印所有环境变量，遍历字典
for key in env_dist:
    print(key + ' : ' + env_dist[key])
# 设置环境变量
# Linux： export FLASKY_ADMIN=<your-email-address>
# windows set FLASKY_ADMIN=<Gmail username>
```
### 蓝图模版设定
```python
from flask import Blueprint
Blueprint('main', __name__, template_folder='../../templates')
```
       'mian'为蓝图设定目录，template_folder模版文件不得同目录下，要设定模版文件夹路径。
    否则会报错 jinja2.exceptions.TemplateNotFound: （文件名）
### 创建数据表或者升级到最新修订版本
```textmate
python manage.py db upgrade
```