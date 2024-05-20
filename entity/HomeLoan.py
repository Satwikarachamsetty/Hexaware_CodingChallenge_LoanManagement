class HomeLoan:
    def __init__(self, LoanID, PropertyAddress, PropertyValue):
        self.LoanID = LoanID
        self.PropertyAddress = PropertyAddress
        self.PropertyValue = PropertyValue

    # Getter methods
    def getLoanID(self):
        return self.LoanID

    def getPropertyAddress(self):
        return self.PropertyAddress

    def getPropertyValue(self):
        return self.PropertyValue

    # Setter methods
    def setLoanID(self, LoanID):
        self.LoanID = LoanID

    def setPropertyAddress(self, PropertyAddress):
        self.PropertyAddress = PropertyAddress

    def setPropertyValue(self, PropertyValue):
        self.PropertyValue = PropertyValue
