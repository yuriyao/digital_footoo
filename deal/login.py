#encoding:utf8
#处理用户登录

from digital_footoo.database import user
from digital_footoo.util import generate, generate_json
from digital_footoo import error
import json

#生成响应的json数据
def generate_login_json(session_id, session_key):
	data = {'session_id' : session_id, 'session_key' : session_key}
	return generate_json.data_json(data)

#返回一个用户登录cookie的字典
#{'session_id' : session_id, 'session_key' : session_key}
def parse_login_json(data):
	info = json.loads(data)
	d = info['data']
	return d

#uname 用户名
#pwd 密码
#返回一个符合json的数据格式的数据
def login(uname, pwd):
	if user.is_valid_user(uname, pwd):
		session_key = generate.generate_sessionKey()
		session_id = generate.generate_sessionId()
		return generate_login_json(session_id, session_key)
	else:
		return error.raise_deal_fail()
