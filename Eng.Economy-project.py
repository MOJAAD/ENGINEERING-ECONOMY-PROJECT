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
    project=[[0,0,0,0,0,0]]
    us=int(us)-1
    while True:
        for counter in range(us):
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t|           FOR PROJECT {} :            |".format(counter+1))
            print("\t\t\t|        FEEL FOLLOWING FIELD :        |")
            project[counter][0]=input("\t\t\t| ENTER FIRST CAST:")
            project[counter][1]=input("\t\t\t| ENTER THE VALUE OF ABORTION:")    
            try:
                project[counter][2]=int(input("\t\t\t| ENTER MARR(in persent):"))
                if project[counter][2]<=0 or project[counter][2]>=100:
                    project[counter][2]=int("typeerror")
                else :
                    project[counter][2]=project[counter][2]/100
                project[counter][3]=int(input("\t\t\t| ENTER TAX RATE(in persent):"))
                if project[counter][3]<=0 or project[counter][3]>=100:
                    project[counter][3]=int("typeerror")
                else:
                    project[counter][3]=project[counter][3]/100
                n=int(input("\t\t\t| ENTER LIFETIME(years):"))
                r=int(input("\t\t\t| ENTER INTEREST RATE(in persent):"))
                if r<=0 or r>=100:
                    r=int("typeerror")
                print("\t\t\t|______________________________________|")
                print("\t\t\t|    CHOOSE PRIOD OF INTEREST RATE:    |")
                print("\t\t\t| 1) ANNUAL                            |")
                print("\t\t\t| 2) SEMIANNUAL                        |")
                print("\t\t\t| 4) TRIMESTER                         |")
                print("\t\t\t| 12) MOUNTLY                          |")
                t=input("\t\t\t|______________________________________|")
                if int(t==1) or int(t)==2 or int(t)==4 or int(t)==12 :
                    r=r/100
                    project[counter][4]=((1+r)**t)-1
                
                # while True:
                #     input("\t\t\t| CHOOSE INCMOE/CAST TYPE:(1-constant 2-in a period 3-no one 4-next)")
                #     if _=='1':
                #         _=int("typeerror")
                #     if _=='2':
                #         _=int("typeerror")
                #     if _=='3':
                #         _=int("typeerror")
                #     if _=='4':
                #         break    
            except TypeError:
                cls()
                print("\n\n\n\t\t\tPLEASE ENTER CORRECTLY!")
                counter -=1
                continue
            
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
            print("\t\t\t|     STUDENT NUMBER: 9621010042       |")
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
        
    