class programmer():
    company = "Microsoft"
    def __init__ (self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and is working on the product {self.product}")

harry = programmer("harry","Laptop")
larry = programmer("Larry","comp")
harry.getInfo()
larry.getInfo()
