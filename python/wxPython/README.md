# [pyenv 中 wxpython 程序无法启动](http://blog.scicooking.net/2017/cannot-startup-wxpython-in-pyenv.html)

## 解决方法：
使用 –enable-framework 选项重新安装 python
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -f 3.6.1