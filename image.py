print("pixel manipulstion")

#semmatric key in encryption and decryption 


def Enc(path,key):
    try :
        # open file
        fin = open(path, 'rb')
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
     
        # converting image into byte array to 
        # perform encryption easily on numeric data
        image = bytearray(image)
        #print(image)
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
           image[index] = values ^ key
 
        # opening file for writing purpose
        fin = open(path, 'wb')
     
        # writing encrypted data in image
        fin.write(image)
        fin.close()
    except Exception:
        print('Error caught : ', Exception.__name__)
        
def Dec(path,key):
    try :
        # open file
        fin = open(path, 'rb')
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
     
        # converting image into byte array to 
        # perform encryption easily on numeric data
        image = bytearray(image)
        #print(image)
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
           image[index] = values ^ key
 
        # opening file for writing purpose
        fin = open(path, 'wb')
     
        # writing encrypted data in image
        fin.write(image)
        fin.close()
    except Exception:
        print('Error caught : ', Exception.__name__)
             
        
 
 
while 1:
     
  ch=input("if you want encrept enter EN if you want decrypt enter DE ")

  if ch=="EN":
    path=input("enter your image path :")
    
    key = int(input("enter key : "))
    Enc(path, key)
    print("Encrypted....")


  elif ch=="DE":
    path=input("enter your image path :")
    
    key = int(input("enter key : "))
    Dec(path, key)
    print("decrypted....")  
    
  else :
    print("invalid input")
