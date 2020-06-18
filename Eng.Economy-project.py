#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT  OF  ECONOMY                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/17/6                                                    #
#                                                                                                                   #
#                                                                                                                   #
#################################################### MODULES ########################################################
import sys,time,os,random
################################################ PROJECT OBJECTS ####################################################
def cls():
    os.system(['clear','cls'][os.name=='nt'])
################################################### DEFINE FCN ######################################################
def DEFINE(us):
    while True:
        for counter in range(us)-1:
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|           FOR PROJECT {} :           |".format(counte+1))
        print("\t\t\t|        FEEL FOLLOWING FIELD :        |")
        input("\t\t\t| ENTER FIRST CAST:")
        input("\t\t\t| ENTER THE VALUE OF ABORTION:")    
        try:
            input("\t\t\t| ENTER MARR(in persent):")
            input("\t\t\t| ENTER INTEREST RATE(in persent):")
            input("\t\t\t| ENTER TAX RATE(in persent):")
        except :
            cls()
            print("\n\n\n\t\t\tPLEASE ENTER CORRECTLY!")
            counter -=1
            continue
        
        print("\t\t\t|______________________________________|")
#####################################################################################################################
def wait():
    value=random.random()
    for counter in range(int(5*value)):
        cls()
        print("\t\t\t                 WAITING",end='')
        print(".",end='')
        time.sleep(0.8)
        print(".",end='')
        time.sleep(0.8)
        print(".",end='')
        time.sleep(0.8)
#####################################################################################################################

#####################################################################################################################

################################################## MAIN MENU ########################################################
while True:
    cls()
    print("\t\t\t ______________________________________")
    print("\t\t\t|             WELCOME USER!            |")
    print("\t\t\t|      PLEASE  SELECT BY NUMBER:       |")
    print("\t\t\t|   1) DEFINE NEW SITUATION            |")
    print("\t\t\t|   2) ABOUT US!                       |")
    print("\t\t\t|   3) EXIT!                           |")
    print("\t\t\t|______________________________________|")
    selector=input()
    if selector=='1' :
        cls()
        print("\t\t\t _________________________________________ ")
        print("\t\t\t| HOW MANY PROJECT DO YOU WANT TO DEFINE? |")
        print("\t\t\t|_________________________________________|")
        us=input()
        DEFINE(us)
    elif selector=='2' :
            cls()
            print("\t\t\t ______________________________________ ")
            print("\t\t\t|             CREATED BY:              |")
            print("\t\t\t|        MOHAMMAD JAVAD  ADEL          |")
            print("\t\t\t|        ELECTRONIC ENGINIEER          |")
            print("\t\t\t|        IN DATE : 2020/29/5           |")
            print("\t\t\t|                                      |")
            print("\t\t\t|      1) BACK TO MAIN MENU            |")
            print("\t\t\t|      2) EXIT FROM APP                |")
            print("\t\t\t|______________________________________|")
            us=input()
            if us=='2':
                cls()
                exit=input("\n\n\t\t\tARE YOU SURE?(YES or NO)\n")
                if exit.upper()=="YES" or exit.upper()=='Y' :
                    sys.exit(0)
                elif exit.upper()=="NO" or exit.upper()=='N' :
                    pass
            else :
                pass        
    elif selector=='3' :
        cls()
        exit=input("\n\n\t\t\tARE YOU SURE?(YES or NO)\n")
        if exit.upper()=="YES" or exit.upper()=='Y' :
            sys.exit(0)
        elif exit.upper()=="NO" or exit.upper()=='N' :
            pass
        
    