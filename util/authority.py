#encoding:utf-8
#用户权限管理

from digital_footoo.confi import PHYSICAL_INFO

#定义用户权限等级,等级值越大，权限越高
#0:普通用户, 1:临时权限1, 2:实验室成员, 3:临时权限3, 4:管理员
NORMAL_USER = 0
TEMP_USER1 = 1
LAB_MEMBER = 2
TEMP_USER3 = 3
ADMIN = 4

#检测用户是否拥有权限
#min 所需要的最低权限
#authority 用户的权限值
def has_authority(min, authority):
	return (authority >= min)

#检测用户是否有权限获得物理量数据
def can_access_physical(type_id, uname):
	from digital_footoo.database import user 
	perm = user.get_permission(uname)
	if perm == None:
		return False
	if type_id >= len(PHYSICAL_INFO):
		return False
	min = PHYSICAL_INFO[type_id]['min']
	return has_authority(min, perm)

#检测是否是合法的权限值
def is_valid(authority):
	return (authority >= NORMAL_USER or authority <= ADMIN)