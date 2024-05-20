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


   