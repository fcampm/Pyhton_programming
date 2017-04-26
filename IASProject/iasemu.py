#  -*- coding: utf-8 -*-
# Authors:
#           Fabián Camp Mussa
#
# Subject: Final Project
# Date: Before Final Exam
from __future__ import print_function
from __future__ import division
import iasemu2




def menu():
    print("\n")
    print("       ===============================    ")
    print("      |*** Welcome to IAS emulator ***|   ")
    print("      |            Menu               |   ")
    print("      |===============================|   ")
    print("      |     1. Binary                 |   ")
    print("      |     2. Hexadecimal            |   ")
    print("      |     3. Decimal                |   ")
    print("      |                               |   ")
    print("      |     4. Exit                   |   ")
    print("      | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |   ")

def menu2():
    print("\n")
    print("  =======================  ")
    print(" |    *** Run type ***   | ")
    print(" |=======================| ")
    print(" | 1. Fast Run           | ")
    print(" | 2. Low Run            | ")
    print(" |                       | ")
    print(" | 3. Return to Main Menu| ")
    print(" |_ _ _ _ _ _ _ _ _ _ _ _| ")

def main():
    while(True):
        menu()
        print("\n")
        option = int(input("Select and option: "))
        if option == 1:
            print("\n", "         Decimal           ")
            menu2()
            print("\n")
            option2 = int(input("Select and option: "))
            if option2 == 1:
                iasemu2.main()
            elif option2 == 2:
                iasemu2.main()
            elif option2 == 3:
                main()
            else:
                print("\n")
                print("Number ", option2, " it's not a valid option, returning to main menu")

        elif option == 2:
            print("\n", "       Hexadecimal         ")
            menu2()
            print("\n")
            option2 = int(input("Select and option: "))
            if option2 == 1:
                iasemu2.main()
            elif option2 == 2:
                iasemu2.main()
            elif option2 == 3:
                main()
        elif option == 3:
            print("\n", "         Decimal           ")
            menu2()
            option2 = int(input("Select and option: "))
            if option2 == 1:
                iasemu2.main()
            elif option2 == 2:
                iasemu2.main()
            elif option2 == 3:
                main()
        elif option == 4:
            print ("\n")
            print ("Thaks for using IAS emulator, come back soon")
            return
        else:
            print ("Number ",option, " it's not a valid option")
main()
