'''
To split bills
INPUT:
Initial: Names of members, Corpus fund if any

Every instance: Who paid how much, How many subscribers, Equal division(or not?)

On demand: Peer to peer transfer, forthwith settlement member's balance

OUTPUT:
Pool method:
All the money to be settled is put on table as per balance sheet and accessed by ones owed to

peer to peer(least transaction criterion):
Every member who owes money is transfers with one or multiple members, (as per least transfers calculated by the alogrithm to be designed?)

Future features:
Classification of expenditures(eg food, entertainment)
Statistical analysis and insights(based on classes of expenditures)
Online integration by creating and joining common room
Money transfers by UPI from app(if RBI approves :-P
'''
from typing import Dict, Any
import math
from datetime import datetime

master: dict[Any, Any] = {}
balSheet: dict[Any, Any] = {}
instSheet: dict[Any, Any] = {}
expSheet: dict[Any, Any] = {"All expenses": {}}
expSheet["All expenses"]["GRAND TOTAL"] = 0
allStatements = []


def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return ui


def intro():
    condition = 1
    while condition:
        name = sanitised_input("Enter member name: ", str)
        if name not in instSheet:
            memExp: dict[Any, Any] = {}
            # master[name] = 0
            instSheet[name] = 0
            expSheet[name] = memExp
            expSheet[name]["TOTAL"] = 0
            condition = 0
        else:
            print("Name already exists.")


def intro0():
    Member_Q = sanitised_input("How many members? ", int, 1)
    for i in range(0, Member_Q):
        intro()


def instNonUnif():
    expense = sanitised_input("Name of expense: ", str)
    members = (instSheet.keys())
    print(members)
    payee = sanitised_input("Who is paying? ", str, range_= members)
    subs = input("Subscribers (seperated by just comma): (* for all) ") #has to be integrated with santised_input
    if subs == '*':
        subsList = list(instSheet.keys())
    else:
        subsList = subs.split(",")
    payeeVal = sanitised_input("Payment value: ",float, 0)
    # master[payee] -= payeeVal
    instVal = payeeVal / len(subsList)
    instVal = round(instVal, 5)
    while len(subsList) != 0:
        for i in instSheet:
            if i in subsList:
                instSheet[i] += instVal
                expSheet[i][expense] = instVal
                expSheet[i]["TOTAL"] += instVal  # totalling should be optimised
                print(subsList)
                subsList.pop(0)
    expSheet["All expenses"]["GRAND TOTAL"] += payeeVal
    expSheet["All expenses"][expense] = payeeVal
    instSheet[payee] -= payeeVal
    print("\nTotal expense value: ", payeeVal, "\nExpense per member(who has subscribed): ", instVal,
          "\nBalance sheet: ", instSheet)


def transaction():
    expLen = len(expSheet["All expenses"])
    print(expLen)
    tolerance = 0.01
    est = 5
    if 10000 > expLen > 100:
        tolerance *= 100
        est += 2

    while not all(-tolerance < value < tolerance for value in instSheet.values()):
        # print("Balance Sheet:", instSheet)
        if max(instSheet.values()) <= abs(min(instSheet.values())):
            a = max(instSheet, key=instSheet.get)
            b = min(instSheet, key=instSheet.get)
            av = round(instSheet[a], est)
            bv = round(instSheet[b], est)
            statement = ("\n***     " + str(a) + " gives " + str(abs(av)) + " to " + str(b) + "     ***\n")
        else:
            b = max(instSheet, key=instSheet.get)
            a = min(instSheet, key=instSheet.get)
            av = round(instSheet[a], est)
            bv = round(instSheet[b], est)
            statement = ("\n***     " + str(b) + " gives " + str(abs(av)) + " to " + str(a) + "     ***\n")

        print(statement)
        allStatements.append(statement)
        instSheet[b] = bv + av
        instSheet[a] = 0
    print(instSheet)
    print("\n***\n\nExpenditure per member:")
    [print(key, ':', value) for key, value in expSheet.items()]
    print("\n***\n")


def saveTrans():
    cond = 1
    while cond == 1:
        save_stat = "Do you want to save the transactions? (y/n): "
        op = input(save_stat).lower()
        if  op == "y":

            file = (open("balance.txt", "w"))

            now = datetime.now()

            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
            file.write("At ")
            file.write(dt_string)

            for statement in allStatements:
                file.write(statement)


            #file.write((key, ':', value) for key, value in expSheet.items())

            file.close()
            cond = 0

        elif op == "n":
            cond = 0

        else:
            print("Wrong Input")
            op = input(op)


def main():  ## not sure if this is still true: loop is working only for order 0 -> 1 -> 2
    init_stat = "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "

    op = input(init_stat)
    while 1:
        if op == '0':  # switch case can be used
            intro0()
            op = input(init_stat)

        elif op == '1':
            if len(instSheet)==0:
                print("Members not initialized.")
                intro0()
            instNonUnif()
            op = input(init_stat)

        elif op == '2':
            # balance()
            transaction()
            saveTrans()
            op = input(init_stat)

        else:
            print("Wrong Input")
            op = input(init_stat)


main()
