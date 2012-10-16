#encoding:utf8
from digital_footoo.util import generate_json

#数字浮屠的错误种类
#没有错误
ERROR_NO = 0
#请求名未知
ERROR_UNKNOWN_REQ_NAME = 1
#参数过少
ERROR_PARAM_LESS = 2
#请求参数不合法
ERROR_PARAM_ILLEGAL = 3
#内部错误
ERROR_INTERNAL = 4
#还未登录
ERROR_NOT_LOGIN = 5
#处理失败
ERROR_DEAL_FAIL = 6
#请求方式不合法
ERROR_ILLEGAL_REQ_METHOD = 7
#带有信息的错误，错误情况详见对应的信息
ERROR_WITH_INFO = 8
#没有权限
ERROR_NO_AUTH = 9


#请求号和其对应的解释
ERROR_INFO = ({
	ERROR_NO 					: 	'没有错误',
	ERROR_UNKNOWN_REQ_NAME 		: 	'请求名未知' , 
	ERROR_PARAM_LESS       		: 	'请求参数过少',
	ERROR_PARAM_ILLEGAL    		: 	'请求参数不合法',
	ERROR_INTERNAL         		: 	'内部错误',
	ERROR_NOT_LOGIN				: 	'还未登录',
	ERROR_DEAL_FAIL				: 	'处理失败',
	ERROR_ILLEGAL_REQ_METHOD	:	'请求方式不合法',
	ERROR_WITH_INFO				:	'带有信息的错误',
	ERROR_NO_AUTH				:	'没有足够的权限',
	})

#
def raise_no_error():
	return generate_json.error_json(ERROR_NO)

#
def raise_unknown_req_name():
	return generate_json.error_json(ERROR_UNKNOWN_REQ_NAME)

#
def raise_param_less():
	return generate_json.error_json(ERROR_PARAM_LESS)

#
def raise_param_illegal():
	return generate_json.error_json(ERROR_PARAM_ILLEGAL)

#
def raise_internal():
	return generate_json.error_json(ERROR_INTERNAL)

#
def raise_not_login():
	return generate_json.error_json(ERROR_NOT_LOGIN)

#
def raise_deal_fail():
	return generate_json.error_json(ERROR_DEAL_FAIL)

#
def raise_illegal_req_method():
	return generate_json.error_json(ERROR_ILLEGAL_REQ_METHOD)

#
def raise_error_with_info(info):
	return generate_json.error_with_info_json(ERROR_WITH_INFO, info)

#
def raise_no_auth():
	return generate_json.error_json(ERROR_NO_AUTH)

