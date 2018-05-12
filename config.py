# coding=utf-8

class Config(object):
  SECRET_KEY = "792BDA9S7DH312O80DYASH9812"
  pass

class ProdConfig(object):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'
  pass

class DevConfig(object):
  Debug=True

  # sqlite
  SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'
  # mysql 
  # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user.password@ip:port/db_name'
 
  # 可以看到 SQLALCHEMY 打印出来的 sql 语句
  # SQLALCHEMY_ECHO = True``