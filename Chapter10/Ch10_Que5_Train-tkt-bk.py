class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The seats available in the Train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the Ticket in the Train is : Rs.{self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(
                f"Your Ticket has beeen BOOKED !Your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("SORRY...this Train is FULL...Kindly try in TATKAAL.. ")

    def cancelTicket(self,seatsNo):
        pass

intercity = Train("Intercity Express:14681", 90., 2)
intercity.getStatus()
# intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
