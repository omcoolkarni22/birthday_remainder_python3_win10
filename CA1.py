from datetime import datetime
from win10toast import ToastNotifier

#save the file as with name birthday.txt to execute this program.And In the same folder where your .py file is saved...

n=ToastNotifier()
filename = open("birthday.txt",'r')
timestamp = 1528797322

def CheckBirthdayToday():
    
    Today = datetime.fromtimestamp(timestamp)
    d=Today.strftime("%d%m")
    

    for line in filename:
        if d in line:
            
                line=line.split(' ')
                n.show_toast("BirthDay Remainder",line[1]+line[2],duration=10)
            
        else:
                n.show_toast("Birthday Remainder","No Birthday Today",duration=10)

CheckBirthdayToday()








