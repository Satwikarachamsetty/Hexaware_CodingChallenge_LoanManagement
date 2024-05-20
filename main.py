from dao import ILoanService
from entity import HomeLoan, CarLoan,Loan,Customer


class MainMenu:

    loan_service= ILoanService()

    def loan_menu(self):
        while True:
            print(
                """      
            1. Apply for a Loan
            2. Calculate Interest
            3. Check Status of Loan
            4. Loan Repayment
            5. Calculate EMI
            6. View All Loans
            7. View Loan by ID
            8. Exit
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                LoanID = int(input("Please enter LoanID: "))
                CustomerID = int(input("Please enter CustomerID: "))
                PrincipalAmount = float(input("Please enter PrincipalAmount: "))
                InterestRate = float(input("Please enter InterestRate: "))
                LoanTerm = int(input("Please enter LoanTerm: "))
                LoanType = input("Please enter LoanType: ")
                LoanStatus = input("Please enter LoanStatus: ")
                new_loan = Loan(LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus)
                self.loan_service.applyLoan(new_loan)

            elif choice == 2:
                LoanID = int(input("Please enter LoanID: "))
                interest=self.loan_service.calculateInterest(LoanID)
                print(f'\n--> The Interest for the Loan of Loan ID: {LoanID} is {interest}')

            elif choice == 3:
                LoanID= int(input("Please enter Loan ID: "))
                status = self.loan_service.loanStatus(LoanID)
                print(f'\n--> The Status of Loan with Loan ID {LoanID} is {status}')

            elif choice== 4:
                LoanID = int(input("Please enter Loan ID: "))
                Amount = int(input("Please enter the amount you wanted to repay:"))
                self.loan_service.loanRepayment(LoanID,Amount)
            
            elif choice == 5:
                    LoanID = int(input("Please enter the Loan ID: "))
                    EMI = self.loan_service.calculateEMI(LoanID)
                    print(f"\n--> The EMI for the Loan of Load ID {LoanID} is: {EMI}")

            elif choice ==6:
                self.loan_service.getAllLoans()
            
            elif choice ==7:
                LoanID = int(input("Please enter LoanID: "))
                self.loan_service.getLoanbyId(LoanID)
    
            elif choice == 8:
                break
            
def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
               1. Loan Management    
               2. Exit  
                """
        )
        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.loan_menu()
        elif choice == 2:
            main_menu.loan_service.close() 
            print("Visit Again Soon....Good Day! 😊\n")
            break


if __name__ == "__main__":
    print("✨ 🎊 Welcome to Loan Management System 🎊 ✨")
    main()

    


