#encoding:utf8
#处理用户会话的数据库部分
#会话数据库由四项组成:
#sessionid 会话id char(27)
#sessionkey 会话key char(20)
#uname 用户的name varchar(15)
#lastactive 最后一次活跃的时间 time
"""create table if not exist session (
	sessionid char(27), 
	sessionkey char(20), 
	uname varchar(15), 
	lastactive timestamp, 
	primary key(sessionid),
	foreign key(uname) references user(uname)
	)"""

from database import database
from digital_footoo.util import generate

from time import strftime, strptime
from datetime import datetime

SESSION_KEY = 'sessionKey'
SESSION_ID = 'sessionID'
#cookie的生存时间(不活动的时间)12小时
COOKIE_LIFE = 43200

def insert(sessionid, sessionkey, uname):
	"""将会话信息保存到数据库"""
	time = strftime('%Y-%m-%d %H:%M:%S')
	database.query("insert into session (sessionid, sessionkey, uname, lastactive)"
	 "values('%s', '%s', '%s', '%s')" % (sessionid, sessionkey, uname, time))

#通过用户的sessionid和sessionkey获得用户的用户名
#如果存在，则返回用户名，否则返回None
def get_uname(sessionid, sessionkey):
	sql = 'select uname from session where sessionid = "%s" and sessionkey = "%s"' % (sessionid, sessionkey)
	cur = database.execute(sql)
	res = cur.fetchone()
	#关闭游标
	database.clear_execute(cur)
	if res:
		return  res[0]
	return None
