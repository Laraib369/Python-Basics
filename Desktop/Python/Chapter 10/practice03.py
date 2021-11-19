class Train():
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getInfo(self):
        print(f"The name of the passenger is {self.name}")    
        print(f"There are {self.seats} available")

    def getFare(self):
        print(f"The fare is {self.fare}")

    def getStatus(self):
        if self.seats > 0 :
            print(f"Your seat has been booked ,your seat number is {self.seats}")
            self.seats = self.seats - 1

        else:
            print("Sorry!!!,All saets have been booked")

a = Train("larry",300,100)
a.getInfo()
a.getFare()
a.getStatus()

   


larry = Train("larry","40","300")
larry.getInfo()