class InvalidLoanException(Exception):
     def __init__(self, LoanID):
        super().__init__(f"Loan with {LoanID} is not Found")