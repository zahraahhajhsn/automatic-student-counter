create database senior 
use senior 
go 

create table cameraInfo (
id int PRIMARY KEY IDENTITY(0,1),
roomNumber varchar(20),
department varchar(255),
ip varchar(20)
);

create table headsInfo(
name varchar(255),
email varchar(255) UNIQUE,
pass varchar(255),
department varchar(255) PRIMARY KEY
);

create table room(
roomNumber varchar(5),
department varchar(50)
);

insert into room values('D2','Physical Biochemistry')
insert into room values('12','Physical Biochemistry')
insert into room values('13','Physical Biochemistry')
insert into room values('404','Physical Biochemistry')
insert into room values('401','Physical Biochemistry')



insert into headsInfo values('houda kanaan','nurkanaan@outlook.com','1234','Applied Mathematics')
insert into cameraInfo values(45,'Applied Mathematics')
