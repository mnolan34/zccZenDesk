from zenDeskCode import ticketManager

class driver:

    def main():
        task = ticketManager()
        task.connect()
        print('Welcome to the ticket viewer')
        print("Type 'menu' to view options or 'quit' to exit")
        command = input()
        while command != 'q':
            #ListCommand
            if(command == 'l'):
                task.listTickets()
                command = input()
            #Menu Command
            elif(command == 'menu'):
                task.menuList()
                command = input()
            #Quit Command
            elif(command == 'quit'):
                command = 'q'
            #nextPage Command
            elif(command == 'n'):
                task.nextPage()
                command = input()
            #prevPage Command
            elif(command == 'p'):
                task.prevPage()
                command = input()
            #specificTicket Command
            elif(command == 't'):
                ticket = input("Enter ticket number:")
                task.printTicket(ticket)
                command = input()
            #If command unrecognized, ask again
            else:
                print("Command unrecognized: please try again")
                command = input()

    if __name__ == "__main__":
        main()
