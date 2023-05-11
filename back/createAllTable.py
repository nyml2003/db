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

create table Diagnosis(
 DGno varchar(20) primary key not null,
 Pno varchar(20) not null,
 FOREIGN KEY(Pno) REFERENCES Patient(Pno),
 Dno varchar(20) not null,
 FOREIGN KEY(Dno) REFERENCES Doctor(Dno),
 Symptom varchar(20) not null,
 Diagnosis varchar(20) not null,
 DGtime DATETIME not null,
 Rfee DECIMAL(12,4) not null
);

"""
ret=db.execute(sql)
print(ret)