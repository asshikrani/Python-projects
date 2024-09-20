emil = input("Enter your email:")#g@g.in
k,j,d = 0,0,0
if len(emil) >=6:
    if emil[0].isalpha():
            if ("@" in emil) and (emil.count("@") == 1):
                if (emil[-4]==".") ^ (emil[-3] =="."):
                    for i in emil:
                        if i ==i.isspace():
                              k=1
                        elif i.isalpha():
                             if i.isupper():
                                  j=1
                        elif i.isdigit():
                             continue
                        elif i=="_" or i =="." or i=="@":
                             continue
                        else:
                             d=1          
                    if k == 1 or j == 1 or d == 1:
                         print("wrong email 5")
                    else:
                         print("email is totally alright.")
                else:
                     print("wrong email 4")
            else:
                print("wrong emil 3")                       
    else:
        print("wrong emil 2")        
else:
    print("wrong emil 1")

