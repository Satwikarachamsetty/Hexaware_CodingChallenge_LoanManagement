class CarLoan:
    def __init__(self, LoanID, CarModel, CarValue):
        self.LoanID = LoanID
        self.CarModel = CarModel
        self.CarValue = CarValue

    # Getter methods
    def getLoanID(self):
        return self.LoanID

    def getCarModel(self):
        return self.CarModel

    def getCarValue(self):
        return self.CarValue

    # Setter methods
    def setLoanID(self, LoanID):
        self.LoanID = LoanID

    def setCarModel(self, CarModel):
        self.CarModel = CarModel

    def setCarValue(self, CarValue):
        self.CarValue = CarValue
