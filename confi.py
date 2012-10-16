#encoding:utf-8
#配置数据库
#数据库连接信息
db_info = {'u_name' : 'root', 'pwd' : 'iloveparent', 'db_name' : 'digital_footoo'}
#LOG文件路径
LOG_PATH = 'digital_footoo.log'
#物理量信息配置信息
#name 物理量英文名称
#doc 物理量中文名称
#id 物理量的标号,用于实际区分物理量的类型,其值必须和其在列表里的序号相同
#min 获得这个物理量的最小权限
PHYSICAL_INFO = ([
	{'name' : 'light', 'doc' : '亮度', 'id' : 0, 'min' : 0},
	{'name' : 'humidity', 'doc' : '湿度', 'id' : 1, 'min' : 0},
	{'name' : 'temperature', 'doc' : '温度', 'id': 2, 'min' : 0},
	{'name' : 'gas', 'doc' : '气体情况', 'id' : 3, 'min' : 0},
	])
