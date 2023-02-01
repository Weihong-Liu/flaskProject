from models import db, UserInfo, Announcement, GameExchangeCode, DownloadRecord
from app import app
a = Announcement(announcement="这是最新公告！")
app.app_context().push()
db.session.add(a)
db.session.commit()
# app.app_context().push()
# a = Announcement.query.get(1) #Announcement.query.order_by(Announcement.update_time.desc()).first()
# # for i in announcement:
# print(a.announcement,a.update_time)



# 生成订单号接口
@order.route('/get_order', methods=['GET'])
def get_order():
    return jsonify(msg="success", order_id=client.get_guid())  # 雪花算法

from snowflake import client