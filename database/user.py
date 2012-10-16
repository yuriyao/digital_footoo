#encoding:utf-8
#用户信息的数据库管理
#uname 用户名 varchar(15) 主键
#email email varchar(40)
#rname 真实姓名 varchar(24)
#pwd 用户密码 varchar(32) 通过md5加密
#permission 用户权限 0:普通用户, 1:临时权限1, 2:实验室成员, 3:临时权限3, 4:管理员

"""create table user (uname varchar(15) not null, email varchar(40) not null, rname varchar(24) not null,
	pwd varchar(32) not null, permission enum('0', '1', '2', '3', '4') not null, primary key(uname))"""

from digital_footoo.util import authority
from database import database
from digital_footoo.util import md5


#插入用户注册信息
def insert(uname, email, rname, pwd, permission = 0):
	#对密码进行md5的加密
	pwd = md5.md5(pwd)
	sql = "insert into user values('%s', '%s', '%s', '%s', '%d')" % (uname, email, rname, pwd, permission)
	return database.query(sql)

#检测用户是否是合法用户
def is_valid_user(uname, pwd):
	pwd = md5.md5(pwd)
	sql = 'select * from user where uname = "%s" and pwd = "%s"' % (uname, pwd)
	return database.is_exist(sql)

#改变用户的权限值
#uname 用户名
#permission 欲改变成的权限
#如果权限值合理，则返回True,否则返回False
def change_permission(uname, permission):
	if not authority.is_valid(permission):
		return False 
	sql = "update user set permission = '%d' where uname = '%s'" % (permission, uname)
	return database.query(sql)

#获得一个用户的权限值
#uname 用户名
#如果用户存在，则返回其权限值，否则返回None
def get_permission(uname):
	sql = "select permission from user where uname = '%s'" % uname
	cur = database.execute(sql)
	res =  cur.fetchone()
	database.clear_execute(cur)
	if res:
		return res[0]
	return None

#获得用户的e-mail地址
#如果用户存在，返回其邮箱地址，否则返回None
def get_email(uname):
	sql = "select email from user where uname = '%s'" % uname
	cur = database.execute(sql)
	res =  cur.fetchone()
	database.clear_execute(cur)
	if res:
		return res[0]
	return None

#获得用户的真实姓名
def get_rname(uname):
	sql = "select rname from user where uname = '%s'" % uname
	cur = database.execute(sql)
	res =  cur.fetchone()
	database.clear_execute(cur)
	if res:
		return res[0]
	return None

#获得用户的所有信息（除了密码）
#返回用户信息的字典,次序为用户email，用户真实姓名，用户权限值
def get_all_info(uname):
	sql = "select email, rname, permission from user where uname = '%s'" % uname
	cur = database.execute(sql)
	info = cur.fetchone()
	#规范化返回值
	if info:
		info = list(info)
		info[2] = int(info[2], 10)
		res = {'email' : info[0], 'rname' : info[1], 'permission' : info[2]}
		return res
	return None

#确定对应的用户名是否可以注册
def uname_registerable(uname):
	sql = 'select * from user where uname = "%s"' % uname
	cur = database.execute(sql)
	data = cur.fetchone()
	database.clear_execute(cur)
	if data:
		return False
	return True

#确定对应的邮箱是否可以注册
def email_registerable(email):
	sql = 'select * from user where email = "%s"' % email
	cur = database.execute(sql)
	data = cur.fetchone()
	database.clear_execute(cur)
	if data:
		return False
	return True