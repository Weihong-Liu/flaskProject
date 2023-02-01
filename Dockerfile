FROM python:3.9

WORKDIR ~/flaskProject/
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
