import re
import string
def check_password_strength(password):
    global F1, F2, F3, F4, F5
     
    def lengthcal():
        if(len(password)>=8):
            return True
        else:
            return False
    def uppercase():
        str=password
        che=bool(re.search(r'[A-Z]',str))
        return che
    def lowercase():
        str=password
        che=bool(re.search(r'[a-z]',str))
        return che
    def digitcheck():
        str=password
        che=bool(re.search(r'[0-9]',str))
        return che
    def spechar():
        str=password
        for s in str:
            if s in string.punctuation:
                return True
        else:
            return False
        #regex= re.compile('[@_!#$%^&*()<>?/|}{~:-][;]')
       # if(regex.search(str)==None):
         #   return False
       # else:
         #   return True
            
    F1=lengthcal()
    F2=uppercase()
    F3=lowercase()
    F4=digitcheck()
    F5=spechar()
     
    if(F1==False):
        if(F2==False):            
            if(F3==False):
                if(F4==False):
                    if(F5==False):
                        print("The length of the Password should be more than 8 characters and The Password should have atleast one Lower case and one Upper case chanracter and one special chanracter")
                        return False
                    else:
                        
                        print("The length of the Password should be more than 8 characters, should have atleast one Upper and Lower case character and should have atleast one Digit[0-9]")
                        return False
                else:
                    print("The length of the Password should be more than 8 characters and The Password should have one Upper case chanracter and Lower Character")
                    return False
            elif(F5==False):
                    print("The length of the Password should be more than 8 characters and The Password should have atleast one Upper case chanracter and one special chanracter and one Digit [0-9]")
                    return False
            elif(F4==False):
                print("The length of the Password should be more than 8 characters and The Password should have atleast one Upper case chanracter and one special chanracter")
                return False
            else:
                print("The length of the Password should be more than 8 characters and The Password should have atleast one Lower case chanracter")
                return False 
        elif(F3==False):
            print("The length of the Password should be more than 8 characters and The Password should have atleast one Lower case chanracter and one Special Character and one Digit[0-9]")
            return False 
        elif(F4==False):
            print("The length of the Password should be more than 8 characters and The Password should have atleast one Lower case chanracter and one Special Character")
            return False
        elif(F5==False):
            print("The length of the Password should be more than 8 characters and The Password should have atleast one Lower case chanracter")
            return False      
        else:
            print("The length of the Password should be more than 8 characters")
            return False
    elif(F2==False):
        if(F3==False):
            if(F4==False):
                if(F5==False):
                    print("Please enter the Password with atlease one Special Character, one Digit, one Upper case and one Lower case letter ")
                    return False
                else:
                    print("Please enter the Password with atlease one Digit one Upper case and one Lower case letter ")
                    return False
            elif(F5==False):
                print("Please enter the Password with atlease one Special Character, one Upper case and one Lower case letter ")
                return False
            else:
                print("Please enter the Password with atlease one Upper case and one Lower case letter")
                return False
        elif(F5==False):
            print("Please enter the Password with atlease one Special Character, one Upper case and one Digit[0-9] ")
            return False 
        elif(F4==False):
            print("Please enter the Password with atlease one Special Character, one Upper case ")
            return False
        else:
            print("Please enter the Password with atlease one Upper case")
            return False
    elif(F3==False): 
        if(F4==False):
            if(F5==False):
                print("Please enter atleast one Special Character, one Digit and one Lower case letter")
                return False
            else:
                print("Please enter atleast one Digit and one Lower Case letter")
                return False
        elif(F5==False):
            print("Please enter atleast one Special Character, and one Lower case letter")
            return False
        else:
            print("Please enter atleast one Lower Case letter")
            return False
    elif(F4==False):
        if(F5==False):
            print("\nThe Password should have atleast one Special Character (eg : !, @, # , $, %) and one Digit")
            return False
        
        else:
            print("\nThe length of the Password should have atleast one DIgit[0-9]")
            return False
    elif(F5==False):
        print("\nThe Password should have atleast one Special Character (eg : !, @, # , $, %)")
        return False
    
    else:    
        return True
    
        
str = input("Enter the Password of your CHoise\n")
result=check_password_strength(str)
if(result==False):
    print("Please try again with all the criteria")
else:
    print("Met all the Password criteria \t")
    print("Password saved") 