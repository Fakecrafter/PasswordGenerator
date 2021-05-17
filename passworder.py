#!usr/bin/python3
import random
import pyperclip

buchstaben_zahlen = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! \" $ % & / ( ) = ? + * # ' , ; . : - _".split()


länge = int(input("wie lang soll dein passwort sein?  \n"))
#    if länge == "quit":
#        break

password = ''

for _ in range(int(länge)):
    password += str(random.choice(buchstaben_zahlen))

print(password)
pyperclip.copy(password)
