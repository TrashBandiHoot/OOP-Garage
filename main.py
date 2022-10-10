
"""Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

By the end of this project each student should be able to:
- Explain and/or demonstrate creating classes
- Explain and/or demonstrate creating class methods
- Explain and/or demonstrate class instantiation"""

class ParkingGarage():
    currentTickets = {}
    takenTickets = []
    takenSpots = []


    def __init__(self, tickets, parkingSpots):
        self.tickets = tickets
        self.parkingSpots = parkingSpots


    def takeTicket(self):
        self.takenTickets.append(self.tickets.pop())
        self.takenSpots.append(self.parkingSpots.pop())
        self.currentTickets["paid"] = False
        print(self.takenTickets)
        print(self.tickets)

    def payForParking(self):
        payment = input("Please enter amount(10): ")
        if payment == "10":
            print("Ticket has been paid, you have 15 minutes to exit the Garage.")
            self.currentTickets.update({"paid": True})
            print(self.currentTickets)
        else:
            print("Tickets are 10 dollars, please input the correct amount")

    def leaveGarage(self):
        if self.currentTickets["paid"]:
            print("Thank you, have a nice day!")
            self.tickets.append(self.takenTickets.pop())
            self.parkingSpots.append(self.takenSpots.pop())
        else:
            self.payForParking()
        


tickets = [1, 2, 3, 4, 5]
parking_spots = [1, 2, 3, 4, 5]


garage = ParkingGarage(tickets, parking_spots)

while True:
    user_input = input("What would you like to do? take/pay/leave/quit: ").lower()

    if user_input == "quit":
        break
    elif user_input == 'take':
        garage.takeTicket()
    elif user_input == 'pay':
        garage.payForParking()
    elif user_input == 'leave':
        garage.leaveGarage()