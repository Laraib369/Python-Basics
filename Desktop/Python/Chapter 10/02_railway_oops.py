class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Express is {self.train}")

Laraibsapplication = RailwayForm()
Laraibsapplication.name = "Laraib"
Laraibsapplication.train = "Rajdhani"
Laraibsapplication.printData()