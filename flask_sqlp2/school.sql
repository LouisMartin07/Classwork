DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Age     INT,
    Class VARCHAR(100)
);
DROP TABLE IF EXISTS Teachers;
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Age     INT,
    Class VARCHAR(100)
);
DROP TABLE IF EXISTS Subjects;
CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY,
    SubjectName VARCHAR(100),
);