from util.DBconn import DBConnection
from myexception.InvalidLoanException import InvalidLoanException
from abc import ABC, abstractmethod

class ILoanRepository(ABC):
    @abstractmethod
    def applyLoan(self, loan):
        pass

    @abstractmethod
    def calculateInterest(self, loan_id):
        pass

    @abstractmethod
    def loanStatus(self, loan_id):
        pass

    @abstractmethod
    def calculateEMI(self, loan_id):
        pass

    @abstractmethod
    def loanRepayment(self, loan_id, amount):
        pass

    @abstractmethod
    def getAllLoans(self):
        pass

    @abstractmethod
    def getLoanbyId(self, loan_id):
        pass


   
class ILoanService(ILoanRepository, DBConnection):

    def applyLoan(self,loan):
        query = """INSERT INTO Loan (LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus) VALUES (?,?,?,?,?,?,?)"""
        values =(loan.LoanID, loan.CustomerID, loan.PrincipalAmount, loan.InterestRate, loan.LoanTerm, loan.LoanType, 'Pending')
        print(loan)
        confirm=input('Do you want to proceed with the loan application? (Y/N):')
        if confirm=='Y':
            self.cursor.execute(query,values)
            self.conn.commit()
            self.cursor.commit()
        else:
            print('Loan applicaton Cancelled')
            

    def calculateInterest(self, loan_id):
        try:
            result = self.getLoanbyId(loan_id)
        except Exception as e:
            print(e)
            return
        else:
            PrincipalAmount = result[2]
            InterestRate = result[3]
            Term = result[4]
            Interest = (PrincipalAmount * InterestRate * Term) / 12
            return Interest

    def loanStatus(self,loan_id):
        query = """ SELECT [CustomerID] FROM [Loan] WHERE [LoanID] = ?"""
        self.cursor.execute(query, (loan_id,))
        customerID = self.cursor.fetchone()[0]
        query = """ SELECT [CreditScore] FROM [Customer] WHERE [CustomerID] = ?"""
        self.cursor.execute(query, (customerID,))
        creditScore = self.cursor.fetchone()[0]
        if creditScore > 650:
            status = 'Approved'
        else:
            status = 'Pending'
        query = """ UPDATE [Loan] SET [LoanStatus] = ? WHERE [LoanID] = ?"""
        self.cursor.execute(query, (status, loan_id))
        self.cursor.commit()
        return status
        
    def calculateEMI(self, loan_id):
        try:
            result = self.getLoanbyId(loan_id)
        except Exception as e:
            print(e)
            return
        else:
            PrincipalAmount = result[2]
            MonthyInterest = (result[3] / 12) / 100
            Term = result[4]
            EMI = (PrincipalAmount * MonthyInterest * (1 + MonthyInterest) ** Term) / ((1 + MonthyInterest) ** Term - 1)
            return EMI
    
    
    def loanRepayment(self, loan_id, amount):
        MonthlyEMI = self.calculateEMI(loan_id)
        if MonthlyEMI == None:
            return
        if amount < MonthlyEMI:
            print("Payment Rejected. Insufficient payment.")
            return
        else:
            query = """ SELECT [PrincipalAmount] FROM [Loan] WHERE [LoanID] = ?"""
            self.cursor.execute(query, (loan_id,))
            principal_amount = self.cursor.fetchone()[0]
            initial_principal = principal_amount
            principal_amount -= amount
            query = """ UPDATE [Loan] SET [PrincipalAmount] = ? WHERE [LoanID] = ?"""
            self.cursor.execute(query, (principal_amount, loan_id))
            self.cursor.commit()
            result = f"Payment successful.Initial amount: {initial_principal} Remaining amount: {principal_amount}"
            print(result)

    def getAllLoans(self):
        try:
            self.cursor.execute("Select * from Loan")
            loans = self.cursor.fetchall()  # Get all data
            for loan in loans:
                print(loan)
        except Exception as e:
            print(e)
    
    def getLoanbyId(self, loan_id):
            self.cursor.execute(
                "Select * from Loan Where LoanID = ?", (loan_id,)
            )
            loans = self.cursor.fetchone()  # Get all data
            if len(loans) == 0:
                raise InvalidLoanException(loan_id)
            else:
                return loans
    

   
