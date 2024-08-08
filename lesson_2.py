from random import choice

def password(question_1):

    passwords = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    result = ""

    for i in range(question_1):
        result += choice(passwords)

    return  result

