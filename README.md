# Profiles REST API

Profiles REST API course code.


# Vagrant
```shell
vagrant init ubuntu/bionic64
vagrant up # 拉起虚拟机
vagrant ssh # 进入虚拟机
cd /vagrant # 进入host和虚拟机的共享目录
```

# create python virtual environment
```shell
python -m venv ~/env # 没有把虚拟环境放在本地同步目录下, 而是放在家目录下
source ~/env/bin/activate # 启动虚拟环境
deactivate # 直接退出虚拟环境
```

# django admin
```shell
# 创建项目目录和 manage.py 文件
django-admin.py startproject profileproject .
# 创建一个应用
python manage.py startapp profiles_api

# 运行 django server
python manage.py runserver 0.0.0.0:8000

```

django settings
```python
'rest_framework', # djongo restful 的框架
'rest_framework.authtoken', # django restful 的token验证功能
'profiles_api', # 自己构建的api应用
```
