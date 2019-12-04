# [ImportError: pycurl: libcurl link-time ssl backend (openssl) is different from compile-time ssl back](pip uninstall pycurl export PYCURL_SSL_LIBRARY=openssl)

## 这个问题是可以用重新安装解决
``` bash
pip uninstall pycurl
export PYCURL_SSL_LIBRARY=openssl
pip install pycurl
```

## 但是这里有一个坑：在高版本的mac系统环境变量里是找不到openssl的头文件的
``` bash
pip uninstall pycurl# 卸载库
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include # openssl相关头文件路径
pip install pycurl --compile --no-cache-dir # 重新编译安装
```