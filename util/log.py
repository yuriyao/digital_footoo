#encoding:utf8
#系统的log系统
#log的格式:
#time 文件 描述
from digital_footoo.confi import LOG_PATH
import time

class Log(object):
	def __init__(self):
		self.log_file = ''
		try:
			self.log_file = open(LOG_PATH, 'w')
		except IOError, e:
			print e

	def log(self, filename = 'udef', des = 'udef'):
		if self.log_file:
			now = time.strftime('%Y-%m-%d-%H:%M:%S')
			self.log_file.write(('%s %s %s\n' % (now, filename, des)))
			self.log_file.flush()
			
	def close(self):
		if self.log_file:
			self.log_file.close()

log = Log()