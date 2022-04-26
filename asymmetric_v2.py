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


def intro():
    name = input("Enter member name: ")
    #master[name] = 0
    instSheet[name] = 0


def intro0():
    Member_Q = int(input("How many members? "))
    for i in range(0, Member_Q):
        intro()


def instNonUnif():
    print(instSheet.keys())
    payee = input("Who is paying? ")
    subs = input("Subscribers (seperated by comma): ")
    subsList = subs.split(",")
    payeeVal = float(input("Payment value: "))
    #master[payee] -= payeeVal
    instVal = payeeVal / len(subsList)
    for i in instSheet:
        if i in subsList:
            instSheet[i] += instVal
    instSheet[payee] -= payeeVal
    print(instVal, payeeVal, instSheet)


def transaction():
    while not all(value == 0 for value in instSheet.values()):
        print("Balance Sheet:", instSheet)
        if max(instSheet.values()) <= abs(min(instSheet.values())):
            a = max(instSheet, key=instSheet.get)
            b = min(instSheet, key=instSheet.get)
            av = instSheet[a]
            bv = instSheet[b]
            print("\n***", a, "gives ", abs(av), " to", b, "***\n")
        else:
            b = max(instSheet, key=instSheet.get)
            a = min(instSheet, key=instSheet.get)
            av = instSheet[a]
            bv = instSheet[b]
            print("\n***", b, "gives ", abs(av), " to", a, "***\n")

        instSheet[b] = bv + av
        instSheet[a] = 0
        print(instSheet)


def main():  # loop is working only for order 0 > 1 > 2
    op = int(
        input("Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))
    while 1:
        if op == 0:  # switch case can be used
            intro0()
            op = int(
                input(
                    "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))

        elif op == 1:
            instNonUnif()
            op = int(
                input(
                    "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))

        elif op == 2:
            #balance()
            transaction()
            print("Master list", instSheet)
            op = int(
                input(
                    "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))

        else:
            print("Wrong Input")
            op = int(
                input(
                    "Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))


main()
