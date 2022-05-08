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

master: dict[Any, Any] = {}
balSheet: dict[Any, Any] = {}
instSheet: dict[Any, Any] = {}
expSheet: dict[Any, Any] = {"All expenses": {}}


def intro():
    name = input("Enter member name: ")
    memExp: dict[Any, Any] = {}
    # master[name] = 0
    instSheet[name] = 0
    expSheet[name] = memExp
    expSheet[name]["TOTAL"] = 0


def intro0():
    Member_Q = int(input("How many members? "))
    for i in range(0, Member_Q):
        intro()


def instNonUnif():
    expense = input("Name of expense: ")
    print(instSheet.keys())
    payee = input("Who is paying? ")
    subs = input("Subscribers (seperated by just comma): (* for all) ")
    if subs == '*':
        subsList = list(instSheet.keys())
    else:
        subsList = subs.split(",")
    payeeVal = float(input("Payment value: "))
    # master[payee] -= payeeVal
    instVal = payeeVal / len(subsList)
    instVal = round(instVal, 5)
    for i in instSheet:
        if i in subsList:
            instSheet[i] += instVal
            expSheet[i][expense] = instVal
            expSheet[i]["TOTAL"] += instVal  # totalling should be optimised
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
            print("\n***", a, "gives", abs(av), "to", b, "***\n")
        else:
            b = max(instSheet, key=instSheet.get)
            a = min(instSheet, key=instSheet.get)
            av = round(instSheet[a], est)
            bv = round(instSheet[b], est)
            print("\n***", b, "gives", abs(av), "to", a, "***\n")

        instSheet[b] = bv + av
        instSheet[a] = 0
    print(instSheet)
    print("\n***\n\nExpenditure per member:")
    [print(key, ':', value) for key, value in expSheet.items()]
    print("\n***\n")


def main():  # not sure if this is still true: loop is working only for order 0 -> 1 -> 2
    op = (
        input(
            "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "))
    while 1:
        if op == '0':  # switch case can be used
            intro0()
            op = (
                input(
                    "\n-----\nOptions:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "))

        elif op == '1':
            instNonUnif()
            op = (
                input(
                    "\n-----\nOptions:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "))

        elif op == '2':
            # balance()
            transaction()
            op = (
                input(
                    "\n-----\nOptions:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "))

        else:
            print("Wrong Input")
            op = (
                input(
                    "\n-----\nOptions:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\n-----\nInput: "))


main()
