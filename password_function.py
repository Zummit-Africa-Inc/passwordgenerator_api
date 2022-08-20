#PASSWORD GENERATOR

import array
import random


def password_generator():
    #The Minimun length of password should be 12. 
    #This is becasue it takes 34,000 years to hack a 12 character length password to hack
    #source: https://www.weforum.org/agenda/2021/12/passwords-safety-cybercrime/
    min_len = 12

    #digits, lowercases, uppercases, and special characters
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                    '-', '_', '=', '+', '{', '}', '[', ']', '|', '/', ';', ':', 
                    '<', '>', ',', '.', '?']

    #combined list of digit, lowercase, uppercase, and special character.
    combined = digit + lowercase + uppercase + special_char

    #Selecting 1 randon digit, lowercase, uppercase, and special character.
    r_digit = random.choice(digit)
    r_lowercase = random.choice(lowercase)
    r_uppercase = random.choice(uppercase)
    r_special_char = random.choice(special_char)

    #We first create an initial four-character pre_password containing all of digit, lowercase, uppercase, and special character.
    pre_password = r_digit + r_lowercase + r_uppercase + r_special_char

    #To make the password to be 12 character long, we fill the remaining 8 characters with randomly from the combined list.
    for i in range (min_len - len(pre_password)):
        pre_password = pre_password + random.choice(combined)
        #convert pre_password into array
        password_array = array.array('u', pre_password)
        #shuffle to prevent predictable pattern
        random.shuffle(password_array)

    #Tranverse the password_array and append the characters to form password
    password = " "
    for j in password_array:
        password = password + j

    return password



