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
import sys,time,os
################################################ PROJECT OBJECTS ####################################################
def cls():
    os.system(['clear','cls'][os.name=='nt'])
#####################################################################################################################

#####################################################################################################################

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
        #DEFINE(us)
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
        
    