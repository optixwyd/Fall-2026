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

for req in requests:
    if isinstance(req, TechnologyRequest):
        print(f'Request {req.number} is a Technology Request')
    elif isinstance(req, FacilitiesRequest):
        print(f'Request {req.number} is a Facilities Request')
    elif isinstance(req, FundRequest):
        print(f'Request {req.number} is a Fund Request')
    elif isinstance(req,ServiceRequest):
        print(f'Request {req.number} is a Service Request')

if isinstance(servReq1, object):
    print(f"servReq1 is an instance of Python's object class")
else:
    print(f"servReq1 isn't an instance of Python's object class")




#Prediction: My guess is that for each of methods, it will print what is structured in each of its respective class.
#For example, techReq1 will print/return the name, ticket #, description, and device.
#Likewise, facReq2 will print/return the name, ticket #, description, and location.
#Lastly, fundReq will print/return the name, ticket #, description, and fund amount.

experiment = [techReq1, facReq2, fundReq]
for req in experiment:
    print(req.get_summary())
#When ran:
# ___________________________________
#Lily Brown created Ticket #1001.
#Device: 2025 M5 Macbook Air
#Issue: My Laptop won't charge
#___________________________________
#Mia Clark created Ticket #1004
#Location: Library 1st Floor
#Description: I need the library for a community event
#___________________________________
#Dan White created Ticket #1005
#Amount: 15000
#Description: I need this money to pay a construction company to fix potholes in the community.

#Q: How did Python determine which version of get_summary() to execute even though the loop
#used the same method call for every object?

#Python determined the version of get_summary() to execute because we can override methods.Inside each subclass,
#although we inherit attributes and methods from the superclass, ultimately what is written within the subclass
#for that objects method will be used. Ultimately, this a clear example of polymorphism, or dynamic binding, which
#allows python to determine which get_summary() to use, based on the class of the object at runtime.
