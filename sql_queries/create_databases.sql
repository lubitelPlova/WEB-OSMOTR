-- Создание таблицы Job
CREATE TABLE Job (
    JobID INT PRIMARY KEY,
    JobName VARCHAR(100) UNIQUE NOT NULL,
    JobType VARCHAR(50),
    WorkHours INT CHECK (WorkHours >= 0)
);

-- Создание таблицы Patient
CREATE TABLE Patient (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    MedicalInfo TEXT,
    JobID INT,
    ClientOrganizationID INT,
    FOREIGN KEY (JobID) REFERENCES Job(JobID)
);

-- Создание таблицы Location
CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100) NOT NULL,
    LocationCity VARCHAR(100) NOT NULL
);

-- Создание таблицы Terminal
CREATE TABLE Terminal (
    TerminalID INT PRIMARY KEY,
    LocationID INT,
    Status VARCHAR(50),
    ServiceInfo TEXT,
    ClinicID INT,
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

-- Создание таблицы Clinic
CREATE TABLE Clinic (
    ClinicID INT PRIMARY KEY,
    ClinicName VARCHAR(100) NOT NULL
);

-- Создание таблицы ClinicAdmin
CREATE TABLE ClinicAdmin (
    AdminID INT PRIMARY KEY,
    ClinicID INT,
    AdminName VARCHAR(255) NOT NULL,
    AdminInfo TEXT,
    FOREIGN KEY (ClinicID) REFERENCES Clinic(ClinicID)
);

-- Создание таблицы Doctor
CREATE TABLE Doctor (
    DoctorID INT PRIMARY KEY,
    DoctorInfo TEXT,
    Name VARCHAR(255) NOT NULL,
    ClinicID INT,
    FOREIGN KEY (ClinicID) REFERENCES Clinic(ClinicID)
);

-- Создание таблицы MedicalExamination
CREATE TABLE MedicalExamination (
    ExaminationID INT PRIMARY KEY,
    PatientID INT,
    DoctorID INT,
    TerminalID INT,
    Result TEXT,
    DateTime DATETIME NOT NULL,
    Duration INT CHECK (Duration > 0),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
    FOREIGN KEY (TerminalID) REFERENCES Terminal(TerminalID)
);

-- Создание таблицы Image
CREATE TABLE Image (
    ImageID INT PRIMARY KEY,
    ExaminationID INT,
    DateTime DATETIME NOT NULL,
    ImageData BLOB,
    FOREIGN KEY (ExaminationID) REFERENCES MedicalExamination(ExaminationID)
);

-- Создание таблицы DeviceMeasurements
CREATE TABLE DeviceMeasurements (
    MeasurementID INT PRIMARY KEY,
    DateTime DATETIME NOT NULL,
    ExaminationID INT,
    DeviceType VARCHAR(100),
    Data TEXT,
    FOREIGN KEY (ExaminationID) REFERENCES MedicalExamination(ExaminationID)
);