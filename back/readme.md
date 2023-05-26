
## 部署

注意，可能有些库国内下载速度比较慢

### 部署后端代码

github仓库

https://github.com/nyml2003/db

clone下来

安装python和必要的库，以下是你可能要下载的库
```python
pip install Flask
pip install uwsgi
pip install flask_sqlalchemy
pip install gevent
pip install flask-cors
pip install pymysql
pip install pyinstaller
```

先运行init.py，再运行file_server.py