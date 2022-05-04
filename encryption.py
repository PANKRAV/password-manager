#modules
#encryption
from functools import singledispatchmethod
from numpy import random as nprand
from hashlib import sha256

from rsa import PrivateKey, PublicKey
import rsa
from secrets import choice
import cryptography
from base64 import encode
import hashlib
from simplecrypt import encrypt, decrypt
from cryptography.fernet import Fernet



#utility
import _utility #user defined
from password_manager import Password, User, handle_file 
import os
import json


#consts
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
ran_char_seq = 'hA#Fm&s%)0YanG$gQ3xylpvjB9f^M17S6eRCuqDZiwK*Ub!TLot4XV8@HONJ2rE5IcW(zdPk'   
security = 2048






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
        








#FERNET


#fernet_encrypt
def enc_fernet(ctx) -> str:
    f_in_key = Fernet.generate_key()
    f_key = Fernet(f_in_key)
    return f_key.encrypt(ctx.encode())


#Fernet_decrypt
def dec_fernet(f_key : Fernet, ctx) -> str:
    return f_key.decrypt(ctx).decode()







#First Step
def simple_crypt(passkey, ctx, mode : str = "enc") -> str:
    
    if mode == "enc":
        return encrypt(passkey, ctx)

    elif mode == "dec":
        return decrypt(passkey, ctx)

    else:
        return None



class enc_rsa:




    @staticmethod
    class Single_pwd:


        def __init__(self, user : User, ctx : str, enc_key, choice : str = None):

            self.enc_key = enc_key
            self.User = user

            abspath = os.path.abspath(__file__)
            dname = os.path.dirname(abspath)
            os.chdir(dname)
            os.chdir("encryption_data")

            self.enc_json = _utility.handle_file(self.User.file, "json read")


            if choice == "new":

                self.publicKey = self.enc_json["publicKey"]
                self.publicKey = self.publicKey.encode("latin-1")
                self.publicKey = simple_crypt(enc_key, self.publicKey, "dec")
                self.publicKey = rsa.PublicKey.load_pkcs1(self.publicKey)
                self.publicKey : PublicKey

                self.encContent = rsa.encrypt(ctx.encode("latin-1"),
                                    self.publicKey)
            
            else:
                
                self.publicKey = self.enc_json["publicKey"]
                self.publicKey = self.publicKey.encode("latin-1")
                self.publicKey = simple_crypt(enc_key, self.publicKey, "dec")
                self.publicKey = rsa.PublicKey.load_pkcs1(self.publicKey)
                self.publicKey : PublicKey

                self.encContent = ctx.encode("latin-1")

            self.privateKey = self.enc_json["privateKey"]
            self.privateKey = self.privateKey.encode("latin-1")
            self.privateKey = simple_crypt(enc_key, self.privateKey, "dec")
            self.privateKey = rsa.PrivateKey.load_pkcs1(self.privateKey)
            self.privateKey : PrivateKey


            self.decContent = rsa.decrypt(self.encContent, self.privateKey).decode()
            
            


        def revert(self, ctx):
            privateKey = simple_crypt(self.User.key, ctx, "dec")
            return rsa.decrypt(ctx, privateKey).decode()






    @staticmethod
    class User_pwd():



        def __init__(self, User : User, enc_key = None):

            publicKey, privateKey = rsa.newkeys(security)
            self.enc_key = enc_key
            self.User = User

            abspath = os.path.abspath(__file__)
            dname = os.path.dirname(abspath)
            os.chdir(dname)
            os.chdir("encryption_data")


            self.enc_json = _utility.handle_file(self.User.file, "json read")
            
            publicKey = self.enc_json["publicKey"]
            publicKey = publicKey.encode("latin-1")
            publicKey = simple_crypt(enc_key, publicKey, "dec")
            publicKey = rsa.PublicKey.load_pkcs1(publicKey)

            self.privateKey = self.enc_json["privateKey"]
            self.privateKey = self.privateKey.encode("latin-1")
            self.privateKey = simple_crypt(enc_key, self.privateKey, "dec")
            self.privateKey = rsa.PrivateKey.load_pkcs1(self.privateKey)
            self.privateKey : PrivateKey
 

            




            del publicKey, privateKey



        def reset(self):

            _json = self.print_data()
            _json = json.loads(_json)
            _json : dict



            abspath = os.path.abspath(__file__)
            dname = os.path.dirname(abspath)
            os.chdir(dname)
            os.chdir("encryption_data")

            self.publicKey, self.privateKey = rsa.newkeys(security)

            publicKey = self.publicKey
            privateKey = self.privateKey

            publicKey = simple_crypt(self.enc_key, publicKey.save_pkcs1())
            publicKey = publicKey.decode("latin-1")


            privateKey = simple_crypt(self.enc_key, privateKey.save_pkcs1())
            privateKey = privateKey.decode("latin-1")



            
            

            with open(f"{self.User.name}.json", mode = "w") as f:

                new_json = {"privateKey" : privateKey, "publicKey" : publicKey}
                new_json = json.dumps(new_json)
                f.write(new_json)
            
            del new_json


            os.chdir("..")
            os.chdir("data/passwords")

            new_json = _json.copy()

            for key, item in new_json.items() :
                
                new_pwd = rsa.encrypt(new_json[key]["pwd"].encode("latin-1"), self.privateKey)
                new_pwd = new_pwd.decode("latin-1")

                new_json[key]["pwd"] = new_pwd


            with open(f"{self.User.name}.json", mode = "w") as f:

                new_json = json.dumps(new_json)
                f.write(new_json)





        def print_data(self) -> str:
            
            abspath = os.path.abspath(__file__)
            dname = os.path.dirname(abspath)
            os.chdir(dname)
            os.chdir("data/passwords")

            _json = handle_file(self.User.file, "json read")


            dec_json = _json.copy()

            for key, item in dec_json.items() :
                
                new_pwd = rsa.decrypt(dec_json[key]["pwd"].encode("latin-1"), self.privateKey)

                dec_json[key]["pwd"] = new_pwd.decode("latin-1")

            return json.dumps(dec_json)












"""
def enc_rsa(ctx, inUser : User) -> str:
    publicKey, privateKey = rsa.newkeys(512)

    privateSafe = simple_crypt(inUser.key, privateKey)


    encMessage = rsa.encrypt(ctx.encode(),
                            publicKey)
"""

#third step    
def placeholder(ctx) -> str:
    pass



















def standard(ctx):
    pass

def trigonometric(ctx):
    pass

def random(ctx):
    pass







#hash processes
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





