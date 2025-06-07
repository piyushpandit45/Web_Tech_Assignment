email = input("Enter your email id: ")
k = 0

if len(email) >= 6:
    if email[0].isalpha():  
        if ("@" in email) and (email.count("@") == 1):  
            if (email[-4] == ".") ^ (email[-3] == "."):  
                for i in email:
                    if i.isspace(): 
                        k = 1
                        break
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i in ['_', '.', '@']:  
                        continue
                    else:
                        k = 1
                        break

                if k == 1:
                    print("Email is invalid: contains invalid characters or space.")
                else:
                    print("Valid email.")
            else:
                print("Email is invalid: dot position error.")
        else:
            print("Email is invalid: @ error.")
    else:
        print("Email is invalid: should start with alphabet.")
else:
    print("Email is invalid: too short.")
