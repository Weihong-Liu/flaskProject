from flask import Blueprint, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired

from extension import db
from models import GameExchangeCode
from tools.ExchangeCode import ExchangeCode

code = Blueprint("code", __name__, url_prefix="/code")

# 生成兑换码的表单
class GenerateCodeForm(FlaskForm):
    code_num = IntegerField(label='生成兑换码个数: ', validators=[DataRequired()])
    gold_coin = IntegerField(label='金币数量: ', validators=[DataRequired()])
    diamond = IntegerField(label='钻石数量: ', validators=[DataRequired()])
    submit = SubmitField(label='提交')

# 兑换奖励的表单
class ExchangeCodeForm(FlaskForm):
    code = StringField(label='兑换码: ', validators=[DataRequired()])
    submit = SubmitField(label='兑换奖励')

@code.route("/")
def to_code():
    generate_code_form = GenerateCodeForm()
    exchange_code = ExchangeCodeForm()
    return render_template('code.html', generate_code_form=generate_code_form, exchange_code=exchange_code)

@code.route("/generate", methods=['POST'])
def generate_code():
    code_num = int(request.form.get('code_num'))
    gold_coin = int(request.form.get('gold_coin'))
    diamond = int(request.form.get('diamond'))
    exchange_code = ExchangeCode()
    success_num = 0
    code_ls = []
    for x in range(0, code_num):
        code = exchange_code.get_code()
        game_code = GameExchangeCode(code=code, GoldCoin=gold_coin, Diamond=diamond)
        try:
            db.session.add(game_code)
            db.session.commit()
            success_num += 1
            code_ls.append(code)
        except Exception as e:
            print(e)
            db.rollback()
    return jsonify(msg=f"成功生成兑换码{success_num}个", code=code_ls)

@code.route("/exchange", methods=['POST'])
def exchange_code():
    exchange_code = request.form.get('code')
    game_code = GameExchangeCode.query.filter(GameExchangeCode.code==exchange_code).first()
    if game_code is None:
        return "无效的兑换码，请重新输入！"
    else:
        if game_code.is_use == "是":
            return "该兑换码已兑换，请勿重复兑换！"
        else:
            game_code.is_use = "是"
    try:
        db.session.add(game_code)
        db.session.commit()
        return f"恭喜获得金币{game_code.GoldCoin}个，钻石{game_code.Diamond}个"
    except Exception as e:
        print(e)
        db.rollback()
        return "发生错误，请重新兑换！"

