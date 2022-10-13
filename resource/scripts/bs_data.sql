use  bsdb;

# 成分表
create table compound_table(
herb_name varchar(50),#药物名称
compound_id varchar(20),#成分id
compound_chinese_name varchar(200),#成分中文名称
compound_english_name varchar(200),#成分英文名称
compound_smiles varchar(200),#成分化学式
compound_sources varchar(200),#成分来源
compound_oil varchar(50)#成分所属精油
);
insert into compound_table values('','','','','','','');
delete from compound_table where herb_name='' and compound_id='' and compound_chinese_name='' 
and compound_english_name='' and compound_smiles='' and compound_sources='' and compound_oil='';
# 靶点表
create table target_table(
herb_name varchar(50),#药物名称
compound_english_name varchar(200),#英文名称（compound）
compound_chinese_name varchar(200),#中文名称（Source.Name）
target_name varchar(500), #靶点名称
target_common_name varchar(50) #靶点简称
);
delete from target_table where herb_name='' and compound_english_name='' and compound_chinese_name='' and target_name='' and target_common_name='';
# 信号通路表
create table signalentry_table(
herb_name varchar(50),#药物名称
disease_english_name varchar(50),#疾病英文名称
disease_chinese_name varchar(50),#疾病中文名称
intersection_target_name varchar(500),#重合靶点名称
intersection_target_common_name varchar(50),#重合靶点简称
entry_common_name varchar(50),#信号通路简称
entry_name varchar(500)#信号通路名称
);
delete from signalentry_table where herb_name='' and disease_english_name='' and disease_chinese_name='' and intersection_target_name='' and intersection_target_common_name='' and entry_common_name='' and entry_name='';

create table herb_table(
herb_id varchar(50) NOT NULL PRIMARY KEY,
herb_name varchar(50)
);
insert into herb_table values('001','安息香');

select compound_table.herb_name,compound_table.compound_id,compound_table.compound_chinese_name,compound_table.compound_english_name,compound_table.compound_smiles,compound_table.compound_sources,compound_table.compound_oil,target_table.target_name,target_table.target_common_name,signalentry_table.disease_english_name,signalentry_table.disease_chinese_name,signalentry_table.intersection_target_name,signalentry_table.intersection_target_common_name,signalentry_table.entry_common_name,signalentry_table.entry_name
from compound_table inner join target_table on compound_table.herb_name=target_table.herb_name
inner join signalentry_table on compound_table.herb_name=signalentry_table.herb_name
where signalentry_table.herb_name='安息香';

select big_table.*,signalentry_table.disease_english_name,signalentry_table.disease_chinese_name,signalentry_table.intersection_target_name,signalentry_table.intersection_target_common_name,signalentry_table.entry_common_name,signalentry_table.entry_name from(
select compound_table.herb_name,compound_table.compound_id,compound_table.compound_chinese_name,compound_table.compound_english_name,compound_table.compound_smiles,compound_table.compound_sources,compound_table.compound_oil,target_table.target_name,target_table.target_common_name from compound_table join target_table on compound_table.herb_name=target_table.herb_name)
as big_table join signalentry_table on big_table.herb_name=signalentry_table.herb_name;

select distinct compound_table.herb_name,compound_table.compound_id,compound_table.compound_chinese_name,compound_table.compound_english_name,compound_table.compound_smiles,compound_table.compound_sources,compound_table.compound_oil,target_table.target_name,target_table.target_common_name
from compound_table join target_table on compound_table.herb_name=target_table.herb_name
LIMIT 1000000000;

select * from herb_table;
select * from compound_table;
select * from target_table;
select * from signalentry_table;
select * from big_table;
SET SQL_SAFE_UPDATES = 1;



