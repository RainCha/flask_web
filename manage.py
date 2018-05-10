# coding=utf-8

# 通过manage.py 运行命令十分必要，因为一些 flask 扩展只有在flask应用对象被创建后才会被初始化，
# 直接运行默认的python命令行会返回错误

from flask_script import Manager, Server
from main import app


manager = Manager(app)

manager.add_command('server', Server())

@manager.shell
def make_shell_context():
  return dict(app=app)


if __name__ == '__main__':
  manager.run()


# 运行 python manage.py server
# shell 运行 python manage.py shell