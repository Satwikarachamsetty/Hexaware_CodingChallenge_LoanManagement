class Customer:
    def __init__(self, CustomerID=None, Name=None, EmailAddress=None, Phone=None, Address=None, CreditScore=None):
        self.CustomerID = CustomerID
        self.Name = Name
        self.EmailAddress = EmailAddress
        self.Phone = Phone
        self.Address = Address
        self.CreditScore = CreditScore

    # Getter methods
    def getCustomerID(self):
        return self.CustomerID

    def getName(self):
        return self.Name

    def getEmailAddress(self):
        return self.EmailAddress

    def getPhone(self):
        return self.Phone

    def getAddress(self):
        return self.Address

    def getCreditScore(self):
        return self.CreditScore

    # Setter methods
    def setCustomerID(self, CustomerID):
        self.CustomerID = CustomerID

    def setName(self, Name):
        self.Name = Name

    def setEmailAddress(self, EmailAddress):
        self.EmailAddress = EmailAddress

    def setPhone(self, Phone):
        self.Phone = Phone

    def set_Address(self, Address):
        self.Address = Address

    def set_CreditScore(self, CreditScore):
        self.CreditScore = CreditScore
