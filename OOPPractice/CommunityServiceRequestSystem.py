class ServiceRequest:
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description

    def get_summary(self):
        return(f'___________________________________\n'
              f'{self.name} created Ticket #{self.number}.\n'
              f'Request: {self.description}')

class TechnologyRequest(ServiceRequest):
    def __init__(self, name, number, description, device):
        super().__init__(name, number, description)
        self.device = device

    def get_summary(self):
        return(f'___________________________________\n'
              f'{self.name} created Ticket #{self.number}.\n'
              f'Device: {self.device}\n'
              f'Issue: {self.description}')


class FacilitiesRequest(ServiceRequest):
    def __init__(self, name, number, description, location):
        super().__init__(name, number, description)
        self.location = location

    def get_summary(self):
        return(f'___________________________________\n'
              f'{self.name} created Ticket #{self.number}\n'
              f'Location: {self.location}\n'
              f'Description: {self.description}')


class FundRequest(ServiceRequest):
    def __init__(self, name, number ,description, amount):
        super().__init__(name, number,description)
        self.amount = amount

    def get_summary(self):
        return(f'___________________________________\n'
              f'{self.name} created Ticket #{self.number}\n'
              f'Amount: {self.amount}\n'
              f'Description: {self.description}')

servReq1 = ServiceRequest("John Adam",
                          1000,
                          "I need the contact information for a local food bank. ")
techReq1 = TechnologyRequest("Lily Brown",
                             1001,
                             "My Laptop won't charge",
                             "2025 M5 Macbook Air")
techReq2 = TechnologyRequest("Jack Lee",
                             1002,
                             "HDMI cable is missing for the Library projector",
                             "EX3290 3LCD Projector")
facReq1 = FacilitiesRequest("Sam Davis",
                            1003,
                            "I would like to serve room for meeting",
                            "Room 101")
facReq2 = FacilitiesRequest("Mia Clark",
                            1004,
                            "I need the library for a community event",
                            "Library 1st Floor")
fundReq = FundRequest("Dan White",
                      1005,
                      "I need this money to pay a construction company to fix potholes in the community.",
                      15000)
requests = [servReq1, techReq1, techReq2, facReq1, facReq2, fundReq]

for req in requests:
    print(req.get_summary())