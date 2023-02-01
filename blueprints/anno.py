from flask import Blueprint, jsonify, request
from models import Announcement
from extension import db

anno = Blueprint("anno", __name__, url_prefix="/anno")

# 获取公告接口
@anno.route("/get_announcement")
def get_announcement():
    res = Announcement.query.order_by(Announcement.update_time.desc()).first()
    return jsonify(msg="success", content=res.announcement)

# 编辑公告接口
@anno.route("/update_announcement", methods=["POST"])
def update_announcement():
    js = request.get_json()
    content = js.get("content")
    if content is None:
        return jsonify(msg="缺少参数")
    else:
        res = Announcement.query.order_by(Announcement.update_time.desc()).first()
        res.announcement = content
        try:
            db.session.add(res)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(msg="数据库出现错误")
        return jsonify(msg="公告更新成功！")