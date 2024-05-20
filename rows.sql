INSERT INTO Customer (CustomerID, [Name], EmailAddress, Phone, [Address], CreditScore)
VALUES
    (1, 'Shiva', 'shiva@email.com', '9876543210', '12 Main Street, Varanasi', 500),
    (2, 'Anika', 'anika@email.com', '9876543211', '34 Gandhi Nagar, Mumbai', 600),
    (3, 'Varun', 'varun@email.com', '9876543212', '56 Market Road, Hyderabad', 700),
    (4, 'Madhu', 'madhu@email.com', '9876543213', '78 Oak Street, Ooty', 800);



INSERT INTO Loan (LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus)
VALUES
    (1, 1, 20000.0, 5.0, 12, 'CarLoan', 'Pending'),
    (2, 2, 30000.0, 6.0, 24, 'HomeLoan', 'Approved'),
    (3, 3, 40000.0, 7.0, 36, 'HomeLoan', 'Pending'),
    (4, 4, 50000.0, 8.0, 48, 'CarLoan', 'Approved');

INSERT INTO CarLoan (LoanID, CarModel, CarValue) VALUES 
    (1, 'Toyota', 20000),
    (4, 'Ford', 50000);


INSERT INTO HomeLoan (LoanID, PropertyAddress, PropertyValue) VALUES 
    (2, 'Mumbai', 30000),
    (3, 'Hyderabad', 40000);


SELECT * FROM [Customer]

SELECT * FROM [Loan]