#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT  OF  ECONOMY                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/07/14                                                   #
#                                                                                                                   #
#                                                                                                                   #
#################################################### MODULES ########################################################
import sys,time,os,random
from sympy import symbols,solve
################################################# CLEAR SCREEN ######################################################
def cls():
    os.system(['clear','cls'][os.name=='nt'])
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
############################################### (F/P,%i,n) FACTOR ###################################################
def FPFACTOR (p,i,n):
    f=p*((1+i)^n)
    return f
############################################### (F/A,%i,n) FACTOR ###################################################
def FAFACTOR (a,i,n):
    f=a*(i)/(((1+i)^n)-1)
    return f
############################################### (P/G,%i,n) FACTOR ###################################################
def PGFACTOR (g,i,n):
    p=(g/i)*(((((1+i)^n)-1)/(i*((1+i)^n)))-(n/((1+i)^n)))
    return p
############################################### (A/G,%i,n) FACTOR ###################################################
def AGFACTOR (g,i,n):
    a=g*((1/i)-(n/((1+i)^n)-1))
    return a
############################################### (G/P,%i,n) FACTOR ###################################################
def GPFACTOR (p,i,n):
    g=(i*p)/(((((1+i)^n)-1)/(i*((1+i)^n)))-(n/((1+i)^n)))
    return g
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
            project[counter][1]=int(input("\t\t\t| ENTER THE VALUE OF SCRAPPING:"))    
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
            # r=int(input("\t\t\t| ENTER INTEREST RATE(in persent):"))
            # if r<=0 or r>=100:
            #     r=int("typeerror")
            # print("\t\t\t|______________________________________|")
            # print("\t\t\t|    CHOOSE PRIOD OF INTEREST RATE:    |")
            # print("\t\t\t| 1) ANNUAL                            |")
            # print("\t\t\t| 2) SEMIANNUAL                        |")
            # print("\t\t\t| 4) TRIMESTER                         |")
            # print("\t\t\t| 12) MOUNTLY                          |")
            # t=input("\t\t\t|______________________________________|")
            # if int(t)==1 or int(t)==2 or int(t)==4 or int(t)==12 :
            #     r=r/100
            #     project[counter][5]=((1+r)**int(t))-1
            # else:
            #     project[counter][4]=int('typeerror')
            project[counter][6]=int(input("\t\t\t| ENTER ANNUAL PAYMENT:"))
            project[counter][7]=int(input("\t\t\t| ENTER ANNUAL INCOME:"))    
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
################################################## COMPUTE FCN ######################################################
def COMPUTE(project):
    while True:
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|       CHOOSE METHOD BY NUMBER:       |")
        print("\t\t\t|   1) NPW                             |")
        print("\t\t\t|   2) NEUA                            |")
        print("\t\t\t|   3) ROR                             |")
        print("\t\t\t|   4) B/C                             |")
        print("\t\t\t|   5) IGNORE!                         |")
        selector=input("\t\t\t|______________________________________|\n")
        tot=[0]
        for counter in range(len(project)-1):
            tot.append(0)
        if selector=='1':
            for counter in range(len(project)):
                D=(project[counter][0]-project[counter][1])/project[counter][4]
                for year in range(project[counter][4]):
                    if year==0:
                        tot[counter]=-project[counter][0]
                        tot[counter]=APFACTOR(tot[counter],project[counter][2],project[counter][4])
                        #year=project[counter][4]-2
                    elif year==project[counter][4]:
                        CFAT=AFFACTOR(project[counter][1],project[counter][2],project[counter][4])
                        tot[counter]=tot[counter]+CFAT
                    elif year==project[counter][4]-1:
                        CFAT=((project[counter][7]-project[counter][6])-D)
                        TX=project[counter][3]*CFAT
                        if CFAT>0:
                            CFAT=CFAT-TX
                        tot[counter]=tot[counter]+CFAT
            wait()
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t|       NPW OF EACH PROJECT IS :       |")
            for counter in range(len(tot)):
                tot[counter]=PAFACTOR(tot[counter],project[counter][2],project[counter][4])    
                print("\t\t\t|   {}) NPW = {}".format(counter+1,tot[counter]))
            final=max(tot)
            print("\t\t\t|______________________________________|")
            print('\t\t\t|  THE MOST ECONOMICAL PROJECT IS: {}  |'.format(tot.index(final)+1))
            print('\t\t\t|     perss any key to continue...     |')
            input("\t\t\t|______________________________________|")
        elif selector=='2':
            for counter in range(len(project)):
                D=(project[counter][0]-project[counter][1])/project[counter][4]
                for year in range(project[counter][4]):
                    if year==0:
                        tot[counter]=-project[counter][0]
                        tot[counter]=APFACTOR(tot[counter],project[counter][2],project[counter][4])
                        #year=project[counter][4]-2
                    elif year==project[counter][4]:
                        CFAT=AFFACTOR(project[counter][1],project[counter][2],project[counter][4])
                        tot[counter]=tot[counter]+CFAT
                    elif year==project[counter][4]-1:
                        CFAT=((project[counter][7]-project[counter][6])-D)
                        TX=project[counter][3]*CFAT
                        if CFAT>0:
                            CFAT=CFAT-TX
                        tot[counter]=tot[counter]+CFAT
            wait()
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t|       NPW OF EACH PROJECT IS :       |")
            for counter in range(len(tot)):
                tot[counter]=PAFACTOR(tot[counter],project[counter][2],project[counter][4])    
                print("\t\t\t|   {}) NPW = {}".format(counter+1,tot[counter]))
            final=max(tot)
            print("\t\t\t|______________________________________|")
            print('\t\t\t|  THE MOST ECONOMICAL PROJECT IS: {}  |'.format(tot.index(final)+1))
            print('\t\t\t|     perss any key to continue...     |')
            input("\t\t\t|______________________________________|")
        elif selector=='3':
            wait()
            cls()
            print("\t\t\t ______________________________________")   
            print("\t\t\t|        ROR for each project :        |") 
            for counter in range(len(project)):
                D=(project[counter][0]-project[counter][1])/project[counter][4]
                for year in range(project[counter][4]):
                    if year==0:
                        tot[counter]=-project[counter][0]
                        #tot[counter]=APFACTOR(tot[counter],project[counter][2],project[counter][4])
                        ROR=symbols('ROR')
                        equation=(ROR*((1+ROR)**project[counter][4]))/(((1+ROR)**project[counter][4])-1)
                        tot[counter]=equation*tot[counter]
                        #year=project[counter][4]-2
                    elif year==project[counter][4]:
                        #CFAT=AFFACTOR(project[counter][1],project[counter][2],project[counter][4])
                        ROR=symbols('ROR')
                        equation=(((1+ROR)**project[counter][4])-1)/ROR
                        equation=equation*project[counter][1]
                        tot[counter]=tot[counter]+equation
                        project[counter][5]=solve(tot[counter])
                        print("\t\t\t|   {})ROR={}                          |".format(counter+1,project[counter][5]))
                    elif year==project[counter][4]-1:
                        CFAT=((project[counter][7]-project[counter][6])-D)
                        TX=project[counter][3]*CFAT
                        if CFAT>0:
                            CFAT=CFAT-TX
                        tot[counter]=tot[counter]+CFAT
            print("\t\t\t|______________________________________|")
            print("\t\t\t|     press any key to continue...     |")   
            print("\t\t\t|______________________________________|")
            # wait()
            # for counter1 in range(len(project)):
            #     for counter2 in range(len(project)-1):
            #         if project[counter2][0] > project[counter2 +1 ][0]:
            #             project.insert(counter2,project[counter2 +1])
            #             del project[counter2 +2]
            # for counter in range(len(project)):
            #     if project[counter][5] >= project[counter][2]:
            #         if project[counter+1][5] >= project[counter][2] and counter+1 <= len(project) :
            #             CFAT=project[counter+1][0]-project[counter][0]
            #             equation=project[counter+1][1]-project[counter][1]
            #             D=(project[counter][0]-project[counter][1])/project[counter][4]
            #             D1=((project[counter][7]-project[counter][6])-D)
            #             TX=project[counter][3]*D1
            #             if D1>0:
            #                 D1=D1-TX
            #             D=(project[counter+1][0]-project[counter+1][1])/project[counter+1][4]
            #             D2=((project[counter+1][7]-project[counter+][6])-D)
            #             TX=project[counter+1][3]*D2
            #             if D2>0:
            #                 D2=D2-TX
            #             D=D2-D1
            #             ROR=symbols('ROR')
            #             equation=(ROR*((1+ROR)**project[counter][4]))/(((1+ROR)**project[counter][4])-1)
            #             tot[counter]=equation*tot[counter]
            #             equation=(((1+ROR)**project[counter][4])-1)/ROR
            #             equation=equation*project[counter][1]
            #             project[counter][5]=solve(tot[counter])
            #         else:

            #     else:               
        elif selector=='4':
            break
        elif selector=='5':
            break
################################################### MAIN MENU #######################################################
while True:
    cls()
    print("\t\t\t ______________________________________")
    print("\t\t\t|             WELCOME USER!            |")
    print("\t\t\t|      PLEASE  SELECT BY NUMBER:       |")
    print("\t\t\t|   1) DEFINE NEW SITUATION            |")
    print("\t\t\t|   2) USING FACTORS                   |")
    print("\t\t\t|   3) ABOUT US!                       |")
    print("\t\t\t|   4) EXIT!                           |")
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
        print("\t\t\t ______________________________________")
        print("\t\t\t|               WHICH ONE?             |")
        print("\t\t\t|      PLEASE  SELECT BY NUMBER:       |")
        print("\t\t\t|   1) P/F          6) F/A             |")
        print("\t\t\t|   2) P/A          7) A/P             |")
        print("\t\t\t|   3) P/G          8) A/F             |")
        print("\t\t\t|   4) F/P          9) A/G             |")
        print("\t\t\t|   5) G/P         10) BACK            |")
        print("\t\t\t|______________________________________|")
        inselector=input()
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|        PLEASE  ENTER NUMBERS:        |")
        try:
            lifetime=int(input("\t\t\t|   ENTER LIFETIME: "))
            interest=int(input("\t\t\t|   ENTER INTEREST RATE (in persent): "))
            if interest<=0 or interest>=100:
                interest=int("typeerror")
            else :
                interest=interest/100
            factor=int(input("\t\t\t|   ENTER FATOR: "))
            print("\t\t\t|______________________________________|")
        except ValueError or TypeError:
            print("\t\t\t|______________________________________|")
            print('\n\n\t\t\t\t   please enter correctly!')
            time.sleep(1)
        if inselector=='1':
            wait()
            factor=PFFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='2':
            wait()
            factor=PAFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='3':
            wait()
            factor=PGFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='4':
            wait()
            factor=FPFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='5':
            wait()
            factor=GPFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='6':
            wait()
            factor=FAFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='7':
            wait()
            factor=APFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='8':
            wait()
            factor=AFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
        elif inselector=='9':
            wait()
            factor=AGFACTOR(factor,interest,lifetime)
            cls()
            print("\t\t\t ______________________________________")
            print("\t\t\t| THE RESULT IS: {}".format(factor))
            print("\t\t\t|______________________________________|")
            input()
    elif selector=='3' :
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
    elif selector=='4' :
        cls()
        exit=input("\n\n\t\t\tARE YOU SURE?(YES or NO)\n")
        if exit.upper()=="YES" or exit.upper()=='Y' :
            sys.exit(0)
        elif exit.upper()=="NO" or exit.upper()=='N' :
            pass
        
    