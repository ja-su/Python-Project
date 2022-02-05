import datetime
import time  
import secrets 
import string 
import os
train1={'AC1':100,'AC2':200,'AC3':300,'SL':400}#t1
train1a={'AC1':100,'AC2':200,'AC3':300,'SL':400}
train1b={'AC1':100,'AC2':200,'AC3':300,'SL':400}
train2={'AC1':100,'AC2':200,'AC3':300,'SL':400}#t1
train2a={'AC1':100,'AC2':200,'AC3':300,'SL':400}
train2b={'AC1':100,'AC2':200,'AC3':300,'SL':400}
train3={'AC1':100,'AC2':200,'AC3':300,'SL':400}#t3
train3a={'AC1':100,'AC2':200,'AC3':300,'SL':400}
train3b={'AC1':100,'AC2':200,'AC3':300,'SL':400}
t1="Duronto Express"
t2="Maveli Express"
t3="Kochuveli Express"
booking={}
bookinga={}
bookingb={}
booking1={}
booking1a={}
booking1b={}
booking2={}
booking2a={}
booking2b={}
traveller={}
global book
book=0
global flag
flag=0
datefirst_Date= datetime.datetime.today() + datetime.timedelta(days=1)
datefirst_Date_Formatted =datefirst_Date.strftime ('%d/%m/%Y')
datefirst= str(datefirst_Date_Formatted)
datesecond_Date = datetime.datetime.today() + datetime.timedelta(days=2)
datesecond_Date_Formatted = datesecond_Date .strftime ('%d/%m/%Y')
datesecond=str(datesecond_Date_Formatted ) 
datethird_Date = datetime.datetime.today() + datetime.timedelta(days=3)
datethird_Date_Formatted = datethird_Date.strftime ('%d/%m/%Y') 
datethird=str(datethird_Date_Formatted)
global payment
payment=0
balanceamt={}
tvc= "Thiruvananthapuram Central Station" 
ers= "Ernakulam Junction South"
trvl="Tiruvalla Railway Station"
ksq="Kasaragod Railway Station"
srr="Shoranur Junction Railway Station"
tcr="Thrissur Railway Station"
clt="Korzhikode Railway Station"

def cls():
    os.system('cls||clear') 
def otp():
  N = 4
  otpp = ''.join(secrets.choice( string.digits) for i in range(N))
  file = open("Message.txt", "w")
  file.write("\n The One Time Password is:")
  file.write(str(otpp))
  file.close
  return str(otpp) 
def randomno():  
  N = 10
  ran = ''.join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(N)) 
  return str(ran)   
def destination(w,x,y,z):
  traveller={}
  cls()
  print("\t---------From -------")
  print("\n 1.",w,"\n 2.",x,"\n 3.",y)
  dep=int(input(" Enter your choice :"))
  if(dep==1):
      traveller['dep']=w
      print("\t--------To---------- ")
      print("\n 1.",x,"\n 2.",y,"\n 3.",z)
      arv=int(input(" Enter your choice : "))
      if(arv==1):
          traveller['arv']=x
          return traveller
      elif(arv==2):
          traveller['arv']=y
          return traveller
      elif(arv==3):
          traveller['arv']=z
          return traveller
      else:
         print("!!!Can't Handle!!!!")
         time.sleep(2)
                  
  elif(dep==2):
      traveller['dep']=x
      print("\t--------To---------- ")
      print("\n1.",y,"\n2.",z)
      arv=int(input("Enter your choice : "))
      if(arv==1):
          traveller['arv']=y
          return traveller
      elif(arv==2):
          traveller['arv']=z
          return traveller
      else:
         print("!!!Can't Handle!!!!")
         time.sleep(2)
  elif(dep==3):
       traveller['dep']=y
       print("\t--------To---------- ")
       print("Only to ",z,"booked")
       traveller['arv']=z
       time.sleep(2)
       return traveller
  else:
     print("!!!Can't Handle!!!!")
     time.sleep(2)
 
    
def ticketcan(pnr):
  try:
     s = open("%s.txt" % key).read()
     pnr=pnr+"\tStatus: confirmed"
     s = s.replace(pnr, '!!!No PNR as the Ticket has been Cancelled!!!\t Status:Cancelled')
     f = open("%s.txt" % key, 'w')
     f.write(s)
     f.close()
  except:
    print("!!!....Error.....!!!")
    time.sleep(1)
 
def ticket(x,y,z,w,t,u,v,r,s,q):
    
 file1=open("%s.txt" % key,"a" ) 
 file1.write("\n PNR no:")
 file1.write(str(q))
 file1.write("\tStatus: confirmed ")
 file1.write("\n Passenger Name: ")
 file1.write(str(x))
 file1.write("\n Passenger Age: ")
 file1.write(str(r))
 file1.write("\n Passenger Gender: ")
 file1.write(str(s))
 file1.write("\n Train name: ")
 file1.write(str(v))
 file1.write("\n Seat Number: ")
 file1.write(str(z))
 file1.write("\n Class is: ")
 file1.write(str(y))
 file1.write("\n Day is: ")
 file1.write(str(w))
 file1.write("\n Arrival is: ")
 file1.write(str(t))
 file1.write("\n Depature is: ") 
 file1.write(str(u))
 file1.write("\n")
 file1.close()


def reservationtraina(user):
        cls()
        x=int(input("Enter the number of passenger: "))
        for i in range(x):
          cls()
          name=input(" \n \t Enter the name :")
          age=int(input("\n \t Enter your Age: "))
          gender=str(input("\n \t Your Gender [Male/Female]: "))
          cls()
          print("\n \t ::::: AVAILABLE TRAIN COMPARTMENTS :::::")
          print(" \n \t AC1 for AC First Class, \n \t AC2 for AC 2-Tier \n \t AC3 for AC 3-Tier \n \t SL For  Sleeper ")
          clas=input(" \n \t Enter the choice :")
          cls()
          print("\n \t <<<<<Available Dates>>>>>>")
          print("\n \t Which day do you prefer....? \n \t 1.",datefirst," \n \t 2.",datesecond ," \n \t 3.",datethird)
          z=int(input(" \n \t Enter your choice : "))
          cls()
          if(z==1):
              mainreservation(user,name,age,gender,train1,booking,clas,datefirst,tvc,trvl,ers,tcr,t1)
          elif(z==2):
              mainreservation(user,name,age,gender,train1a,bookinga,clas,datesecond,tvc,trvl,ers,tcr,t1)
          elif(z==3):
              mainreservation(user,name,age,gender,train1b,bookingb,clas,datethird,tvc,trvl,ers,tcr,t1)
          else:
              print("\n \t Inaccurate") 
              time.sleep(2)


def reservationtrainb(user):
        cls()
        x=int(input("Enter the number of passanger"))

        for i in range(x):
          cls()  
          name=input(" \n \t Enter the name :")
          age=int(input("\n \t Enter your Age: "))
          gender=str(input("\n \t Your Gender [Male/Female]: "))
          cls()
          print("\n \t ::::: AVAILABLE TRAIN COMPARTMENTS :::::")
          print("\n \t AC1 for AC First Class,\n \t AC2 for AC 2-Tier \n \t AC3 for AC 3-Tier \n \t SL For  Sleeper ")
          clas=input(" \n \t Enter the choice :")
          cls()
          print("\n \t <<<<<Available Dates>>>>>>")
          print("\n \t  Which day do you prefer....? \n \t 1.",datefirst," \n \t 2.",datesecond ," \n \t 3.",datethird)
          time.sleep(2)
          z=int(input(" Enter the choice : "))
          cls()
          if(z==1):
              mainreservation(user,name,age,gender,train2,booking1,clas,datefirst,tcr,srr,clt,ksq,t2)
          elif(z==2):
              mainreservation(user,name,age,gender,train2a,booking1a,clas,datesecond,tcr,srr,clt,ksq,t2)
          elif(z==3):
              mainreservation(user,name,age,gender,train2b,booking1b,clas,datethird,tcr,srr,clt,ksq,t2)
          else:
            print(" \n \t Inaccurate") 
            time.sleep(2)


def reservationtrainc(user):
        cls()
        x=int(input("Enter the number of passanger"))

        for i in range(x):
          cls()  
          name=input(" \n \t Enter the name: ")
          age=int(input("\n \t Enter your Age: "))
          gender=str(input("\n \t Your Gender [Male/Female]: "))
          cls()
          print("\n \t ::::: AVAILABLE TRAIN COMPARTMENTS :::::")
          print(" \n \t AC1 for AC First Class, \n \t AC2 for AC 2-Tier \n \t AC3 for AC 3-Tier \n \t SL For  Sleeper ")
          clas=input(" \n \t Enter the choice : ")
          cls()
          print("\n \t <<<<<Available Dates>>>>>>")
          print("\n \t Which day do you prefer....? \n \t 1.",datefirst," \n \t 2.",datesecond ," \n \t 3.",datethird)
          z=int(input(" \n \t Enter your choice : "))
          if(z==1):
              mainreservation(user,name,age,gender,train3,booking2,clas,datefirst,ksq,srr,ers,tvc,t3) 
          elif(z==2):
              mainreservation(user,name,age,gender,train3a,booking2a,clas,datesecond,ksq,srr,ers,tvc,t3)
          elif(z==3):
              mainreservation(user,name,age,gender,train3b,booking2b,clas,datethird,ksq,srr,ers,tvc,t3)
          else:
              print("\n \t Inaccurate") 
              time.sleep(2)
def mainreservation(user,name,age,gender,x,bookingx,clas,z,a,b,c,d,tname):
        global book
        cls()
        if(clas=='AC1'):
                     if(x['AC1']>=1):             
                                   traveller=destination(a,b,c,d)
                                   transaction(2000,user)
                                   book=1
                                   if(payment==1):
                                               n=x['AC1']
                                               x['AC1']-=1
                                               seat=n
                                               pnr=randomno()
                                               bookingx[pnr]=user
                                               cls()
                                               print("\n \t Booking........",)
                                               time.sleep(1)
                                               cls()
                                               print("\n \t BOOKING COMPLETED")
                                               time.sleep(1)
                                               cls()
                                               print("\n \t Allocating seat...")
                                               time.sleep(1) 
                                               cls()
                                               print(" \n \t PNR No: ",pnr)
                                               print(" \t Passenger name: ",name,"\n \t Seat no: ",str(seat),"\n \t Class is: AC FIRST Class\n \t Day is: ",str(z))
                                               ticket(name,'AC first class',str(seat),z,traveller['arv'],traveller['dep'],tname,age,gender,pnr)
                                               print("\n \t BOOKING COMPLETED THANK YOU :))")
                                               print("\n \t ** Wait for a while **")
                                               time.sleep(3)
                                   elif(payment==0):
                                               print("\n \t !!!!Transaction Failed !!!!")
                                               time.sleep(2)             
                     elif(x['AC1']< 1):
                           print("\n \t No seat is available for the current class on preferred day!!!")
                           time.sleep(3)

    #second class
        elif(clas=='AC2'):
                      cls()
                      if(x['AC2']>=1):
                                 traveller=destination(a,b,c,d)
                                 transaction(1500,user)
                                 book=1
                                 if(payment==1):
                                               n=x['AC2']
                                               x['AC2']-=1
                                               seat=n
                                               pnr=randomno()
                                               bookingx[pnr]=user
                                               cls()
                                               print("\n \t Booking........",)
                                               time.sleep(1)
                                               cls()
                                               print("\n \t BOOKING COMPLETED")
                                               time.sleep(1)
                                               cls()
                                               print("\n \t Allocating seat...")
                                               time.sleep(1)
                                               cls()
                                               print("\n \t PNR No: ",pnr)
                                               print("\t Passenger name: ",name,"\n \t Seat no: ",str(seat),"\n \t Class is: AC Second Class \n \t Day is: ",str(z))
                                               ticket(name,'AC Second Class',str(seat),z,traveller['arv'],traveller['dep'],tname,age,gender,pnr)
                                               print("\n \t BOOKING COMPLETED THANK YOU :))")
                                               print("\n \t ** Wait for a while **")
                                               time.sleep(3)
                                 elif(payment==0):
                                              print("\n \t !!!!Transaction Failed !!!!")  
                                              time.sleep(2)          
                      elif(x['AC3']< 1):
                                 print("\n \t No seat is available for the current class on preferred day")
                                 time.sleep(3) 
             
        #THIRD AC
        elif(clas=='AC3'):
                      cls()        
                      if(x['AC3']>=1):
                                traveller=destination(a,b,c,d)
                                transaction(1000,user)
                                book=1
                                if(payment==1):
                                            n=x['AC3']
                                            x['AC3']-=1
                                            seat=n
                                            pnr=randomno()
                                            bookingx[pnr]=user
                                            cls()
                                            print("\n \t Booking........",)
                                            time.sleep(1)
                                            cls()
                                            print("\n \t BOOKING COMPLETED")
                                            time.sleep(1)
                                            cls()
                                            print("\n \t Allocating seat...")
                                            time.sleep(1) 
                                            cls()
                                            print("\n \t PNR No: ",pnr)
                                            print("\t Passenger name: ",name,"\n \t Seat no: ",str(seat),"\n \t Class is: AC Third Class \n \t Day is: ",str(z)) 
                                            ticket(name,'AC Third Class',str(seat),z,traveller['arv'],traveller['dep'],tname,age,gender,pnr)
                                            print(" \n \t BOOKING COMPLETED THANK YOU :)) ")
                                            print("\n \t ** Wait for a while **")
                                            time.sleep(3)
                                elif(payment==0):
                                            print("\n \t !!!!Transaction Failed !!!!")
                                            time.sleep(2) 
                      elif(x['AC3']< 1):
                                print("\n \tNo seat is available for the current class on preferred day")
                                time.sleep(3) 
        #sleeper
                                    
        elif(clas=="SL"):
                      cls()                             
                      if(x['SL']>=1):
                                traveller=destination(a,b,c,d)
                                transaction(250,user)
                                book=1
                                if(payment==1):
                                             n=x['SL']
                                             x['SL']-=1
                                             pnr=randomno()
                                             seat=n
                                             bookingx[pnr]=user
                                             cls()
                                             print("\n \t Booking........",)
                                             time.sleep(1)
                                             cls()
                                             print("\n \t BOOKING COMPLETED")
                                             time.sleep(1)
                                             cls()
                                             print("\n \t Allocating seat...")
                                             time.sleep(1) 
                                             cls()
                                             print("\n \t PNR No: ",pnr)                
                                             ticket(name,'Sleeper Class',str(seat),z,traveller['arv'],traveller['dep'],tname,age,gender,pnr)
                                             print("\t Passenger name: ",name,"\n \t Seat no: ",str(seat),"\n \t Class is: Sleeper Class\n \t Day is: ",str(z))
                                             print(" \n \tBOOKING COMPLETED THANK YOU :)) ")
                                             print("\n \t** Wait for a while **")
                                             time.sleep(3)
                
                               
                                elif(payment==0):
                                         print("\n \t !!!!Transaction Failed !!!!")
                                         time.sleep(2) 
                
                      elif(x['SL']< 1):
                                print("\n \t No seat is available for the current class on preferred day")
                                time.sleep(3) 
        else:
          print("Invalid")
          time.sleep(2) 

def traina(user):
    cls()
    print("\n \t !!!Welcome to ",t1,"train portal!!!")
    print("\n \t 1. For Reservation \n \t 2. For Cancellation ")
    y=int(input(" \n \t Enter your choice: "))
    if(y==1):
        reservationtraina(user)
    elif(y==2):
        canceltrain(user,train1,train1a,train1b,booking,bookinga,bookingb)
    else:
        print(" \n \tInvalid entry") 
        time.sleep(2)
def trainb(user):
    cls()
    print("\n \t !!!Welcome to ",t2,"train portal!!!")
    print("\n \t 1. For Reservation \n \t 2. For Cancellation ")
    y=int(input(" \n \t Enter your choice: "))
    if(y==1):
        reservationtrainb(user)
    elif(y==2):
        canceltrain(user,train2,train2a,train2b,booking1,booking1a,booking1b)
    else:
        print("Invalid entry") 
        time.sleep(2)
def trainc(user):
    cls()
    print("\n \t !!!Welcome to ",t3,"train portal!!!")
    print("\n \t 1. For Reservation \n \t 2. For Cancellation")
    y=int(input("\n \tEnter your choice: "))
    if(y==1):
        reservationtrainc(user)
    elif(y==2):
        canceltrain(user,train3,train3a,train3b,booking2,booking2a,booking2b)
    else:
        print(" \n \t Invalid entry") 
        time.sleep(2)


def canceltrain(user,x,w,t,y,y1,y2):
    cls()
    print("!!!! CANCELLATION MENU !!!!")
    print("\n \t Which day do you prefer....? \n \t 1.",datefirst," \n \t 2.",datesecond ," \n \t 3.",datethird)
    z=int(input(" \n \tEnter your option: "))
    cls()
    time.sleep(1)
    print("\n \t ::::: AVAILABLE TRAIN COMPARTMENTS :::::")
    print("\n \t AC1 for AC First Class,\n \t AC2 for AC 2-Tier\n \t AC3 for  AC 3-Tier \n \t SL For  Sleeper ")
    time.sleep(1)
    clas=str(input(" \n \tEnter your option: "))
   
    if(z==1):
       if(clas=='AC1'):
        cancel_train(user,y,x,'AC1')
       elif(clas=='AC2'):
        cancel_train(user,y,x,'AC2')
       elif(clas=='AC3' ):
        cancel_train(user,y,x,'AC3')
       elif(clas=='SL'):
        cancel_train(user,y,x,'SL')
       else:
         print("\n \t Invalid class")
         time.sleep(2)
    elif(z==2):
      if(clas=='AC1'):
        cancel_train(user,y1,w,'AC1')
      elif(clas=='AC2' ):
        cancel_train(user,y1,w,'AC2')
      elif(clas=='AC3'):
        cancel_train(user,y1,w,'AC3')
      elif(clas=='SL'):
        cancel_train(user,y1,w,'SL')
      else:
          print("\n \t Invalid class")
          time.sleep(2)
    elif(z==3):
       if(clas=='AC1'):
        cancel_train(user,y2,t,'AC1')
       elif(clas=='AC2'):
        cancel_train(user,y2,t,'AC2')
       elif(clas=='AC3' ):
        cancel_train(user,y2,t,'AC3')
       elif(clas=='SL'):
        cancel_train(user,y2,t,'SL')
       else:
         print("\n \t Invalid class!!!")
         time.sleep(2)
       
    else:
        print("\n \t Invalid Date!!!")
        time.sleep(2)


def cancel_train(user,bookingx,x,y): 
    cls()
    print("\n \t //// CANCELLATION TICKET ////")
    pnr=input("\n \t Enter the PNR Code : ")
    try:
         if(str(bookingx[str(pnr)])==user):
            del bookingx[pnr]
            x[y]+=1
            newbalance=0
            global flag
            if(y=='AC1'):
                        flag=1
                        transaction(800,user)
                        newbalance=balanceamt[user]+800
                        print(" \n \t New balance:",newbalance,"Amount as been transfered to your bank accout") 
                        time.sleep(3)
            if(y=='AC2'):
                        flag+=1
                        transaction(400,user)
                        newbalance=balanceamt[user]+400
                        print("\n \t New balance:",newbalance,"Amount as been transfered to your bank accout") 
                        time.sleep(3)
            if(y=='AC3'):
                        flag=1
                        transaction(200,user)
                        newbalance=balanceamt[user]+200
                        print("\n \t New balance:",newbalance,"Amount as been transfered to your bank accout") 
                        time.sleep(3)
            if(y=='SL'):
                        flag=1
                        transaction(50,user)
                        newbalance=balanceamt[user]+50
                        print("\n \t New balance:",newbalance,"Amount as been transfered to your bank accout") 
                        time.sleep(3)
            print("\n \t Cancellation on process....")
            ticketcan(pnr)
            time.sleep(2) 
            cls()
            print(" \n \t Cancellation successfull")
            print("\n \t ** Wait for a while **")
            time.sleep(3)
            flag=0
         else:
            print("\n \t Invalid Entry!!!") 
            time.sleep(2)
          
    except KeyError: 
          print("\n \t Cancellation is Not Possible!!!")
          time.sleep(2)


def transaction(amt,user):
    try:
        class account():
            def _init_(self):
                self.balance=balanceamt[user]
            def deposit(self):
                amt=float(input("\n \t Enter a amount to deposit: "))
                trial=3
                pin=(int(otp()))
                while(1):
                 print(" \n \t Welcome ",user,"; HDBCI Indian bank Accno:-****")
                 print(" \n \t One Time Password has been message to your Register Mobile Number 9xxxxxxxx")
                 x=int(input("\n \t Enter the OTP: "))
                 if(x==pin and trial > 0):
                   self.balance+=amt
                   balanceamt[user]=self.balance
                   print(" \n \t New balance is",self.balance)
                   time.sleep(2)
                   break
                 elif(x!=pin and trial > 0):
                   print(" \n \t Incorrect PIN you have ",trial ,"more tries")
                   trial-=1
                 else:
                   print(" \n \t Sorry Try Again")
                   time.sleep(2)
                   break
            def withdraw(self):
                 
                 print("\n \t Cost of one ticket is: ",amt)
                 
                 if(self.balance<=amt):
                     print("\n \t Insufficient recharge Rail pay!!! ")
                     time.sleep(2)
                     transaction(amt,user)
                     
                 else:
                     self.balance-=amt
                     global payment
                     payment=1
                     time.sleep(2)
                     balanceamt[user]=self.balance
                     print(" \n \t New balance is: ",self.balance)
                     time.sleep(2)
                     
            def returning(self):
                  print("\n \t Hello ",user,"the amount refunded is: ",amt)
                  print("\n \t Rest of the amount as been taken as our refunding policy")
                  self.balance+=amt
        a=account()
        global flag
        if(flag==1):
          a.returning()
        else:
         while(1):
             cls()
             print("\n \t Transaction only rail pay is allowed")
             print("\n \t 1.Recharge Rail pay \n \t 2.Pay through Rail pay \n \t 3.Abort the payment")
             x=int(input("\n \t Enter a choice: "))
             if(x==1):
                      a.deposit()
             elif(x==2):
                      a.withdraw()
                      
                      break
                           
             elif(x==3):
                      global payment
                      payment=0
                      break
             else:
                      print("\n \t !!! Invalid entry !!!!")
                      time.sleep(2)
    except KeyError:
        print("updating please Wait..")
        time.sleep(2)
        file1=open("user.txt","w")
        file1.close()
        balanceamt[user]=0
        transaction(amt,user)
def update(user):
    try:
        class account():
                def _init_(self):
                    self.balance=balanceamt[user]
                def deposit(self):
                    amt=int(input("\n \t Enter a amount to deposit: "))
                    trial=3
                    pin=(int(otp()))
                    while(1):
                        print(" \n \t Welcome ",user,"; HDBCI Indian bank Accno:-****")
                        print(" \n \t One Time Password has been message to your Register Mobile Number 9xxxxxxxx")
                        x=int(input("\n \t Enter the OTP: "))
                        if(x==pin and trial > 0):
                          self.balance+=amt
                          balanceamt[user]+=amt
                          print(" \n \t New balance is",self.balance)
                          time.sleep(2)
                          break
                        elif(x!=pin and trial > 0):
                          print(" \n \t Incorrect PIN you have ",trial ,"more tries")
                          trial-=1
                        else:
                           print(" \n \t Sorry Try Again")
                           time.sleep(2)
        a=account()
        a.deposit()
    except KeyError:
        cls()
        print("Updating please try again")
        balanceamt[user]=0
        file1=open("user.txt","w")
        file1.close()
        time.sleep(1)
        cls()
    
def display(user):
    cls()
    print("\n \t\t\t---WELCOME-TO-RESERVATION-SYSTEM--- ")
    print("\n    You can only book ticket for 3 days in advance")
    time.sleep(2)
    print("\n \t 1.",t1,"\n \t 2.",t2," \n \t 3.",t3,"\n \t 4. Exit the portal")
    x=int(input("\n \t Enter your choice : "))
    if(x==1):
        traina(user)
    elif(x==2):
        trainb(user)
    elif(x==3):
        trainc(user)
    elif(x==4):
        print("\n \t !!!!!!Have a nice day from our team!!!!!! ")
        time.sleep(2)
        cls() 
   
    else:
        print(" \n \t Invalid entry")
        time.sleep(2)

def showtickets(user):
    cls()
    if(book==1):
        file3=open("%s.txt" % user,"r")
        cuff=file3.read()
        print(cuff)
        input("\n PRESS ENTER TO EXIT!!!")
        cls()
    else:
      print("\n NO Tickets Booked !!!")
      time.sleep(2)
      cls()   


def register():
    cls()
    key=input("Enter username: ")
    val=input("Enter password: ") 
    file1 = open("users.txt","r")
    verify = file1.read()
    if (key + " " + ":" + val) in verify:
        print("User exists!")
        time.sleep(1)
    elif (key) in verify:
        print("User exists!")
        time.sleep(1)
    else:
        file1.close()
        file1 = open("users.txt","a")
        file1.write(key + " " + ":" + val + "\n")
        print("Registration successful")
        balanceamt[key]=0
        time.sleep(1)
        file1.close()

def homepage(user):
    cls()
    print("\n \t \t Hi!! ",user," we welcome you to Portal \t")
    while(1):

         print("\n \t 1.Train Related To Booking or Cancellation \n \t 2.Your Booking \n \t 3.Recharge your Railpay \n \t 4.Log Out")
         opt=int(input("\tEnter your choice: "))
         if (opt==1):
             display(user)
         elif(opt==2):
             showtickets(user)
         elif(opt==3):
             update(user)
         else:
             print(user,"is logging out!!!")
             break
def login():
    cls()
    global key
    key=input("Enter username: ")
    val=input("Enter password: ")
    file2 = open("users.txt", "r")
    verify = file2.read()
    if (key + " " + ":" + val) in verify:
        print("Login Success")
        time.sleep(1)
        homepage(key)
    elif (key) in verify:
        print("Password not recognised")
        time.sleep(1)
    else:
        print("User not found")
        time.sleep(1) 
    file2.close()
while(1): 
    cls()
    print("\n\t\t\t\t\t TRAIN RUNNING STATUS")
    print('\n   Train Name',"\t\t  Date",'\t\t  AC1', '\t  AC2', '\t  AC3','\t   SL',"\t\tStation details")
    print("\n",t1,"\t",datefirst,"\t ", train1['AC1'],"\t ",train1['AC2'],"\t ",train1['AC3'],"\t ",train1['SL'],"\t\tTVC TRVL ERS TCR")
    print("\n",t2,"\t",datefirst,"\t ", train2['AC1'],"\t ",train2['AC2'],"\t ",train2['AC3'],"\t ",train2['SL'],"\t\tTCR SRR CLT KSQ")
    print("\n",t3,"\t",datefirst,"\t ", train3['AC1'],"\t ",train3['AC2'],"\t ",train3['AC3'],"\t ",train3['SL'],"\t\tKSQ SRR ERS TVC")
    print("\n")
    print("\n",t1,"\t",datesecond,"\t", train1a['AC1'],"\t ",train1a['AC2'],"\t ",train1a['AC3'],"\t ",train1a['SL'],"\t\tTVC TRVL ERS TCR")
    print("\n",t2,"\t",datesecond,"\t", train2a['AC1'],"\t ",train2a['AC2'],"\t ",train2a['AC3'],"\t ",train2a['SL'],"\t\tTCR SRR CLT KSQ")
    print("\n",t3,"\t",datesecond,"\t", train3a['AC1'],"\t ",train3a['AC2'],"\t ",train3a['AC3'],"\t ",train3a['SL'],"\t\tKSQ SRR ERS TVC")
    print("\n")
    print("\n",t1,"\t",datethird,"\t ", train1b['AC1'],"\t",train1b['AC2'],"\t ",train1b['AC3'],"\t ",train1b['SL'],"\t\tTVC TRVL ERS TCR")
    print("\n",t2,"\t",datethird,"\t ", train2b['AC1'],"\t",train2b['AC2'],"\t ",train2b['AC3'],"\t ",train2b['SL'],"\t\tTCR SRR CLT KSQ")
    print("\n",t3,"\t",datethird,"\t ", train3b['AC1'],"\t",train3b['AC2'],"\t ",train3b['AC3'],"\t ",train3b['SL'],"\t\tKSQ SRR ERS TVC")
    input("\n ENTER TO CONTINUE")
    cls()
    print("\n1.Create a user")
    print("2.Login")
    print("3.Show Tickets")
    print("4.Exit")
    ch=int(input("Enter your choice: "))
    cls()
    if(ch==1):
        register()
    elif(ch==2):
        login()
    elif(ch==3):
        user=input("Enter your username:")
        showtickets(user)
    elif(ch==4):
        break 
    else:
        print("invalid entry")
