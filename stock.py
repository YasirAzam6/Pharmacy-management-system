import os
import time

import pandas as pd


class stock:
    _Stocks_ = pd.DataFrame()
    _Salelog_ = pd.DataFrame()

    if os.path.isfile("Stocks.csv"):
        _Stocks_ = pd.read_csv("Stocks.csv", encoding='unicode_escape')
    else:
        _Stocks_ = pd.DataFrame(columns=["Medicine Name", "Common Formula", "Dosage", "Quantity"])
        _Stocks_.to_csv("Stocks.csv", index=False)

    if os.path.isfile("Salelog.csv"):
        _Salelog_ = pd.read_csv("Salelog.csv", encoding='unicode_escape')
    else:
        _Salelog_ = pd.DataFrame(columns=["custID", "MedID", "Medicine Name", "Quantity", "Cost"])
        _Salelog_.to_csv("Salelog.csv", index=False)

    def __init__(self):

        pass

        # __init__(self) end

    # Public Functions
    def ViewStocks(self):
        _Stocks_ = self._Stocks_

        print("\nPrinting Medicine List:\n")
        print("\nFirst Ten Stock Medicines\n")
        print(_Stocks_.head(10))
        print("\nLast Ten Stock Medicines\n")
        print(_Stocks_.tail(10))
        print("")

        # ViewStocks(self) End

    def ViewSales(self):
        _Salelog_ = self._Salelog_
        i = 0
        while True:
            print("\nPrinting 100 entries:\n")

            print(_Salelog_.head(100))

            i += 100

            opt = input("Do you want to continue(y/n): ").lower()

            if opt == 'y':
                i += 100
                print(_Salelog_.head(i))
            else:
                break
        # ViewSales(self) End

    def EditStocks(self, opt):

        opt -= 1

        if opt == 1:
            self._OrderStock_()
        elif opt == 2:
            self._EditStockEntry_()
        else:
            print("No such option available.")

        # EditStocks(self) End

    def Sales(self, custid, opt, qtt, cost):
        _Stocks_ = self._Stocks_
        _Salelog_ = self._Salelog_

        switcher = {
            1: "Panadol",
            2: "Brufen",
            3: "Tricarden",
            4: "Xplendid",
            5: "Strepsils",
            6: "Sebastin",
            7: "Antial",
            8: "Neoprox",
            9: "Velosef",
            10: "Azolim",
            11: "Nocid",
            12: "Voverin SR",
            13: "Dicloran",
            14: "Arinac",
            15: "Ossobon-D",
            16: "Tenoret",
            17: "Perispa",
            18: "Kozivin",
            19: "Caflam",
            20: "No-Spa",
            21: "Biozit",
            22: "Zafnol",
            23: "Sipirion",
            24: "Colofac",
            25: "Puldol",
            26: "Novidat",
            27: "Flagyl",
            28: "Urigo",
            29: "Metodine",
            30: "Evion",
            31: "Cyrocin",
            32: "Brexin",
            33: "Motilium",
            34: "Imodium",
            35: "Sebesta",
            36: "Neurobion",
            37: "Brysk",
            38: "Tizoril",
            39: "Terlax",
            40: "Calpol",
            41: "Aspirin",
            42: "Arnica",
            43: "Danshen",
            44: "Moxtra",
            45: "Ashton",
            46: "Vivitrol",
            47: "Loratadine",
            48: "ibuprofen",
            49: "cephradine",
            50: "Cefazolin",
            51: "famotidine",
            52: "Diclonac",
            53: "Voverin SR",
            54: "ibuprofen",
            55: "Calcium 500+D",
            56: "Pretenol C",
            57: "Eperisone",
            58: "Azithromycin",
            59: "ibuprofen",
            60: "Drotaverine",
            61: "Atenolol",
            62: "Clopidogrel",
            63: "Mebeverine",
            64: "Diclofen",
            65: "Ciprofloxacin",
            66: "Tindamax",
            67: "Febuxostat",
            68: "Lomotil",
            69: "Ambrosia",
            70: "Cipro",
            71: "Piroxicam",
            72: "Domperidone",
            73: "Cholestyramine",
            74: "Ebastine",
            75: "M-Natal Plus",
            76: "Piroxicam",
            77: "Qiazol",
            78: "Tizanidine",
            79: "Tylenol"

        }

        if _Stocks_.at[opt - 1, "Quantity"] - qtt >= 0:
            stock = _Stocks_.at[opt - 1, "Quantity"]
            stock -= qtt
            _Stocks_.loc[opt - 1, "Quantity"] = [stock]
            self._Salelog_ = self._Salelog_.append({
                "Cost": cost,
                "MedID": opt - 1,
                "Medicine Name": switcher.get(opt),
                "Quantity": qtt,
                "custID": custid
            }, ignore_index=True)

            self._Salelog_.update(_Salelog_)
            self._Stocks_.update(_Stocks_)

            self._Stocks_.to_csv("Stocks.csv", index=False)
            self._Salelog_.to_csv("Salelog.csv", index=False)

            return "Transaction Successful"

        else:
            return "Transaction failed, Item not available."

        # EditSales(self) End

    def ViewFormula(self, opt):
        _Stocks_ = self._Stocks_

        return _Stocks_.loc[opt - 1, "Common Formula"]

        # ViewFormula(self, opt) End

    def ViewAlternative(self, formula):
        _Stocks_ = self._Stocks_
        altmed = _Stocks_[_Stocks_["Common Formula"] == formula]

        return altmed

        # ViewAlternative(self, formula) End

    def CalculateRevenue(self):
        _Salelog_ = self._Salelog_

        Revenue = 0

        for i in _Salelog_["Cost"]:
            Revenue += i

        return Revenue

        # CalculateRevenue(self) End

    # Private Functions
    def _OrderStock_(self):
        _Stocks_ = self._Stocks_
        print("What do you want to order:")
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

        print("\nPlacing order\n")
        time.sleep(1)
        print("\nOrder placed\n")
        time.sleep(1)

        if opt > 0 and opt < 80:
            _Stocks_.at[opt - 1, "Quantity"] += qtt
            _Stocks_.to_csv("Stocks.csv", index=False)
            self._Stocks_.update(_Stocks_)
        else:
            print("No such option available")

        print("\nOrder Arrived in Stock\n")

        # _OrderStock_(self) End

    def _EditStockEntry_(self):
        _Stocks_ = self._Stocks_
        print("What do you want to Edit:")
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

        if opt > 0 and opt < 80:
            _Stocks_.at[opt - 1, "Quantity"] -= qtt
            _Stocks_.to_csv("Stocks.csv", index=False)
            self._Stocks_.update(_Stocks_)
        else:
            print("No such option available")

        # _EditStockEntry_(self) End
