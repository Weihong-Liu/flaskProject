import os
from flask import Blueprint, render_template, request
from config import UPLOAD_FOLDER

file = Blueprint("file", __name__, url_prefix="/file")

@file.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # 渲染文件
    return render_template('upload.html')

@file.route('/uploader', methods=['GET', 'POST'])
def uploader():
    """
        文件上传
    """
    if request.method == 'POST':
        # input标签中的name的属性值
        f = request.files['file']

        # 拼接地址，上传地址，f.filename：直接获取文件名
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        # 输出上传的文件名
        print(request.files, f.filename)

        return '文件上传成功!'
    else:
        return render_template('upload.html')