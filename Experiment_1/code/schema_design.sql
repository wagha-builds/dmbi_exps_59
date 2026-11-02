-- ====================================================================
-- Experiment 1: Star Schema and Snowflake Schema Implementation
-- Student Name: Atharva Waghmode | Roll No: 59 | Div: D15A
-- GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_1
-- ====================================================================

-- 1. STAR SCHEMA 1: Student Result Analysis System
DROP TABLE IF EXISTS Result_Fact;
DROP TABLE IF EXISTS Student_Dimension;
DROP TABLE IF EXISTS Subject_Dimension;
DROP TABLE IF EXISTS Exam_Dimension;
DROP TABLE IF EXISTS Date_Dimension;

CREATE TABLE Date_Dimension (
    Date_ID INT PRIMARY KEY,
    Date DATE NOT NULL,
    Month VARCHAR(20),
    Quarter VARCHAR(5),
    Year INT
);

CREATE TABLE Student_Dimension (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(100),
    Class VARCHAR(20),
    Section VARCHAR(5)
);

CREATE TABLE Subject_Dimension (
    Subject_ID INT PRIMARY KEY,
    Subject_Name VARCHAR(100),
    Subject_Type VARCHAR(20)
);

CREATE TABLE Exam_Dimension (
    Exam_ID INT PRIMARY KEY,
    Exam_Name VARCHAR(50),
    Exam_Type VARCHAR(20),
    Semester VARCHAR(20)
);

CREATE TABLE Result_Fact (
    Result_ID INT PRIMARY KEY,
    Student_ID INT,
    Subject_ID INT,
    Exam_ID INT,
    Date_ID INT,
    Marks_Obtained NUMERIC(5, 2),
    Max_Marks INT,
    FOREIGN KEY (Student_ID) REFERENCES Student_Dimension(Student_ID),
    FOREIGN KEY (Subject_ID) REFERENCES Subject_Dimension(Subject_ID),
    FOREIGN KEY (Exam_ID) REFERENCES Exam_Dimension(Exam_ID),
    FOREIGN KEY (Date_ID) REFERENCES Date_Dimension(Date_ID)
);

-- 2. STAR SCHEMA 2: Library Book Issue System
DROP TABLE IF EXISTS Issue_Fact;
DROP TABLE IF EXISTS Book_Dimension;
DROP TABLE IF EXISTS Staff_Dimension;

CREATE TABLE Book_Dimension (
    Book_ID INT PRIMARY KEY,
    Book_Title VARCHAR(150),
    Author VARCHAR(100),
    Category VARCHAR(50)
);

CREATE TABLE Staff_Dimension (
    Staff_ID INT PRIMARY KEY,
    Staff_Name VARCHAR(100),
    Designation VARCHAR(50)
);

CREATE TABLE Issue_Fact (
    Issue_ID INT PRIMARY KEY,
    Book_ID INT,
    Student_ID INT,
    Staff_ID INT,
    Date_ID INT,
    Days_Issued INT,
    Fine_Amount NUMERIC(6, 2),
    FOREIGN KEY (Book_ID) REFERENCES Book_Dimension(Book_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student_Dimension(Student_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff_Dimension(Staff_ID),
    FOREIGN KEY (Date_ID) REFERENCES Date_Dimension(Date_ID)
);

-- 3. SNOWFLAKE SCHEMA: Student Result Analysis System (Normalized)
DROP TABLE IF EXISTS Department_SubDimension;
DROP TABLE IF EXISTS Course_SubDimension;
DROP TABLE IF EXISTS Student_Dimension_Snowflake;
DROP TABLE IF EXISTS Subject_Dimension_Snowflake;

CREATE TABLE Department_SubDimension (
    Dept_ID INT PRIMARY KEY,
    Dept_Name VARCHAR(100),
    HOD_Name VARCHAR(100)
);

CREATE TABLE Student_Dimension_Snowflake (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(100),
    Dept_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES Department_SubDimension(Dept_ID)
);

CREATE TABLE Course_SubDimension (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(100),
    Duration VARCHAR(20)
);

CREATE TABLE Subject_Dimension_Snowflake (
    Subject_ID INT PRIMARY KEY,
    Subject_Name VARCHAR(100),
    Course_ID INT,
    FOREIGN KEY (Course_ID) REFERENCES Course_SubDimension(Course_ID)
);

-- Analytical Sample OLAP Query on Star Schema
SELECT 
    d.Year,
    d.Quarter,
    sub.Subject_Name,
    AVG(rf.Marks_Obtained) AS Average_Marks,
    MAX(rf.Marks_Obtained) AS Highest_Marks
FROM Result_Fact rf
JOIN Date_Dimension d ON rf.Date_ID = d.Date_ID
JOIN Subject_Dimension sub ON rf.Subject_ID = sub.Subject_ID
GROUP BY d.Year, d.Quarter, sub.Subject_Name;
