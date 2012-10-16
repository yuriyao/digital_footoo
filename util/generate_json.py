#encoding:utf8
#生成json数据

import json
#错误的json数据
def error_json(errno):
	str = {"error" : errno} 
	return json.dumps(str)

#带有错误信息的json数据
def error_with_info_json(errno, info):
	str = {'error' : errno, 'info' : info}
	return json.dumps(str)

#生成返回正常数据的json
def data_json(data):
	str = {"error" : 0, "data" : data}
	return json.dumps(str)
