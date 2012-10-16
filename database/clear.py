#encoding:utf-8
#一个定时运行的脚本，用于定期清除session表里的过期的会话
#这个脚本是可以独立于整个项目文件而运行的

import time
from datetime import datetime, timedelta
import MySQLdb

#定时的时间长度(s)
TIME_GAP = 3600
#会话的过期时间(s)
SESSION_LIVE = 43200
#数据库连接信息
db_info = {'u_name' : 'root', 'pwd' : 'iloveparent', 'db_name' : 'digital_footoo'}

while True:
	now = datetime.now()
	print('I am working again at %s' % now.strftime('%Y-%m-%d %H:%M:%S'))
	delta = timedelta(seconds = SESSION_LIVE)
	#会话是否过期的界限
	live = now - delta

	sql = 'delete from session where lastactive <= "%s"' % live.strftime('%Y-%m-%d %H:%M:%S')
	try:
		co = MySQLdb.connect(db = db_info['db_name'], user = db_info['u_name'], passwd = db_info['pwd'])
		co.query(sql)
	except Exception as e:
		print e
	finally:
		try:
			co.close()
		except Exception as e2:
			print e2
	#启动定时
	time.sleep(TIME_GAP)

