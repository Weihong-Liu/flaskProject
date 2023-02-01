import os
import time

from flask import Blueprint, render_template, request, send_from_directory

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


@file.route('/download', methods=['GET', 'POST'])
def download():
    """
        文件下载
    :return:
    """
    timelist = []  # 获取指定文件夹下文件并显示
    Foder_Name = []  # 文件夹下所有文件
    Files_Name = []  # 文件名
    file_dir = UPLOAD_FOLDER

    # 获取到指定文件夹下所有文件
    lists = os.listdir(file_dir + '/')

    # 遍历文件夹下所有文件
    for i in lists:
        # os.path.getatime => 获取对指定路径的最后访问时间
        timelist.append(time.ctime(os.path.getatime(file_dir + '/' + i)))

    # 遍历文件夹下的所有文件
    for k in range(len(lists)):
        # 单显示文件名
        Files_Name.append(lists[k])
        # 获取文件名以及时间信息
        Foder_Name.append(lists[k] + " ~~~~~~~~~~~~~~~~~~~~~ " + timelist[k])

    print(file_dir)  # ./upload

    return render_template('download.html', allname=Foder_Name, name=Files_Name)


@file.route('/downloads/<path:path>', methods=['GET', 'POST'])
def downloads(path):
    """
        重写download方法，根据前端点击的文件传送过来的path，下载文件

		send_from_directory：用于下载文件
		flask.send_from_directory(所有文件的存储目录，相对于要下载的目录的文件名，as_attachment：设置为True是否要发送带有标题的文件)
    :param path:
    :return:
    """
    return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)

