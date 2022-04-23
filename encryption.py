import hashlib
from numpy import random as nprand
from hashlib import sha512, sha3_512

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
ran_char_seq = 'hA#Fm&s%)0YanG$gQ3xylpvjB9f^M17S6eRCuqDZiwK*Ub!TLot4XV8@HONJ2rE5IcW(zdPk'   

def ceasar(ctx, indent : int = 0) -> str:
    ctx = list(ctx)
    for idx, char in enumerate(ctx):
        char:str
        if not char.isspace():
            #ran_char_seq =  was assigned at line 22
            _index = ran_char_seq.index(char)
            try:
                new_char = ran_char_seq[_index + indent]
            
            except IndexError:
                if _index + indent > 72:
                    new_char = ran_char_seq[indent]
                
                elif _index + indent < 0:
                    new_char = ran_char_seq[72 - indent]
            ctx[idx] = new_char

    return "".join(ctx)


def reverse_ceasar(ctx, indent : int = 0) -> str:
    return ceasar(ctx , -indent)
        

def standard(ctx):
    pass

def trigonometric(ctx):
    pass

def random(ctx):
    pass

def hash2(ctx) -> str:
    byte_data = ctx.encode()
    return hashlib.sha512(byte_data).hexdigest()

def hash3(ctx) -> str:
    byte_data = ctx.encode()
    return hashlib.sha3_512(byte_data).hexdigest()

def salt(ctx : str) -> str:
    salt = random_password(5)
    return ctx + salt



def random_password(length = 10):
    pr = []

    char_list = [char for char in chars]
    lower_list = [char for char in lower]
    upper_list = [char for char in upper]
    numbers_list = [char for char in numbers]
    symbols_list = [char for char in symbols]

    const = 1/len(char_list)

    for char in char_list:
        
        if char in lower_list:
            pr.append(0.2/len(lower_list))


        elif char in upper_list:
            pr.append(0.2/len(upper_list))


        elif char in numbers_list:
            pr.append(0.3/len(numbers_list)) 

        
        elif char in symbols_list:
            pr.append(0.3/len(symbols_list)) 

        
    password = nprand.choice(char_list, p = pr, size = length) 

    return "".join(password)
input()
while True:
    txt = ceasar(input(), 3)
    print(txt)
    print(reverse_ceasar(txt, 3))