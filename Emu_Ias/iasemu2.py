#  -*- coding: utf-8 -*-
# Authors:
#           Fabián Camp Mussa
#
# Subject: Final Project
# Date: Before Final Exam
from __future__ import print_function
from __future__ import division
PC = 0
left = True
AC = 0
MQ = 0
#===================================================================================================================================#
def readdatos_txt():
    with open ("datos.txt", 'r') as datos_list:
        memory = datos_list.readlines()
        return memory
#===================================================================================================================================#
def readprg1_txt():
    #name = "prg1.txt"
    #print ("Opening document", name, "this will take some time...")
    with open("prg1.txt", 'r') as instruction_list:
        reading_inst = instruction_list.readlines()
        listing = reading_inst[0]
        return listing
#===================================================================================================================================#
def read_instructions(OP, AD):
    global PC
    global left
    global AC
    global MQ


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
#    if (OP == "0D"):
        # Implement
    # JUMP M(X, 20:39)
#    if (OP == "0E"):
        # Implement

    # Begin conditional branch

    # JUMP + M(X, 0:19)
#    if (OP == "0F"):
        # Implement
    # JUMP + M(X, 20:39)
#    if (OP == "10"):
        # Implement

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
#    if (OP == "12"):
        # Implement
    # STOR M(X, 28:39)
#    if (OP == "13"):
        # Implement
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
def main():
    global PC
    global left
    readprg1_txt()


    #while (PC != len(reading_inst)):
    #    PC += 1



main()
