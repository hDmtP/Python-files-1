import winsound
n=18
no_of_gu=1

print("You have total 8 chances to guess the correct number\n")
print("Hint: its a +ve & two-digit number\n")
fr=3333
dr=1500
winsound.Beep(fr,dr)

while(no_of_gu<=9):
    u=int(input("Enter your guessed number here: "))
    if(u>18):
        print("Please enter a ***LESSER*** number than", u)
        fr=1333
        dr=1500
        winsound.Beep(fr,dr)

        
    elif(u<18):
        print("Please enter a ***GREATER*** number than", u)
        fr=5333
        dr=1500
        winsound.Beep(fr,dr)
        
    else:
        print("You won by",no_of_gu,"no. of choices") 
        fr=8333
        dr=3000
        winsound.Beep(fr,dr)
        break
    no_of_gu=no_of_gu+1      
while(no_of_gu>9):
    print("****Game Over****")
    fr=500
    dr=3000
    winsound.Beep(fr,dr)
    break

