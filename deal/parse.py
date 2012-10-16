#encoding:utf-8
#解析用户请求，并负责分发
#用户请求协议:
#请求方法必须是get(Http)
#name:请求名称
#参数列表:param1, param2...
#参数个数必须大于等于必须参数的数量

#返回数据的格式(json)
#{"error" : 错误号, "data" : 返回的数据} 

from digital_footoo.database import session
from digital_footoo import error
from django.http import HttpResponse
import login, register, get_last_physical

#请求的种类
#获取数据
REQUEST_TYPE_GET_DATA = 1
#命令
REQUEST_TYPE_COMMAND_TYPE = 2

#请求名称以及对应的处理信息
#格式:
#'请求名称' : {'method' : 处理函数, 'paramNum': 参数数量, 'must' : 必须的参数数量, 'login' : 是否需要先登录}
NAMES = ({
	'login' : {'method' : login.login, 'paramNum' : 2, 'must' : 2, 'must_login' : False},
	'register' : {'method' : register.register, 'paramNum' : 4, 'must' : 4, 'must_login' : False},
	'last_physical' : {'method' : get_last_physical.get_last_one, 'paramNum' : 1, 'must' : 1, 'must_login' : True},
	})

def parse(request):
	if request.method == 'GET':
		get = request.GET
		#get数据不完整
		if not 'name' in get:
			return HttpResponse(error.raise_unknown_req_name())
		name = get['name']
		if not name in NAMES:
			return HttpResponse(error.raise_unknown_req_name())
		d = NAMES[name]
		#对应的处理函数句柄
		method = d['method']
		#处理函数的参数的数量
		paramNum = d['paramNum']
		#必须的参数数量
		must = d['must']
		#是否需要先登录
		must_login = d['must_login']
		#存储参数
		params = []
		#解析出参数
		for i in range(paramNum):
			param_name = 'param%s' % i
			if param_name in get:
				params.append(get[param_name])
			else:
				if i + 1 < must:
					return HttpResponse(error.raise_param_less())
				break
		params = tuple(params)
		#处理需要首先进行登录的请求
		if must_login:
			if not 'session_id' in request.COOKIES or not 'session_key' in request.COOKIES:
				return HttpResponse(error.raise_not_login())
			session_id = request.COOKIES['session_id']
			session_key = request.COOKIES['session_key']
			uname = session.get_uname(session_id, session_key)
			if not uname:
				return HttpResponse(error.raise_not_login())
			try:
				return HttpResponse(method(uname, *params))
			except Exception as e:
				print e
				return HttpResponse(error.raise_internal())
		#处理不需要首先进行登录的数据
		else:
			try:
				return HttpResponse(method(*params))
			except Exception as e:
				print e
				return HttpResponse(error.raise_internal())

	return HttpResponse(error.raise_illegal_req_method())

	
