class Loan:
    def __init__(self, LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus):
        self.LoanID = LoanID
        self.CustomerID = CustomerID
        self.PrincipalAmount = PrincipalAmount
        self.InterestRate = InterestRate
        self.LoanTerm = LoanTerm
        self.LoanType = LoanType
        self.LoanStatus = LoanStatus

    # Getter methods
    def getLoanID(self):
        return self.LoanID

    def getCustomerID(self):
        return self.CustomerID

    def getPrincipalAmount(self):
        return self.PrincipalAmount

    def getInterestRate(self):
        return self.InterestRate

    def getLoanTerm(self):
        return self.LoanTerm

    def getLoanType(self):
        return self.LoanType

    def getLoanStatus(self):
        return self.LoanStatus

    # Setter methods
    def setLoanID(self, LoanID):
        self.LoanID = LoanID

    def setCustomerID(self, CustomerID):
        self.CustomerID = CustomerID

    def setPrincipalAmount(self, PrincipalAmount):
        self.PrincipalAmount = PrincipalAmount

    def setInterestRate(self,InterestRate):
        self.InterestRate = InterestRate

    def setLoanTerm(self, LoanTerm):
        self.LoanTerm = LoanTerm

    def setLoanType(self,LoanType):
        self.LoanType = LoanType

    def setLoanStatus(self, LoanStatus):
        self.LoanStatus = LoanStatus
