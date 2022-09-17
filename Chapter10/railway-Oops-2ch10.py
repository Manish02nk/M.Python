class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print(f"The Name of Travelar is {self.name}.")
        print(f"The Train Name is {self.train}.")


manishsApplication = RailwayForm()
manishsApplication.name = "Manish"
manishsApplication.train = "Rajdhani Express-14681"
manishsApplication.printData()
