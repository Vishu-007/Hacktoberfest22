a = input("Enter The Password : ")
l, c, n, s = 0,0,0,0
x = len(a)
for i in a:
    if(i.islower()):
        l+=1
    elif(i.isalpha()):
        c+=1
    elif(i.isdigit()):
        n+=1
    elif(i == "$" or i =="#" or i == "@"):
        s+=1
if((l>=1 and c>=1 and n>=1 and s>=1) and x>=6):
    print("Valid")
else:
    print("Not Valid")
