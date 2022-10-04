n = input("Enter String ")
s = int(input("Enter shift "))
x = int(input("enter 1 for encryption,0 for decryption "))
l = len(n)
if(x == 1):
    for i in n:
        if(i.isupper()):
            val = ord(i) + s
            if(val>ord('Z')):
                val = val-26
            print(chr(val),end="")
        else:
            val = ord(i)+s
            if(val>ord('z')):
                val = val-26
            print(chr(val),end="")
elif(x == 0):
    for i in n:
        if(i.isupper()):
            val = ord(i)-s
            if(val>ord('Z')):
                val = val-26
            print(chr(val),end="")
        else:
            val = ord(i)-s
            if(val>ord('z')):
                val = val-26
            print(chr(val),end="")
else:
    print("INVALID CHOICE")
