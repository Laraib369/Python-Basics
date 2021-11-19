class Train():
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in train are {self.seats}")

    def fareInfo(self):
        print(f"The fare is Rs.{self.fare} ")

    def bookTicket(self):
        if self.seats >0:
            print(f"Your ticket has been booked, Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry!!!, All the seats have been booked")

    def cancelTicket(self, seatNo):
        pass



intercity = Train("Intercity Express :  14099",90,300)

intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()

