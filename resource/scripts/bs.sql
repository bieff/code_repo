show variables like '%datadir%';
select current_user();
create database bsdb;
use bsdb;
create table login_log(
login_account varchar(50),
login_time varchar(200),
login_ip varchar(200),
login_system varchar(200),
login_hostname varchar(200)
);
select COLUMN_NAME from INFORMATION_SCHEMA.Columns where table_name='login_log';

create table work_log(
work_account varchar(200),
work_time varchar(200),
work_success varchar(10),
work_text varchar(2000)
);
create table feedback_log(
feedback_account varchar(200),
feedback_name varchar(50),
feedback_time varchar(200),
feedback_type varchar(10),
feedback_text varchar(1000),
feedback_phone varchar(200)
);
create table user_ifo(
user_account varchar(200) NOT NULL PRIMARY KEY,
user_name varchar(50),
user_password varchar(50),
user_email varchar(100),
user_introduction varchar(1000),
user_sex varchar(10),
user_headimageurl varchar(1000),
user_experience int,
user_grade int
);
insert into user_ifo values('201601033017','夜晓希声','123456','2573100722@qq.com','只争朝夕，不负韶华','男','./resource/icos/201601033017.ico',6666,6);
update user_ifo set user_headimageurl='./resource/icos/201601033017.ico' where user_account='201601033017';
insert into user_ifo values('123','123','123','123','123','女','./resource/icos/default.ico',0,0);
update user_ifo set user_experience=6668 where user_account='201601033017';
insert into work_log values('201601033017','123456','是','不知道');
select * from user_ifo;
select * from feedback_log;
select * from login_log;
select * from work_log;
delete from work_log;
update user_ifo set user_experience=2 where user_account='201601033034';
SET SQL_SAFE_UPDATES = 1;