class programmer():
    company = "Microsoft"

    def __init__(self,name,salary,product):
        self.name = name
        self.salary = salary
        self.product = product

    def getInfo(self):
        print(f"The programmer of {self.company} named {self.name} is working on {self.product} for {self.salary} ")

harry = programmer("harry","200k","Laptop")
larry = programmer("larry","600k","comp")
harry.getInfo()
larry.getInfo()