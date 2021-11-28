from zenDeskCode import ticketManager

class unitTests:

        #Test printTicket with int negative
        def unitTest1():
                test1 = ticketManager()
                test1.connect()
                test1.printTicket(-1)
                print("Above should print Ticket does not exist")

        #Test printTicket with int too high
        def unitTest2():
                test2 = ticketManager()
                test2.connect()
                test2.printTicket(1000)
                print("Above should print Ticket does not exist")

        #Test printTicket with string
        def unitTest3():
                test3 = ticketManager()
                test3.connect()
                test3.printTicket('blue')
                print("Above should print Please enter an integer value")

        #Test nextPage end page
        def unitTest4():
                test4 = ticketManager()
                test4.connect()
                test4.pageNum = 3
                test4.nextPage()
                print("Above should say Last Page Reached")

        #Test prevPage beginning page
        def unitTest5():
                test5 = ticketManager()
                test5.connect()
                test5.prevPage()
                print("ABove should say first page reached")

        unitTest1()
        unitTest2()
        unitTest3()
        unitTest4()
        unitTest5()
