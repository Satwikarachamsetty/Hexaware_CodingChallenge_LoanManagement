create database HexawareLoanDB
use HexawareLoanDB

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    [Name] VARCHAR(255),
    EmailAddress VARCHAR(255),
    Phone VARCHAR(20),
    [Address] VARCHAR(255),
    CreditScore INT
);

CREATE TABLE [Loan] (
    LoanID INT PRIMARY KEY,
    CustomerID INT,
    PrincipalAmount FLOAT,
    InterestRate FLOAT,
    LoanTerm INT ,
    LoanType VARCHAR(50) CHECK (LoanType IN ('CarLoan', 'HomeLoan')),
    LoanStatus VARCHAR(50) CHECK (LoanStatus IN ('Pending', 'Approved')),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE HomeLoan (
    LoanID INT PRIMARY KEY,
    PropertyAddress VARCHAR(255),
    PropertyValue FLOAT,
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);

CREATE TABLE CarLoan (
    LoanID INT PRIMARY KEY,
    CarModel VARCHAR(255),
    CarValue FLOAT,
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);