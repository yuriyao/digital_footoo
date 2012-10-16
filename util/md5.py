#encoding:utf-8
#封装md5的c处理函数
#注意这个函数不是线程安全的

import MD5

def md5(data = ''):
	return MD5.md5(data)