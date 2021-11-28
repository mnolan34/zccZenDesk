import requests
import json

class ticketManager:
    
    def __init__(self):
        self.pageNum = 0
        self.ticketList = None


    def connect(self):
        url = 'https://zccterra.zendesk.com/api/v2/tickets.json'
        user = 'nolan.matt@northeastern.edu/token'
        token = 'us7JSCXEcuEZjlnMuqoo8cnCCIbe0hNT8jVlMcS4'

        #do the http get request
        response = requests.get(url, auth=(user,token))

        #check for codes besides 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
    
        #Decode JSON response into a dictionary, and use data
        data = response.json()
     
        ticketList = data['tickets']

        #for ticket in ticketList:
            #print(ticket['subject'])

        self.ticketList = ticketList

    #Function to list 25 tickets
    def listTickets(self):
        startTicket = 25*self.pageNum
        if(startTicket + 25 > len(self.ticketList)):
            endTicket = len(self.ticketList)
        else:
            endTicket = startTicket + 25

        for i in range(startTicket, endTicket):
            print("Ticket " + str(i) + " with subject: "
                  + self.ticketList[i]['subject'] + "opened by: " + str(self.ticketList[i]['requester_id']))

    #Function to print an individual ticket
    def printTicket(self, ticketNum):
        value = int(ticketNum)
        print("Ticket " + ticketNum + " with subject: "
                  + self.ticketList[value]['subject'] + " opened by: " + str(self.ticketList[value]['requester_id']))
        
    def menuList(self):
        print("\t Select view options:")
        print("\t * Press l to view all tickets")
        print("\t * Press t to view a ticket")
        print("\t * Press n to view next page of tickets")
        print("\t * Press p to view previous page of tickets")
        print("\t * Type quit to exit")

    #Function to print next page
    def nextPage(self):
        if(self.pageNum == len(self.ticketList)//25 - 1):
            print("Last page reached!")
        else:
            self.pageNum += 1
            print(len(self.ticketList))
            print("PAGE NUM", self.pageNum)
            self.listTickets()

    def prevPage(self):
        if(self.pageNum == 0):
            print("First page reached!")
        else:
            self.pageNum -= 1
            self.listTickets()


