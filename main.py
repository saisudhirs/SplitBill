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


def intro():
    name = input("Enter member name: ")
    master[name] = 0


def intro0():
    Member_Q = int(input("How many members? "))
    for i in range(0, Member_Q):
        intro()


def instUnif():
    print(master.keys())
    payee = input("Who is paying? ")
    payeeVal = float(input("Payment value: "))
    master[payee] -= payeeVal


def balance():
    totBal = sum(master.values())
    costMem = totBal / len(master)  # remember that this is a negative value
    for i in master:
        balSheet[i] = master[i] - costMem


def transaction():
    while not all(value == 0 for value in balSheet.values()):
        print("Balance Sheet:", balSheet)
        if max(balSheet.values()) <= abs(min(balSheet.values())):
            a = max(balSheet, key=balSheet.get)
            b = min(balSheet, key=balSheet.get)
            print(a, "gives all to", b)
        else:
            b = max(balSheet, key=balSheet.get)
            a = min(balSheet, key=balSheet.get)
            print(b, "gives required to", a)

        balSheet[b] = balSheet[b] + balSheet[a]
        balSheet[a] = 0
        print(balSheet)


def main():  # loop is workking only for order 0 > 1 > 2
    op = int(
        input("Options:\n0 for initializing members\n1 for new expense\n2 for showing balance transactions\nInput: "))

    if op == 0:  # switch case can be used
        intro0()
        main()
    elif op == 1:
        instUnif()
        main()
    elif op == 2:
        balance()
        transaction()
        main()
        print("Master list", master)
    else:
        print("Wrong Input")
        main()


main()
