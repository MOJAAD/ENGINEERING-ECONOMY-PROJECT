#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT  OF  ECONOMY                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/21/6                                                    #
#                                                                                                                   #
#                                                                                                                   #
#################################################### MODULES ########################################################
import sys,time,os,random
################################################# CLEAR SCREEN ######################################################
def cls():
    os.system(['clear','cls'][os.name=='nt'])
################################################## DEFINE  FCN ######################################################
def DEFINE(us):
    project=[[0,0,0,0,0,0,0,0]]
    us=int(us)
    if us>=1:
        counter=0
        for counter in range(us-1):
            project.append([0,0,0,0,0,0,0,0])
    counter=0
    while counter<us:
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|           FOR PROJECT {} :            |".format(counter+1))
        print("\t\t\t|        FEEL FOLLOWING FIELD :        |")
        try:
            project[counter][0]=int(input("\t\t\t| ENTER FIRST CAST:"))
            project[counter][1]=int(input("\t\t\t| ENTER THE VALUE OF ABORTION:"))    
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
            project[counter][4]=int(input("\t\t\t| ENTER LIFETIME(years):"))
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
            if int(t)==1 or int(t)==2 or int(t)==4 or int(t)==12 :
                r=r/100
                project[counter][5]=((1+r)**int(t))-1
            else:
                project[counter][4]=int('typeerror')
            project[counter][6]=int(input("\t\t\t| ENTER ANNUAL PAYMENT:"))
            project[counter][7]=int(input("\t\t\t| ENTER FUTURE VALUE:"))    
            counter=counter+1
        except ValueError or TypeError:
            cls()
            print("\n\n\n\t\t\tPLEASE ENTER CORRECTLY!")
            time.sleep(1)
            continue
    counter=0
    for counter in range(us):
        print("\t\t\t| project {} : {}".format(counter+1,project[counter]))
    input("\t\t\t| press any key to continue...")
    return project
################################################### WAIT  FCN #######################################################
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
################################################## COMPUTE FCN ######################################################
def COMPUTE(project):
    while True:
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|       CHOOSE METHOD BY NUMBER:       |")
        print("\t\t\t|   1) NPW                             |")
        print("\t\t\t|   2) NEU                             |")
        print("\t\t\t|   3) ROR                             |")
        print("\t\t\t|   4) IGNORE!                         |")
        selector=input("\t\t\t|______________________________________|")
        tot=[0]
        for counter in range(len(project)-1):
            tot.append([0])
        if selector=='1':
            pass
        elif selector=='2':
            for counter in range(len(project)-1):
                pass            
        elif selector=='3':
            pass
        elif selector=='4':
            break
############################################### (P/F,%i,n) FACTOR ###################################################            
def PFFACTOR(f,i,n):
    p=1/((1+i)**n)
    p=p*f
    return p
############################################### (P/A,%i,n) FACTOR ###################################################
def PAFACTOR (a,i,n):
    p=(((1+i)**n)-1)/(i*((1+i)**n))
    p=p*a
    return p
############################################### (A/P,%i,n) FACTOR ###################################################
def APFACTOR (p,i,n):
    a=(i*((1+i)**n))/(((1+i)**n)-1)
    a=a*p
    return a
############################################### (A/F,%i,n) FACTOR ###################################################
def AFFACTOR (f,i,n):
    a=(((1+i)**n)-1)/i
    a=a*f
    return a
################################################### MAIN MENU #######################################################
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
        project=DEFINE(us)
        COMPUTE(project)
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
        
    