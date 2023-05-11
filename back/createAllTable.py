from dataBase import DataBase

db=DataBase()
sql = """

create table Patient(
 Pno int primary key COMMENT '患者编号',
 Pname varchar(20) not null COMMENT '患者姓名',
 Pid varchar(20) not null COMMENT '身份证号',
 Pino varchar(20) not null COMMENT '社会保险号',
 Pmno varchar(20) not null COMMENT '医疗卡识别号',
 Psex varchar(20) not null COMMENT '性别',
 Pbd date not null COMMENT '出生日期',
 Padd varchar(100) not null COMMENT '地址'
) COMMENT '患者';

INSERT INTO Patient VALUES(161,'刘景','142201198702130061','1201676','6781121941','男','1987-2-13','新华路光源街');
INSERT INTO Patient VALUES(181,'陈禄','142201196608190213','1204001','5461021938','男','1966-8-19','城建路茂源路');
INSERT INTO Patient VALUES(201,'曾华','142201197803110234','0800920','1231111932','男','1978-3-11','新建路柳巷');
INSERT INTO Patient VALUES(421,'傅伟相','142202199109230221','0700235','4901021947','男','1991-9-23','高新区西源大道');
INSERT INTO Patient VALUES(481,'张珍','142201199206200321','1200432','3451121953','女','1992-6-20','西湖区南街');
INSERT INTO Patient VALUES(501,'李秀','142203198803300432','0692015','3341111936','女','1988-3-30','泰山大道北路');

create table Patient_tel(
 Ptno int primary key AUTO_INCREMENT COMMENT '患者联系电话编号',
 Pno int not null COMMENT '患者编号',
 FOREIGN KEY(Pno) REFERENCES Patient(Pno),
 Pteltype varchar(20) not null COMMENT '联系方式类型',
 Ptel varchar(20) not null COMMENT '联系号码'
) COMMENT '患者联系电话';

INSERT INTO Patient_tel(Pno, Pteltype, Ptel) VALUES(161,'手机','12988011007');
INSERT INTO Patient_tel(Pno, Pteltype, Ptel) VALUES(161,'家庭电话','01166699988');
INSERT INTO Patient_tel(Pno, Pteltype, Ptel) VALUES(161,'单位电话','01244552277');

create table Salary(
 Sno int not null primary key,
 Slevel varchar(20) not null,
 Snumber DECIMAL(12,4) not null
);

INSERT INTO Salary VALUES(03,'高级',4000);
INSERT INTO Salary VALUES(05,'中级',3000);
INSERT INTO Salary VALUES(01,'高级',5000);
INSERT INTO Salary VALUES(06,'初级',2500);
INSERT INTO Salary VALUES(04,'高级',4500);

create table Title(
 Tno int primary key not null,
 Sno int not null,
 FOREIGN KEY(Sno) REFERENCES Salary(Sno),
 Ttype varchar(20) not null,
 Ttrade varchar(20) not null
);

INSERT INTO Title VALUES(102,05,'医师','医疗');
INSERT INTO Title VALUES(104,03,'副主任医师','医疗');
INSERT INTO Title VALUES(103,04,'主治医师','医疗');
INSERT INTO Title VALUES(105,01,'主任医师','医疗');
INSERT INTO Title VALUES(233,06,'初级护师','护理');
INSERT INTO Title VALUES(235,03,'主任护师','护理');

CREATE TABLE Doctor (
    Dno INT PRIMARY KEY,
    Dname VARCHAR(20) NOT NULL,
    Dsex VARCHAR(20) NOT NULL,
    Dage INT NOT NULL,
    Ddeptno INT NOT NULL,
    Tno INT NOT NULL
);

INSERT INTO Doctor VALUES (140, '郝亦柯', '男', 28, 101, 01);
INSERT INTO Doctor VALUES (21, '刘伟', '男', 43, 104, 01);
INSERT INTO Doctor VALUES (368, '罗晓', '女', 27, 103, 04);
INSERT INTO Doctor VALUES (73, '邓英超', '女', 43, 105, 33);
INSERT INTO Doctor VALUES (82, '杨勋', '男', 104, 104, 35);

CREATE TABLE Dept (
    DeptNo INT PRIMARY KEY NOT NULL,
    DeptName VARCHAR(20) NOT NULL,
    ParentDeptNo INT,
    Manager INT
) COMMENT '组织机构';

INSERT INTO Dept VALUES (00, 'XX医院', NULL, NULL);
INSERT INTO Dept VALUES (10, '门诊部', 00, NULL);
INSERT INTO Dept VALUES (101, '消化内科', 10, 82);
INSERT INTO Dept VALUES (102, '急诊内科', 10, 368);
INSERT INTO Dept VALUES (103, '门内三诊室', 10, 21);
INSERT INTO Dept VALUES (20, '社区医疗部', 00, NULL);
INSERT INTO Dept VALUES (201, '家庭病床病区', 20, 73);

ALTER TABLE Doctor ADD FOREIGN KEY (Ddeptno) REFERENCES Dept (DeptNo);
ALTER TABLE Doctor ADD FOREIGN KEY (Tno) REFERENCES Title (Tno);
ALTER TABLE Dept ADD FOREIGN KEY (ParentDeptNo) REFERENCES Dept (DeptNo);
ALTER TABLE Dept ADD FOREIGN KEY (Manager) REFERENCES Doctor (Dno);

create table Godown_Entry(
 GMno int not null primary key,
 GMdate DATETIME not null,
 GMname varchar(20) not null
);

create table Godown_Slave(
 GSno int not null primary key,
 GMno int not null,
 FOREIGN KEY(GMno) REFERENCES Godown_Entry(GMno),
 Mno int not null,
 FOREIGN KEY(Mno) REFERENCES Medicine(Mno),
 GSnumber DECIMAL(12,4) not null,
 GSunit varchar(20) not null,
 GSbatch varchar(20) not null,
 GSprice DECIMAL(12,4) not null,
 GSexpdate date not null
);

create table Medicine(
 Mno int not null primary key,
 GSno int not null,
 FOREIGN KEY(GSno) REFERENCES Godown_Slave(GSno),
 Mname varchar(20) not null,
 Mprice DECIMAL(12,4) not null,
 Munit varchar(20) not null,
 Mtype varchar(20) not null
);
create table Cashier(
 Cno int not null primary key
);
INSERT INTO Cashier VALUES(09);
INSERT INTO Cashier VALUES(01);
INSERT INTO Cashier VALUES(02);
INSERT INTO Cashier VALUES(05);
INSERT INTO Cashier VALUES(08);

create table Diagnosis(
 DGno varchar(20) primary key not null,
 Pno int not null,
 FOREIGN KEY(Pno) REFERENCES Patient(Pno),
 Dno varchar(20) not null,
 FOREIGN KEY(Dno) REFERENCES Doctor(Dno),
 Symptom varchar(20) not null,
 Diagnosis varchar(20) not null,
 DGtime DATETIME not null,
 Rfee DECIMAL(12,4) not null
);

INSERT INTO Diagnosis VALUES(1645,481,140,);
INSERT INTO Diagnosis VALUES();
INSERT INTO Diagnosis VALUES();
INSERT INTO Diagnosis VALUES();
INSERT INTO Diagnosis VALUES();
INSERT INTO Diagnosis VALUES();

create table Recipe_Master(
  RMno int not null primary key,
  DeptNo int not null,
  FOREIGN KEY(DeptNo) REFERENCES Dept(DeptNo),
  Dno int not null,
  FOREIGN KEY(Dno) REFERENCES Doctor(Dno),
  Pno int not null,
  FOREIGN KEY(Pno) REFERENCES Patient(Pno),
  RMage int not null,
  RMtime DATETIME not null
);

INSERT INTO Recipe_Master VALUES(1282317,103,140,181,12,'2016-7-21 01:12:01');
INSERT INTO Recipe_Master VALUES(1282872,201,368,161,50,'2016-7-22 10:10:03');
INSERT INTO Recipe_Master VALUES(1283398,20,73,481,23,'2016-7-23 10:59:42');
INSERT INTO Recipe_Master VALUES(1284041,101,368,501,48,'2017-7-23 11:11:34');
INSERT INTO Recipe_Master VALUES(1284256,103,21,201,36,'2017-7-23 02:01:05');
INSERT INTO Recipe_Master VALUES(1458878,102,82,421,30,'2017-1-8 05:17:03');

create table Recipe_Detail(
 RDno int not null primary key,
 RMno int not null,
 FOREIGN KEY(RMno) REFERENCES Recipe_Master(RMno),
 Mno int not null,
 FOREIGN KEY(Mno) REFERENCES Medicine(Mno),
 RDprice DECIMAL(12,4) not null,
 RDnumber int not null,
 RDunit varchar(20) not null
);

INSERT INTO Recipe_Detail VALUES(16,1282872,314941,200,3,'盒');
INSERT INTO Recipe_Detail VALUES(32,1458878,315189,360,4,'盒');
INSERT INTO Recipe_Detail VALUES(47,1284041,315977,14,1,'片');
INSERT INTO Recipe_Detail VALUES(89,1282317,316910,2.5,10,'粒');

create table Register_Form(
 RFno int not null primary key,
 RFdept int not null,
 FOREIGN KEY(RFdept) REFERENCES Dept(DeptNo),
 RFdoctor int not null,
 FOREIGN KEY(RFdoctor) REFERENCES Doctor(Dno),
 RFpatient int not null,
 FOREIGN KEY(RFpatient) REFERENCES Patient(Pno),
 RFcashier int not null,
 FOREIGN KEY(RFcashier) REFERENCES Cashier(Cno),
 RFtime DATETIME not null,
 RFvisittime DATETIME not null,
 RFfee DECIMAL(12,4) not null,
 RFnotes varchar(20)
);

INSERT INTO Register_Form VALUES(13,20,73,481,01,'2016-7-11 06:12:09','2016-7-11 08:00:00',5,NULL);
INSERT INTO Register_Form VALUES(56,201,368,161,08,'2016-7-28 09:20:19','2016-7-28 09:30:00',7,NULL);
INSERT INTO Register_Form VALUES(71,103,140,181,09,'2017-1-10 16:09:02','2017-1-10 17:30:00',7,NULL);
INSERT INTO Register_Form VALUES(89,102,82,421,02,'2017-3-16 19:18:10','2017-3-16 19:20:00',5,NULL);

create table Fee(
 Fno int not null primary key,
 Fnumber varchar(20) not null,
 Fdate DATETIME not null,
 DGno int not null,
 FOREIGN KEY(DGno) REFERENCES Diagnosis(DGno),
 RMno int not null,
 FOREIGN KEY(RMno) REFERENCES Recipe_Master(RMno),
 Cno int not null,
 FOREIGN KEY(Cno) REFERENCES Cashier(Cno),  
 Pno int not null,
 FOREIGN KEY(Pno) REFERENCES Patient(Pno),
 FRecipefee DECIMAL(12,4) not null,
 Fdiscount DECIMAL(12,4) not null,
 Fsum DECIMAL(12,4) not null
);

INSERT INTO Fee VALUES(1281645,'02995606','2016-7-21 01:12:01',1645,1282317,09,181,200,0,200);
INSERT INTO Fee VALUES(1282170,'02994356','2016-7-22 10:10:03',7816,1282872,01,481,189,37.8,151.2);
INSERT INTO Fee VALUES(1283265,'02996768','2016-7-23 10:59:42',2170,1283998,02,501,560,112,448);
INSERT INTO Fee VALUES(1283308,'02995687','2016-7-23 11:11:34',3308,1284041,05,201,17,3.4,13.6);
INSERT INTO Fee VALUES(1283523,'02997432','2016-7-23 02:01:05',3523,1284256,08,481,13,0,13);
INSERT INTO Fee VALUES(1457816,'02990101','2017-1-8 05:17:03',3265,1458878,09,21,111,0,111);
"""
# FOREIGN KEY() REFERENCES (),
ret=db.execute(sql)
print(ret)