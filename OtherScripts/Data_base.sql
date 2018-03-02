USE master
GO
CREATE DATABASE PryhodaOleksandr25

ON PRIMARY
(NAME=PryhodaOleksandr25, FILENAME='C:\DB\PryhodaOleksandr25.mdf', SIZE=50MB, MAXSIZE=UNLIMITED, FILEGROWTH=10MB)

LOG ON
(NAME=PryhodaOleksandr25_log, FILENAME='C:\DB\PryhodaOleksandr25.ldf', SIZE=50MB, MAXSIZE=UNLIMITED, FILEGROWTH=10MB)
GO


USE PryhodaOleksandr25
GO


CREATE TABLE Doctor
(IDDoctor int IDENTITY PRIMARY KEY,
Name nvarchar(30) NOT NULL,
Surname nvarchar(30) NOT NULL,
Fathername nvarchar(30) NOT NULL,
PhoneNumber nchar(10) NULL,
OfficeNumber int NULL CHECK(OfficeNumber>=0),
Speciality nvarchar(25) NULL)


CREATE TABLE Reference
(IDReference int IDENTITY PRIMARY KEY,
IDDoctor int NULL,
Diagnose nvarchar(100) NULL,
TreatmentAppointment nvarchar(100) NULL,
ResultAppointment nvarchar(100) NULL,
FOREIGN KEY (IDDoctor) REFERENCES Doctor(IDDoctor))

CREATE TABLE Visit
(IDVisit int IDENTITY PRIMARY KEY,
Appeal nvarchar(100) NULL,
VisitDate date NULL,
IDReference int NULL,
FOREIGN KEY (IDReference) REFERENCES Reference(IDReference))

CREATE TABLE Habitant
(IDHabitant int IDENTITY PRIMARY KEY,
Name nvarchar(30) NOT NULL,
Surname nvarchar(30) NOT NULL,
Fathername nvarchar(30) NOT NULL,
Photo nvarchar(300) NULL,
BloodType int NULL, 
BirthDate date NULL CHECK(BirthDate>=CONVERT(date, GETDATE())),
Adress nvarchar(50) NULL,
IDDoctor int NULL,
IDVisit int NULL,
DiseaseInfo nvarchar(300) NULL,
FOREIGN KEY (IDDoctor) REFERENCES Doctor(IDDoctor),
FOREIGN KEY (IDVisit) REFERENCES Visit(IDVisit))

CREATE TABLE DisabilityLetter
(IDDisabilityLetter int IDENTITY PRIMARY KEY,
IDDoctor int NULL,
OpenDate date NULL,
CloseDate date NULL,
Diagnose  nvarchar(100) NULL,
FOREIGN KEY (IDDoctor) REFERENCES Doctor(IDDoctor))



INSERT INTO Doctor( Name, Surname, Fathername, PhoneNumber, OfficeNumber, Speciality)
Values('John', 'Grew', 'Petrowych', '0676723459', 1, 'proctolog'), 
      ('Erik', 'Maus', 'Ivanowych', '0676768765', 2, 'theethdoctor'),
	  ('Mark', 'Varguver', 'Rostyslawowych', '0930009990', 3, 'doctor')


INSERT INTO Reference(IDDoctor, Diagnose, TreatmentAppointment, ResultAppointment)
VALUES (1, 'cancer', 'medicines', 'good'), 
       (2, 'fieber', 'spazmalhon', 'correct'),
	   (3, 'stomach ache', 'sorbex', 'bad')


INSERT INTO Visit(Appeal, VisitDate, IDReference)
VALUES ('stomach', '2017-05-03', 1 ), 
       ('head', '2017-06-07', 2), 
       ('leg', '2016-12-03', 3)


INSERT INTO Habitant(Name, Surname, Fathername, Photo, BloodType, BirthDate, Adress, IDDoctor, IDVisit, DiseaseInfo)
VALUES ('Petro', 'Petrenko', 'Petrovych', '12345', 1, '2017-05-03', 'Lviv', 1, 2, 'Very strong disease'), 
       ('Nazar', 'Nazarenko', 'Nazarovych', '12345', 1, '2017-06-07', 'Odesa', 2, 3, 'will not live'), 
       ('Oleg', 'Olegenko', 'Olegovych', '12345', 4, '2017-12-03', 'Charkiv', 3, 1, 'better')


INSERT INTO DisabilityLetter(IDDoctor, OpenDate, CloseDate, Diagnose)
VALUES (1, '2017-05-03', '2017-05-05', 'cancer'), 
       (3, '2017-06-07', '2017-05-09', 'hard to decide'), 
       (2, '2016-12-03', '2017-05-07', 'dead')