#encoding:utf-8
#进行数据库的底层操作的抽象化,实现数据库的长连接,并防止数据库的重复打开

import MySQLdb
import sys
from digital_footoo.confi import db_info
from digital_footoo.util.log import log

reload(sys)
sys.setdefaultencoding('utf-8')

class Database:
	def __init__(self, dbname, user, passwd):
		self.dbname = dbname
		self.user = user
		self.passwd = passwd
		self.con = MySQLdb.connect(db = dbname, user = user, passwd = passwd)
		#self.cursor = self.con.cursor()

	#进行sql查询时，先查询，如果发生异常
	#进行异常类型检测，如果是连接超时，则重连
	def query(self, sql):
		res = True
		try:
			self.con.query(sql)
		except MySQLdb.MySQLError, e:
			try:
				#检查是否超时
				self.con.ping()
			except MySQLdb.InterfaceError:
				#如果是数据库连接超时,重新进行连接
				self.con = MySQLdb.connect(db = self.dbname, user = self.user, passwd = self.passwd)
				self.con.query(sql)
			else:
				res = False
				log.log('database.py/query', '查询语法出错')
				print e
		return res
		#self.con.commit()

	def is_exist(self, sql):
		res = False
		try:
			res = (self.con.cursor().execute(sql) != 0)
		except MySQLdb.MySQLError, e:
			try:
				#检查是否超时
				self.con.ping()
			except MySQLdb.InterfaceError:
				#如果是数据库连接超时,重新进行连接
				self.con = MySQLdb.connect(db = self.dbname, user = self.user, passwd = self.passwd)
				res = (self.con.cursor().execute(sql) != 0)
			else:
				res = False
				log.log('database.py/is_exist', '查询语法出错')
				print e
		finally:
			return res;

	def execute(self, sql):
		cursor = ''
		try:
			cursor = self.con.cursor()
			cursor.execute(sql)
		except MySQLdb.MySQLError, e:
			print e
			self.clear_execute(cursor)
			try:
				#检查是否超时
				self.con.ping()
			except MySQLdb.InterfaceError:
				#如果是数据库连接超时,重新进行连接
				self.con = MySQLdb.connect(db = self.dbname, user = self.user, passwd = self.passwd)
				cursor = self.con.cursor()
				cursor.execute(sql)
			else:
				cursor = ''
				log.log('database.py/execute', '查询语法出错')
		finally:
			return cursor

	def clear_execute(self, cursor):
		if cursor:
			cursor.close()

	def close(self):
		try:
			self.con.close()
		except MySQLError, e:
			print e

database = Database(db_info['db_name'], db_info['u_name'], db_info['pwd'])



