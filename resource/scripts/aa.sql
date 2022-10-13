select * from zyetable1;
select * from zyetable2;
use zye;
create database xiao;
use xiao;
create table user(
User_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Username varchar(100),
Email varchar(100),
Phone varchar(20),
Pad varchar(50)
);
insert into user(Username,Email,Phone,Pad) values('艾希礼','2573100722@qq.com','15707079305','19980320xzs');
insert into user(Username,Email,Phone,Pad) values('周宏森','1107547237@qq.com','15070274986','15070274986');
select * from user;
# 随机抽取20条记录
SELECT keynote,title,egname
FROM zyetable2 AS t1 
JOIN(SELECT ROUND(RAND() * ((SELECT MAX(id) FROM zyetable2)-(SELECT MIN(id) FROM zyetable2))+(SELECT MIN(id) FROM zyetable2))AS id) AS t2 
WHERE t1.id >= t2.id 
ORDER BY t1.id LIMIT 20;

SELECT keynote,title,egname 
FROM zyetable2 
WHERE id>=
(SELECT floor(RAND() * ((SELECT MAX(id) FROM zyetable2)-(SELECT MIN(id) FROM zyetable2)) + (SELECT MIN(id) FROM zyetable2))) 
ORDER BY id LIMIT 20;

use xiao;
# 答题测试记录表：英文选词
create table model1_record(
record_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Username varchar(100),
grade varchar(10),
time_point timestamp default CURRENT_TIMESTAMP
);

select * from  model1_record;

# 答题测试记录表：中文选词
create table model2_record(
record_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Username varchar(100),
grade varchar(10),
time_point timestamp default CURRENT_TIMESTAMP
);
select * from  model2_record;
