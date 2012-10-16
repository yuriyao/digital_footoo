#encoding:utf8
#获得最新的物理量
#这些物理量一般是原始的数据,没有进行处理

from digital_footoo import error
from digital_footoo.database import physical
from digital_footoo.util import authority, generate_json, str_deal
import time as libtime, datetime

#获得一个物理量的最新的一个数据
#uname 用户名，由系统自动传入,不计为用户请求参数
#type_id 物理量序号，是字符串，是用户请求参数
def get_last_one(uname, type_id):
	if not type_id.isdigit():
		return error.raise_param_illegal()
	type_id = int(type_id)
	#检查权限
	if not authority.can_access_physical(type_id, uname):
		return error.raise_no_auth()
	value = physical.get_last_one(type_id)
	if value == None:
		return error.raise_error_with_info('没有对应物理量的数据')
	return generate_json.data_json(value)

#生成最近一天的物理量数据的json
#datas: 包含时间和数据双元祖的列表
#data域：[{'time' : 时间, 'value' : 数据}, ...]p
def generate_today_json(datas):
	data = []
	for time, value in datas:
		d = {'time' : time, 'value' : value}
		data.append(d)
	return generate_json.data_json(data)

#获得某一天的物理信息数据
def get_someday_values(uname, day, type_id):
	if not str_deal.is_day_str(day) or not type_id.isdigit():
		return error.raise_param_illegal()
	type_id = int(type_id)
	#检查权限
	if not authority.can_access_physical(type_id, uname):
		return error.raise_no_auth()
	datas = physical.get_someday_values(type_id, day)
	if datas:
		return generate_today_json(datas)
	return error.raise_error_with_info('没有对应的数据')

#获得今天一天的信息
def get_today_values(uname, type_id):
	#参数合法性检查
	if not type_id.isdigit():
		return error.raise_param_illegal()
	type_id = int(type_id)
	#检查权限
	if not authority.can_access_physical(type_id, uname):
		return error.raise_no_auth()
	today = libtime.strftime('%Y-%m-%d')
	datas = physical.get_someday_values(type_id, today)
	if datas:
		return generate_today_json(datas)
	return error.raise_error_with_info('没有对应的数据')

#获得前一天的一天的数据
def get_yesterday_values(uname, type_id):
	yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
	yesterday = yesterday.strftime('%Y-%m-%d')
	return get_someday_values(uname, yesterday, type_id)


