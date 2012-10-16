#encoding:utf8
#用户注册

from digital_footoo.database import user
from digital_footoo.util import generate_json, security
from digital_footoo import error

INFO_UNAME = '用户名已存在'
INFO_EMAIL = '邮箱已被注册'
INFO_OK = '注册成功'

def register(uname, email, rname, pwd):
	#检测参数是否合法
	if(not security.is_uname_valid(uname)
		or not security.is_email_valid(email)
		or not security.is_rname_valid(rname)
		or not security.is_pwd_valid(pwd)):
		return error.raise_param_illegal()
	#用户名已被注册
	if not user.uname_registerable(uname):
		return error.raise_error_with_info(INFO_UNAME)
	#邮箱已被注册
	if not user.email_registerable(email):
		return error.raise_error_with_info(INFO_EMAIL)
	#插入数据库
	if user.insert(uname, email, rname, pwd):
		return generate_json.data_json(INFO_OK)
	return error.raise_internal()
