from ZCCZen import zenDeskCode

class driver:

    def main():
        task = ticketManager()
        data = task.connect
        data = factorData()
        print('Welcome to the ticket viewer')
        print("Type'menu' to view options or 'quit' to exit")
        command = input()
        while command != 'q':
            #ListCommand
            if(command == 'l'):
                task.listTickets()
            #Menu Command
            elif(command == 'menu'):
                task.menuList()
            #Quit Command
            elif(command == 'quit'):
                command = 'q'
            #nextPage Command
            elif(command == 'n'):
                task.nextPage()
            #prevPage Command
            elif(command == 'p'):
                task.prevPage()
            #specificTicket Command
            elif(command == 't'):
                continue
            #If command unrecognized, ask again
            else:
                print("Command unrecognized: please try again")

    if __name__ == "__main__":
        main()
