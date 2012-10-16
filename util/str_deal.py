#encoding:utf8
#处理字符串
import re

DAY_PATTERN = re.compile(r'^\d{4,4}\-(\d{2,2})\-(\d{2,2})$')

#判断一个字符串是否是一个代表一个日期值
def is_day_str(string):
	c = re.match(DAY_PATTERN, string)
	if c:
		month = c.groups()[0]
		month = int(month)
		day = c.groups()[1]
		day = int(day)
		if(month > 0 and month < 13 and day > 0 and day < 32): 
			return True
	return False

