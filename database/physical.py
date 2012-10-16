#encoding:utf8
#物理环境采集获得的物理量
#type_id int(10) 物理量的种类id,唯一确定一个物理数据的类型
#value float 物理量的数值
#collect_time timestamp 采集的时间

"""create table if not exists physical(
		id int(10) auto_increament,
		type_id int(10),
		value float,
		collect_time timestamp,
		primary key(id)
	)"""
from database import database

#存储数据
def insert(type_id, value):
	sql = 'insert into physical(type_id, value) values(%d, %s)' % (type_id, value)
	return database.query(sql)

#获得一个物理量的数值
#type_id 物理量的id
#成功获得则返回其值，否则None
def get_last_one(type_id):
	sql = 'select  value from physical where type_id = %d order by collect_time desc limit 1' % type_id
	cur = database.execute(sql)
	if not cur:
		return None
	res = cur.fetchone()
	database.clear_execute(cur)
	if res:
		return res[0]
	return None

#获得某个物理量的所有数据的id
#返回一个代表其数据的列表，或者None
def get_all_id(type_id):
	sql = 'select id from physical where type_id = %d' % type_id
	cur = database.execute(sql)
	if not cur:
		return None
	res = cur.fetchall()
	database.clear_execute(cur)
	if res:
		res = list(res)
		for i in range(len(res)):
			res[i] = res[i][0]
		return res
	return None

#获得一组数据，从序号begin(包括),数量是num
#type_id 物理量的标志
#begin 开始序号(序号从零开始)
#num 最多取得的数量
#desc 是否按最新程度排序
#返回这些数据的列表,或者None
def get_values(type_id, begin, num, desc = True):
	if desc:
		order = 'desc'
	else:
		order = ''
	sql = 'select value from physical where type_id = %d order by collect_time %s limit %d, %d' % (type_id, order, begin, num)
	cur = database.execute(sql)
	if not cur:
		return None
	res = cur.fetchall()
	database.clear_execute(cur)
	if res:
		res = list(res)
		for i in range(len(res)):
			res[i] = res[i][0]
		return res
	return None

#获得某天一天的数据
#返回时间和数据元组的列表
def get_someday_values(type_id, day):
	min = day + ' 00:00:00'
	max = day + ' 23:59:59'
	sql = 'select collect_time, value from physical where collect_time >= "%s" and collect_time <= "%s" and type_id = %d' % (min, max, type_id)
	cur = database.execute(sql)
	res = cur.fetchall()
	database.clear_execute(cur)
	if res:
		res = list(res)
		for i in range(len(res)):
			tm = '%s' % res[i][0]
			value = res[i][1]
			res[i] = (tm, value)
		return res
	return None


