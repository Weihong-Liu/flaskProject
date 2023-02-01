from flask import Blueprint, jsonify
from snowflake import client

order = Blueprint("order", __name__, url_prefix="/order")

# 生成订单号接口
@order.route('/get_order', methods=['GET'])
def get_order():
    try:
        return jsonify(msg="success", order_id=client.get_guid())  # 雪花算法，服务器要先执行snowflake_start_server --worker=3
    except Exception as e:
        print(e)
        return jsonify(msg="error")
