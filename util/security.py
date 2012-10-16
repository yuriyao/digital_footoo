#encoding:utf-8
import re

#用户名的模式
NAME_PATTEN = re.compile(r'^[\w\-]{1,15}$') 
#email的模式
EMAIL_PATTEN = re.compile(r'^[\w\-]+@[\w\-]+\.[\w\-]+$')
#email的最大长度
EMAIL_MAX = 40
#真实姓名的最大长度
RNAME_MAX = 24
#密码的最大长度
PASSWD_MAX = 56

#检测用户名是否合法
def is_uname_valid(uname):
	if re.match(NAME_PATTEN, uname):
		return True
	return False

#检测是否是合法的email地址
def is_email_valid(email):
	if len(email) > EMAIL_MAX:
		return False
	if re.match(EMAIL_PATTEN, email):
		return True
	return False

#检测是否是合法的真实姓名
def is_rname_valid(rname):
	if len(rname) > RNAME_MAX or '\'' in rname:
		return False
	return True

#检测是否是合法的密码
def is_pwd_valid(pwd):
	if len(pwd) > PASSWD_MAX:
		return False
	return True