#encoding:utf8
#初始时用来创建所有的表的脚本
from database import database
#创建表user
database.query("""create table if not exists user 
	(uname varchar(15) not null, 
	email varchar(40) not null, 
	rname varchar(24) not null,
	pwd varchar(32) not null, 
	permission enum('0', '1', '2', '3', '4') not null, 
	primary key(uname))""")

database.query("""create table if not exists session (
	sessionid char(27), 
	sessionkey char(20), 
	uname varchar(15), 
	lastactive timestamp, 
	primary key(sessionid),
	foreign key(uname) references user(uname)
	)""")

database.query("""create table if not exists physical(
		id int(10) auto_increment,
		type_id int(10),
		value float,
		collect_time timestamp,
		primary key(id)
	)""")

database.close()