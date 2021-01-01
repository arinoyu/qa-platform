FROM python:3.6
WORKDIR /root/Q&Aplatform

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn","--certfile=./4620052_www.arino.top.pem","--keyfile=./4620052_www.arino.top.key", "app:app", "-c", "./gunicorn.conf.py"]