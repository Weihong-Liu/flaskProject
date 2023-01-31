from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://LWH:123456@120.76.202.170:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 公告数据库
class Announcement(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    announcement = db.Column(db.String(99), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now)
    # def __str__(self):
    #     return self.announcement


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)


class DownloadRecord(db.Model):
    __tablename__ = 'download_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    is_download = db.Column(db.Enum("是", "否"), nullable=False)
    file_md5 = db.Column(db.String(99), nullable=False)


class GameExchangeCode(db.Model):
    __tablename__ = 'game_exchange_code'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(99), nullable=False)  # 兑换码
    GoldCoin = db.Column(db.Integer, nullable=False)  # 金币
    Giamond = db.Column(db.Integer, nullable=False)  # 钻石
    is_use = db.Column(db.Enum("是", "否"), nullable=False)


if __name__ == '__main__':
    # db.drop_all()
    app.app_context().push()
    db.create_all()
