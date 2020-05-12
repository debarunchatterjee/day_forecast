from datetime import date
today=date.today()
today=today.strftime("%Y%m%d")
today=int(today)


print("\nPlease enter the date in DD-MM-YYYY format")
inputDay=input("Enter the day: ")
inputMonth=input("Enter the month: ")
inputYear=input("Enter the year: ")


dateList=[inputDay,inputMonth,inputYear]
dateString=".".join(dateList)
dateCheck=[inputYear,inputMonth,inputDay]
dateCheck="".join(dateCheck)
dateCheck=int(dateCheck)


if(dateCheck>today):
    tenseString="will be"
elif(dateCheck<today):
    tenseString="was"
else:
    tenseString="is"


inputDay=int(inputDay)
inputMonth=int(inputMonth)
inputYear=int(inputYear)


if((inputYear%400==0) or (inputYear%100!=0 and inputYear%4==0)):
    leapCheck=True
else:
    leapCheck=False


yearOddDay=0
extraYear=inputYear%400
if(extraYear==0):
    yearOddDay=0
elif(extraYear>=100 and extraYear<200):
    yearOddDay+=5
elif(extraYear>=200 and extraYear<300):
    yearOddDay+=3
elif(extraYear>=300):
    yearOddDay+=1

#Say, if the given doubleYear is '29 then the number of leap or non-leap
#years will be counted till '28 because the '29th year is running 
doubleExtraYear=(extraYear%100)-1
for i in range(1,doubleExtraYear+1):
    if((i%4==0 and i%100==0) or (i%100!=0 and i%4==0)):
        yearOddDay+=2
    else:
        yearOddDay+=1       

      
if(inputMonth==1):
    monthOddDay=inputDay
elif(inputMonth==2):
    monthOddDay=inputDay+31
elif(inputMonth==3):
    monthOddDay=inputDay+31+28
elif(inputMonth==4):
    monthOddDay=inputDay+31+28+31
elif(inputMonth==5):
    monthOddDay=inputDay+31+28+31+30
elif(inputMonth==6):
    monthOddDay=inputDay+31+28+31+30+31
elif(inputMonth==7):
    monthOddDay=inputDay+31+28+31+30+31+30
elif(inputMonth==8):
    monthOddDay=inputDay+31+28+31+30+31+30+31
elif(inputMonth==9):
    monthOddDay=inputDay+31+28+31+30+31+30+31+31
elif(inputMonth==10):
    monthOddDay=inputDay+31+28+31+30+31+30+31+31+30
elif(inputMonth==11):
    monthOddDay=inputDay+31+28+31+30+31+30+31+31+30+31
elif(inputMonth==12):
    monthOddDay=inputDay+31+28+31+30+31+30+31+31+30+31+30
     
#For a leap year there'll be an extra day for any day after
#29th Feb, i.e any date from March 1
if((leapCheck==True) and (inputMonth>=3)):
    monthOddDay+=1

    
totalOddDay=yearOddDay+monthOddDay
totalOddDay=totalOddDay%7


if totalOddDay==0:
    print("\n"+dateString+" "+tenseString+" a Sunday")
elif totalOddDay==1:
    print("\n"+dateString+" "+tenseString+" a Monday")
elif totalOddDay==2:
    print("\n"+dateString+" "+tenseString+" a Tuesday")
elif totalOddDay==3:
    print("\n"+dateString+" "+tenseString+" a Wednesday")
elif totalOddDay==4:
    print("\n"+dateString+" "+tenseString+" a Thursday")
elif totalOddDay==5:
    print("\n"+dateString+" "+tenseString+" a Friday")
elif totalOddDay==6:
    print("\n"+dateString+" "+tenseString+" a Saturday")