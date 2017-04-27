#  -*- coding: utf-8 -*-
# Authors:
#           Fabián Camp Mussa
#
# Subject: Final Project
# Date: Before Final Exam
from __future__ import print_function
from __future__ import division
import iasemu2

PC = 0
left = True
AC = 0
MQ = 0
memory=[]
listing=[]

#===================================================================================================================================#
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
#===================================================================================================================================#
def menu2():
    print("\n")
    print("     =================================    ")
    print("    |    ***  RUNNING MENU ***        |   ")
    print("    |=================================|   ")
    print("    |      1. Fast Running            |   ")
    print("    |      2. Slow Running            |   ")
    print("    |                                 |   ")
    print("    |      3. Return to Main Menu     |   ")
    print("    | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |   ")

#===================================================================================================================================#
def readdatos_txt():
    with open ("datos.txt", 'r') as datos_list:
        global memory
        memory = datos_list.readlines()
#===================================================================================================================================#
def readprg1_txt():
    #name = "prg1.txt"
    #print ("Opening document", name, "this will take some time...")
    with open("prg1.txt", 'r') as instruction_list:
        reading_inst = instruction_list.readlines()
        global listing
        listing = reading_inst
#===================================================================================================================================#
def read_instructions(OP, AD):
    global PC
    global left
    global AC
    global MQ
    global memory


    AD = int(AD, 16)

    # Begin Data transfer instruction set

    # LOAD MQ
    if (OP == "0A"):
        AC = MQ
    # LOAD MQ, M(X)
    if (OP == "09"):
        MQ = int(memory[AD], 16)
    # STOR M(X)
    if (OP == "21"):
        if (AC >= 0):
            memory[AD] = str(hex(AD))
        else:
            memory[AD] = str(hex(int(complemetA2(abs(AC)), 2)))
    # LOAD M(X)
    if (OP == "01"):
        AC = int(memory[AD], 16)
    # LOAD -M(X)
    if (OP == "02"):
        AC = int(memory[AD], 16) * -1
    # LOAD |M(X)|
    if (OP == "03"):
        AC = abs(int(memory[AD], 16))
    # LOAD -|M(X)|
    if (OP == "04"):
        AC = abs(int(memory[AD],16)) * -1
    # Begin unconditional branch

    # JUMP M(X, 0:19)
    if (OP == "0D"):
        PC = AD
        left = True
    # JUMP M(X, 20:39)
    if (OP == "0E"):
        PC = AD
        left = False

    # Begin conditional branch

    # JUMP + M(X, 0:19)
    if (OP == "0F" and AC >= 0):
        PC = AD
        left = True
    # JUMP + M(X, 20:39)
    if (OP == "10" and AC >= 0):
        PC = AD
        left = False

    # Begin Arithmetic

    # ADD M(X)
    if (OP == "05"):
        AC += int(memory[AD], 16)
    # ADD |M(X)|
    if (OP == "07"):
        AC += abs(int(memory[AD], 16))
    # SUB M(X)
    if (OP == "06"):
        AC -= int(memory[AD], 16)
    # SUB |M(X)|
    if (OP == "08"):
        AC -= abs(int(memory[AD], 16))
    # MUL M(X)
    if (OP == "0B"):
        AC *= int(memory[AD], 16)
    # DIV M(X)
    if (OP == "0C"):
        var = AC
        AC %= int(memory[AD], 16)
        MQ =var // int(memory[AD], 16)
    # LSH
    if (OP == "14"):
        AC *= 2
    # RSH
    if (OP == "15"):
        Ac /= 2

    # Begin Address modify

    # STOR M(X, 8:19)
    if (OP == "12"):
        left = True
        memory[AD] = AC
    # STOR M(X, 28:39)
    if (OP == "13"):
        left = False
        memory[AD] = AC
    # HALT instruction
    if OP == "00" and AD == 0:
        #print("HALT")
        return

    print("\n")
    print("AC: ", bin(AC), "\t", hex(AC), "\t", AC)
    print("\n")
    print("MQ: ", bin(MQ), "\t", hex(MQ), "\t", MQ)
    print("\n")
    print("PC: ", bin(PC), "\t", hex(PC), "\t", PC)
    print("\n")
#===================================================================================================================================#
def complemetA2(decimal):
    flag1exists = False
    decimal_toA2 = ""

    while (decimal != 0):
        if (flag1exists == False):
            if (decimal % 2 == 0):
                decimal_toA2 += "0"
            else:
                decimal_toA2 += "1"
                flag1exists = True
        else:
            if (decimal % 2 == 0):
                decimal_toA2 += "1"
            else:
                decimal_toA2 += "0"
        decimal //= 2

    if (len(decimal_toA2) < 8):
        decimal_toA2 = "1" * (8 - len(decimal_toA2))
    return decimal_toA2[::-1]
#===================================================================================================================================#
def printresultsbin():
    global AC
    global MQ
    global PC
    print("\n")
    print("AC: ", bin(AC))
    print("\n")
    print("MQ: ", bin(MQ))
    print("\n")
    print("PC: ", bin(PC))
    print("\n")
#===================================================================================================================================#
def printresultshexa():
    global AC
    global MQ
    global PC
    print("\n")
    print("AC: ", hex(AC))
    print("\n")
    print("MQ: ", hex(MQ))
    print("\n")
    print("PC: ", hex(PC))
    print("\n")
#===================================================================================================================================#
def printresultsdecimal():
    global AC
    global MQ
    global PC
    print("\n")
    print("AC: ", AC)
    print("\n")
    print("MQ: ", MQ)
    print("\n")
    print("PC: ", PC)
    print("\n")
#===================================================================================================================================#
def main():
    global PC
    global left

    readprg1_txt()
    readdatos_txt()
    content = listing[0]

    while (PC != len(listing)):
        PC += 1
        OP1 = content[0:2]
        AD1 = content[2:5]
        OP2 = content[5:7]
        AD2 = content[7:10]
        if (left == True):
            left = False
            read_instructions(OP1, AD1)

        if (left == False):
            left = True
            read_instructions(OP2, AD2)

        if len(listing) != PC:
            content =  listing[PC]

    while(True):
        menu()
        print("\n")
        option = int(input("Select and option: "))
        if option == 1:
            print("\n", "         Binary           ")
            menu2()
            print("\n")
            option2 = int(input("Select and option: "))
            if option2 == 1:
                printresultsbin()
            elif option2 == 2:
                print("Funciona")
            elif option2 == 3:
                main()
            else:
                print("\n")
                print("Number ", option2, " it's not a valid option, returning to main menu")

        elif option == 2:
            print("\n", "       Hexadecimal         ")
            menu2()
            option2 = int(input("Select and option: "))
            if option2 == 1:
                printresultshexa()
            elif option2 == 2:
                print("Funciona")
            elif option2 == 3:
                main()
            else:
                print("\n")
                print("Number ", option2, " it's not a valid option, returning to main menu")
        elif option == 3:
            print("\n", "         Decimal           ")
            menu2()
            option2 = int(input("Select and option: "))
            if option2 == 1:
                printresultsdecimal()
            elif option2 == 2:
                print("Funciona")
            elif option2 == 3:
                main()
            else:
                print("\n")
                print("Number ", option2, " it's not a valid option, returning to main menu")
        elif option == 4:
            print ("\n")
            print ("Thaks for using IAS emulator, come back soon")
            return
        else:
            print ("Number ",option, " it's not a valid option")


main()
