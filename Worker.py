from Pharmacist import Pharmacist
from stock import stock


class Worker:
    global stocks
    stocks = stock()

    def __init__(self):
        opt = 0

        print("Welcome Worker!!...\n")

        print("1. Check medicine list")
        print("2. Place Customer order")
        print("3. Ask for Alternative")
        print("0. Exit\n")

        opt = eval(input("What shall you do today: "))

        if  opt == 1:
            self._Medicine_()
        elif opt == 2:
            self._Order_()
        elif opt == 3:
            self._Alternative_()
        elif opt == 0:
            self._Exit_()
        else:
            print("No such option available.")

    #__init__(self) end

    def _Medicine_(self):
        stocks.ViewStocks()

        # _Medicine_(self) end

    def _Order_(self):
        print("Which medicine is being asked for:")

        print("1: Panadol")
        print("2: Brufen")
        print("3: Tricarden")
        print("4: Xplendid")
        print("5: Strepsils")
        print("6: Sebastin")
        print("7: Antial")
        print("8: Neoprox")
        print("9: Velosef")
        print("10: Azolim")
        print("11: Nocid")
        print("12: Voverin SR")
        print("13: Dicloran")
        print("14: Arinac")
        print("15: Ossobon-D")
        print("16: Tenoret")
        print("17: Perispa")
        print("18: Kozivin")
        print("19: Caflam")
        print("20: No-Spa")
        print("21: Biozit")
        print("22: Zafnol")
        print("23: Sipirion")
        print("24: Colofac")
        print("25: Puldol")
        print("26: Novidat")
        print("27: Flagyl")
        print("28: Urigo")
        print("29: Metodine")
        print("30: Evion")
        print("31: Cyrocin")
        print("32: Brexin")
        print("33: Motilium")
        print("34: Imodium")
        print("35: Sebesta")
        print("36: Neurobion")
        print("37: Brysk")
        print("38: Tizoril")
        print("39: Terlax")
        print("40: Calpol")
        print("41: Aspirin")
        print("42: Arnica")
        print("43: Danshen")
        print("44: Moxtra")
        print("45: Ashton")
        print("46: Vivitrol")
        print("47: Loratadine")
        print("48: ibuprofen")
        print("49: cephradine")
        print("50: Cefazolin")
        print("51: famotidine")
        print("52: Diclonac")
        print("53: Voverin SR")
        print("54: ibuprofen")
        print("55: Calcium 500+D")
        print("56: Pretenol C")
        print("57: Eperisone")
        print("58: Azithromycin")
        print("59: ibuprofen")
        print("60: Drotaverine")
        print("61: Atenolol")
        print("62: Clopidogrel")
        print("63: Mebeverine")
        print("64: Diclofen")
        print("65: Ciprofloxacin")
        print("66: Tindamax")
        print("67: Febuxostat")
        print("68: Lomotil")
        print("69: Ambrosia")
        print("70: Cipro")
        print("71: Piroxicam")
        print("72: Domperidone")
        print("73: Cholestyramine")
        print("74: Ebastine")
        print("75: M-Natal Plus")
        print("76: Piroxicam")
        print("77: Qiazol")
        print("78: Tizanidine")
        print("79: Tylenol")

        opt = eval(input("Your option: "))
        qtt = eval(input("How much: "))
        custid = eval(input("Enter an ID for the customer(in numbers): "))
        cost = eval(input("Enter the cost of the purchase: "))

        print(stocks.Sales(custid, opt, qtt, cost))

        # _Order_(self) end

    def _Alternative_(self):
        print("1: Panadol")
        print("2: Brufen")
        print("3: Tricarden")
        print("4: Xplendid")
        print("5: Strepsils")
        print("6: Sebastin")
        print("7: Antial")
        print("8: Neoprox")
        print("9: Velosef")
        print("10: Azolim")
        print("11: Nocid")
        print("12: Voverin SR")
        print("13: Dicloran")
        print("14: Arinac")
        print("15: Ossobon-D")
        print("16: Tenoret")
        print("17: Perispa")
        print("18: Kozivin")
        print("19: Caflam")
        print("20: No-Spa")
        print("21: Biozit")
        print("22: Zafnol")
        print("23: Sipirion")
        print("24: Colofac")
        print("25: Puldol")
        print("26: Novidat")
        print("27: Flagyl")
        print("28: Urigo")
        print("29: Metodine")
        print("30: Evion")
        print("31: Cyrocin")
        print("32: Brexin")
        print("33: Motilium")
        print("34: Imodium")
        print("35: Sebesta")
        print("36: Neurobion")
        print("37: Brysk")
        print("38: Tizoril")
        print("39: Terlax")
        print("40: Calpol")
        print("41: Aspirin")
        print("42: Arnica")
        print("43: Danshen")
        print("44: Moxtra")
        print("45: Ashton")
        print("46: Vivitrol")
        print("47: Loratadine")
        print("48: ibuprofen")
        print("49: cephradine")
        print("50: Cefazolin")
        print("51: famotidine")
        print("52: Diclonac")
        print("53: Voverin SR")
        print("54: ibuprofen")
        print("55: Calcium 500+D")
        print("56: Pretenol C")
        print("57: Eperisone")
        print("58: Azithromycin")
        print("59: ibuprofen")
        print("60: Drotaverine")
        print("61: Atenolol")
        print("62: Clopidogrel")
        print("63: Mebeverine")
        print("64: Diclofen")
        print("65: Ciprofloxacin")
        print("66: Tindamax")
        print("67: Febuxostat")
        print("68: Lomotil")
        print("69: Ambrosia")
        print("70: Cipro")
        print("71: Piroxicam")
        print("72: Domperidone")
        print("73: Cholestyramine")
        print("74: Ebastine")
        print("75: M-Natal Plus")
        print("76: Piroxicam")
        print("77: Qiazol")
        print("78: Tizanidine")
        print("79: Tylenol")

        opt = eval(input("Your option: "))

        Pharm = Pharmacist

        Pharm.Alternative(opt)

        # _Alternative_(self) end

    def _Exit_(self):
        return 0

        #  _Exit_(self) end
