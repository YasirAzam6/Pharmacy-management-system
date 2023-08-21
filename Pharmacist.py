from stock import stock


class Pharmacist:
    global stocks
    stocks = stock()

    def __init__(self):
        opt = 0

        print("Welcome Pharmacist!...\n")

        print("1. Manage Orders")
        print("2. View Customer's Orders")
        print("3. Calculate Revenue")
        print("0. Exit\n")

        opt = eval(input("What shall you do today: "))

        if opt == 1:
            self._Orders_()
        elif opt == 2:
            self._Customer_()
        elif opt == 3:
            self._Revenue_()
        elif opt == 0:
            self._Exit_()
        else:
            print("No such option available.")

        # __init__(self) end

    def Alternative(opt):
        formula = stocks.ViewFormula(opt)
        print("Common formula found: " + formula)
        altmed = stocks.ViewAlternative(formula)

        print("My recommendations are:\n")
        print(altmed.head(10))
        

        # Alternative(self, opt)

    def _Orders_(self):
        print("What do you want to do")
        print("1. View Stock")
        print("2. Order Stock")
        print("3. Edit an entry")
        print("0. Exit")

        opt = eval(input("\nWhat shall you do today: "))

        if opt == 1:
            stocks.ViewStocks()
        elif opt == 2:
            stocks.EditStocks(opt)
        elif opt == 3:
            stocks.EditStocks(opt)
        elif opt == 0:
            pass
        else:
            print("\nNo such option available\n")

        # _Orders_(self) end

    def _Customer_(self):

        stocks.ViewSales()

        # __Customer__(self) end

    def _Revenue_(self):

        print("Total Revenue generated till now: ", stocks.CalculateRevenue())

        # _Revenue_(self) end

    def _Exit_(self):
        return 0

        #  _Exit_(self) end

