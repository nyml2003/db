### 部署前端代码

github仓库

https://github.com/nyml2003/db

clone下来

你需要保证自己安装了node.js和npm,

#### 初始化（下载node_modules）
```
npm install
```

#### 编译+热更新
```
npm run serve
```

如果要在localhost上通信，请把

```
/src/components/services/DataService.js
```
修改代码
```javascript
const apiClient = axios.create({
  // 设置后端 API 的基础 URL
  baseURL: "http://host:port/api",
  // 设置请求头
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});
```
中的baseURL
```
baseURL: "http://localhost:port/api"
```

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