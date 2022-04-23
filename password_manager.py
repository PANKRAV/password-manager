#files
import json
import os
import pathlib
import sys


#utility
from functools import singledispatchmethod
import asyncio
from cgitb import text
from msilib.schema import Error
import math
from ast import Pass
import pyautogui as pg


#cryptography
from numpy import random as nprand
from hashlib import sha256
import rsa
from secrets import choice
import cryptography
from base64 import encode
import hashlib
#user defined
import encryption




chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
ran_char_seq = "hA#Fm&s%)0YanG$gQ3xylpvjB9f^M17S6eRCuqDZiwK*Ub!TLot4XV8@HONJ2rE5IcW(zdPk"

users_data = dict({})



class Errors(Exception):
    pass




    
class BadValue(Errors):
    pass


async def minimal_time(func, delay : int):
    tasks = []

    async def _func():
        func()


    async def _time(_delay):
        await asyncio.sleep(_delay)
        return


    task1 = await _time(delay)
    task2 = await _func()
    tasks.append(task1)
    tasks.append(task2)
    asyncio.gather(*tasks)





class User:
    global key


    user_count = 0
    def __init__(self, name, key = None, salt = None, passwords = 0):
        self.name = name
        self.key = key
        self.passwords = passwords
        self.file = f"{self.name}.json"
        self.salt = salt
        #self.key = None



        User.user_count += 1



    def __repr__(self) -> str:
        if self.key == None:
            print(f"{self.name} has {self.passwords} passwords")

        else:

            print("profile is locked")



    def __call__(self, key):


        if self.check_key(key) == True:

            print("access gained")


            return self.acess(enc_key = key)



        else:
            print("acess failed")


        return users_data[self.name]










    def __str__(self):
        return self.name




    def get_password(self, acc_name = None, enc_key : str = 0):


        _json = handle_file(self.file, "json read")
        if acc_name == None:

            acc_name = input("what account is it:")

            while not acc_name in _json.keys():
                acc_name = input(

"""
account does not exist
give another name:"""
)

        pwd = Password.User_pwd(self, acc_name)

        print(
f"""
account name: {pwd.acc_name} 
email: {pwd.email}
username: {pwd.username}
password: {pwd.password}"""
)



        input("done? :")
        os.system('cls||clear')














    def add_password(self, enc_key : str = 0):


        _json = handle_file(self.file, "json read")
        acc_name = input("what account is it:")
        while acc_name in _json.keys():
            acc_name = input(

"""
account already exists
give another name:"""
)




        username = input("whats your username:")


        while True:             
            email = input("what's your email:")

            if email != email.rstrip():
                print("email can't have a whitespace")

            else:
                break


        while True:

            mode = input(

"""
1.random password
2.chooce a password
choice:"""
)




            while not isinstance(mode, int) or not (str(mode) in ["1", "2"]):

                try:
                    mode = int(mode)
                    if not (mode in [1, 2]):
                        mode = int(input("Input needs to be a number between 1 and 2:"))

                except ValueError:
                    mode = input("Input needs to be a number:")


            if mode == 2:

                pwd = input("whats your password:")

            else:
                while True:
                    try:
                        length = int(input("give length:"))
                        break  

                    except ValueError:

                        length = input("choice needs to be an integer\nnew choice:")

                pwd = random_password(length)
                print(f"your password is {pwd}")


                choice = input("If you want to generate a new password type yes\n")

                if  not choice.upper() == "YES":
                    break





        _json[acc_name] = {"username" : username, "pwd" : pwd, "email": email}
        _json = json.dumps(_json)

        with open(self.file, mode = "w") as f:
            f.write(_json)


        input("done? :")
        os.system('cls||clear')





    def modify_password(self, enc_key : str = 0):

        _json = handle_file(self.file, "json read")
        acc_name = input("what account is it:")

        while not acc_name in _json.keys():
            acc_name = input(

"""
account does not exist
give another name:"""
)



        while True:


            pwd = Password.User_pwd(self, acc_name)

            print(
f"""
account name: {pwd.acc_name} 
email: {pwd.email}
username: {pwd.username}
password: {pwd.password}"""
)



            print("what would you like to change?")

            change = input(
"""
1.account name:
2.email
3.username
4.password
5.view current
choice:"""
)



            while not isinstance(change, int) or not (str(change) in ["1", "2", "3", "4", "5"]):

                try:
                    change = int(change)
                    if not (change in [1, 2, 3, 4, 5]):
                        change = int(input("Input needs to be a number between 1 and 5:"))

                except ValueError:
                    change = input("Input needs to be a number:")



            if change == 1:
                while True:
                    change_text = input("new account name:")

                    if change_text in list(_json.keys()):

                        print("account already exists")

                    else:
                        break

                _json[change_text] = _json.pop(acc_name)




            elif change == 2:

                while True:

                    change_text = input("new email:")

                    if change_text != change_text.rstrip():
                        print("email can't have a whitespace")

                    else:
                        break




                _json[acc_name]["email"] = change_text


            elif change == 3:
                change_text = input("new username:")

                _json[acc_name]["username"] = change_text



            elif change == 4:


                while True:

                    mode = input(

"""
1.random password
2.chooce a password
choice:"""
)






                    #minimized
                    while not isinstance(mode, int) or not (str(mode) in ["1", "2"]):

                        try:
                            mode = int(mode)
                            if not (mode in [1, 2]):
                                mode = int(input("Input needs to be a number between 1 and 2:"))
                        
                        except ValueError:
                            mode = input("Input needs to be a number:")


                    #minimized
                    if mode == 2:

                        pwd = input("whats your password:")

                    else:
                        while True:
                            try:
                                length = int(input("give length:"))
                                break  

                            except ValueError:

                                length = input("choice needs to be an integer\nnew choice:")


                        pwd_text = random_password(length)

                        print(f"your password is {pwd_text}")




                        choice = input("If you want to generate a new password type yes\n")


                        if not choice.upper() == "YES":
                            break


                _json[acc_name]["pwd"] = pwd_text





            elif change == 5:

                self.get_password(acc_name, enc_key = enc_key)



            else:
                pass

            _json = json.dumps(_json)
            with open(self.file, mode = "w") as f:
                f.write(_json)



            done = input("Are you done with the changes?\n1.Yes\n2.No\nchoice:")

            #minimized
            while not isinstance(done, int) or not (str(done) in ["1", "2"]):

                try:
                    done = int(done)
                    if not (done in [1, 2]):
                        done = int(input("Input needs to be a number between 1 and 3:"))

                except ValueError:
                    done = input("Input needs to be a number:")



            if done == 1:
                
                os.system('cls||clear')

                break


            elif done == 2:
                _json = handle_file(self.file, "json read")

                continue


            else:
                pass















    def delete_password(self):

        _json = handle_file(self.file, "json read")
        acc_name = input("what account is it:")



        while not acc_name in _json.keys():
            acc_name = input(

"""
account does not exist
give another name:"""
)


        choice = input("Are you sure\n1.Yes\n2.No\nchoice:")

        while not isinstance(choice, int) or not (str(choice) in ["1", "2"]):

            try:
                choice = int(choice)
                if not (choice in [1, 2]):
                    choice = int(input("Input needs to be a number between 1 and 2"))
            
            except ValueError:

                choice = input("Input needs to be a number:")


        if choice == 1:
            _key = input("confirm with user key")

            if self.check_key(key = _key) == False:
                print("wrong key")
                return


            _json.pop(acc_name)


            _json = json.dumps(_json)
            with open(self.file, mode = "w") as f:
                f.write(_json)

        else:
            return



        os.system('cls||clear')






    def list_accounts(self):

        _json = handle_file(self.file, "json read")

        if _json == {} or _json == { }:
            print("It does'nt seem they are any account\nmaybe create some")
            return


        print()

        for index, account in enumerate(_json, start = 1) :
            print(f"{index}.{account}")



        input("done? :")

        os.system('cls||clear')







    """
    @singledispatchmethod
    def update_users(self):
        pass




    @update_users.register
    def single_user(self):
        pass
    """





    def check_key(self, key, hash_type = 3) -> bool:

        key += self.salt
        if hash_type == 3:
            key = encryption.hash3(key)
        elif hash_type == 2:
            key = encryption.hash2(key)




        if key == self.key:
            return True

        else:
            return False
















    def acess(self, enc_key : str = 0):


        while True:

            mode = input(
"""
MODE:
1.Add password account
2.Acess password account
3.Modify password account
4.Delete password account
5.List accounts
6.Get encrypted copy of data
7.Get decrypted copy of data
8.exit
9.back
choice:"""
)




            while not isinstance(mode, int) or not (str(mode) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):

                try:
                    mode = int(mode)
                    if not (mode in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
                        mode = int(input("Input needs to be a number between 1 and 9"))
                
                except ValueError:
                    mode = input("Input needs to be a number")





            if mode ==  1:
                self.add_password(enc_key = enc_key)


            elif mode == 2:
                self.get_password(enc_key = enc_key)


            elif mode == 3:
                self.modify_password(enc_key = enc_key)


            elif mode == 4:
                self.delete_password()


            elif mode == 5:
                self.list_accounts()


            elif mode == 6:
                pass


            elif mode == 7:
                pass


            elif mode == 8:
                quit()


            elif mode == 9:
                break






    @staticmethod
    def create_users() -> dict:
        global users_data

        for user in os.listdir():

            if user[:-5] == "passwords":
                continue

            try:

                with open(user, "r") as f:
                    text = f.read()
                    _json = json.loads(text)
                    pw_cnt = len(_json)

            except:

                handle_file(user, "json create")

            os.chdir("..")


            with open("users.json", "r") as f:
                f = f.read()
                _json = json.loads(f)
                _key = _json[user[:-5]]["key"]
                _salt = _json[user[:-5]]["salt"]


            os.chdir("passwords")

            users_data[user[:-5]] = User(user[:-5], passwords = pw_cnt, key = _key, salt = _salt)  




        return users_data 









class Password:


    @staticmethod
    class single:

        def __init__(self, password):

            self.password = password




        def __repr__(self) -> str:

            return self.password





        def encrypt(self, key):
            pass    


        def decrypt(self, key):
            pass




    @staticmethod
    class User_pwd:


        def __init__(self, owner : User, acc_name):

            self.owner = owner
            self.file = owner.file
            self.acc_name = acc_name

            _json = handle_file(self.file, "json read")
            _json = _json[self.acc_name]


            self.username = _json["username"]
            self.password = _json["pwd"]
            self.email = _json["email"]







        def __repr__(self):

            if self.owner.name[:-1].upper() == "S":
                print(
                    f"""
User: {self.owner.name}\' 
\naccount: {self.acc_name} 
\nusersname: {self.username}
\nemail: {self.email}
\npassword: {self.password}

                    """)



            else:
                print(
                    f"""
 User: {self.owner.name}\'s 
 \naccount: {self.acc_name} 
 \nusersname: {self.username}
 \nemail: {self.email}
 \npassword: {self.password}
""")




    def scrape(self) -> dict:
            pass



















def init():

    global dirs
    global users_data


    os.system('cls||clear')


    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    dirs = os.listdir()



    if ".env" not in dirs:
        with pathlib.Path(".env").open(mode = "x") as f:
            pass



    if "data" not in dirs:
        os.mkdir("data")
    os.chdir("data")
    #print(os.getcwd())
    
    
    dirs = os.listdir()
    if "users.json" not in dirs:
        with pathlib.Path("users.json").open(mode = "w") as f:
            f.write(json.dumps({}))


    dirs = os.listdir()
    if "passwords" not in dirs:
        os.mkdir("passwords")

    os.chdir("passwords")



    users_data = User.create_users()




    dirs = os.listdir()








def user_init(name, key = None):
    global users_data

    key = encryption.salt(key)
    salt = key[-5:]
    key = encryption.hash3(key)


    with pathlib.Path(f"{name}.json").open(mode = "x") as f:
            _json = json.dumps({})
            f.write(_json)


    os.chdir("..")

    with open("users.json", mode = "r") as in_f:

        text = in_f.read()
        _json = json.loads(text)
        _json[name] = dict()
        _json[name]["key"] = key
        _json[name]["salt"] = salt
        _json = json.dumps(_json)


    with open("users.json", mode = "w") as out_f:
        out_f.write(_json)

    users_data[name] = User(name, key = key, salt = salt)




    os.chdir("passwords")




















def quit():

    #kialla polla pramata



    sys.exit()








"""

class encryption:


    #indent < 72
    @staticmethod
    def ceasar(ctx, indent : int = 0) -> str:
        ctx = list(ctx)

        for idx, char in enumerate(ctx):

            char:str
            if not char.isspace():
                #chars was assigned at line 22
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




    @staticmethod
    def reverse_ceasar(ctx, indent : int = 0) -> str:

        return encryption.ceasar(ctx , -indent)



    @staticmethod
    def enc_rsa(ctx):
        pass


    @staticmethod
    def placeholder(ctx):
        pass


    @staticmethod
    def standard(ctx):
        pass


    @staticmethod
    def trigonometric(ctx):
        pass


    @staticmethod
    def random(ctx):
        pass


    @staticmethod
    def hash2(ctx) -> str:
        byte_data = ctx.encode()
        return hashlib.sha512(byte_data).hexdigest()


    @staticmethod
    def hash3(ctx) -> str:
        byte_data = ctx.encode()
        return hashlib.sha3_512(byte_data).hexdigest()


    @staticmethod
    def salt(ctx : str) -> str:
        salt = random_password(5)
        return ctx + salt

"""






#opt = norm or json or  json create or norm create
def handle_file(path, opt: str, content = "") -> dict:


    if opt == "json create":

        with open(path, mode = "w") as f:
            f.write(json.dumps({}))
            return


    elif opt == "norm create":

        with open(path, mode = "w"):
            return


    elif opt == "norm read":

        with open(path, mode = "r") as f:
            return f.read()


    elif opt == "json read":

        with open(path, mode = "r") as f:
            return json.loads(f.read())


    elif opt == "json modify":

        _json = handle_file(path, "json read")


        with open(path, mode = "w") as f:
            pass





    elif opt == "norm modify":
        pass



    else:
        return













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







def main():

    init()
    handle_file("passwords.json", "create json")
    
    while True:
        mode = input("mode:\n1.new user\n2.user\n3.exit\nchoice:")

        while not isinstance(mode, int) or not (str(mode) in ["1", "2", "3"]):

            try:
                mode = int(mode)
                if not (mode in [1, 2, 3]):
                    mode = int(input("Input needs to be a number between 1 and 3"))

            except ValueError:
                mode = input("Input needs to be a number")





        print(type(mode))
        print(os.listdir())
        dirs = os.listdir()

        if mode == 1:
            name = input("name:")
            while True:
                if not isinstance(name, str):
                    name = input("Input needs to be a string:")
                elif name in [names[:-5] for names in dirs] :
                    name = input("name already exists:")
                else:
                    break


            key = input("give key:")

            while True:

                if key == input("confirm key:"):
                    break

                else:
                    print("confirmation failed")
                    key = input("give new key:")

            user_init(name, key)



            input("done? :")
            os.system('cls||clear')




        if mode == 2:
            dirs = os.listdir()



            while True:


                if dirs == []:
                    print("they are no users yet\nmaybe create some")
                    break




                in_name = input("give user name:\nor\n1.List Users\n2.Back\nchoice:")

                if in_name in [names[:-5] for names in dirs]:

                    _user : User = users_data[in_name]


                    in_key = input("give key:")

                    while True:

                        if _user.check_key(in_key) == True:


                            #self.__call__() to check if key is valid
                            _user(key = in_key)

                            break

                        else:
                            print("wrong key")
                            opt = input("1.try again \n2.exit:")

                            while not isinstance(opt, int) or not (str(opt) in ["1", "2"]):

                                try:
                                    opt = int(opt)
                                    if not (opt in [1, 2]):
                                        opt = int(input("Input needs to be a number between 1 and 2"))

                                except ValueError:

                                    opt = input("Input needs to be a number:")


                            if opt == 1:
                                in_key = input("give key:")

                            else:
                                break





                elif in_name == "1":
                    idx = []
                    users = []

                    print()

                    for index, user in enumerate(users_data, start = 1) :
                        print(f"{index}.{user}")

                        users.append(user)
                        idx.append(index)



                    choice = input ("choice:")


                    while not isinstance(choice, int) or not (str(choice) in [str(_idx) for _idx in idx]):

                        try:
                            choice = int(choice)
                            if not (choice in idx):
                                choice = int(input(f"Input needs to be a number between {idx[0]} and {idx[:-1]}"))
                        
                        except ValueError:

                            choice = input("Input needs to be a number:")


                    del idx



                    in_name = users[choice - 1]
                    del users



                    _user : User = users_data[in_name]


                    in_key = input("give key:")


                    while True:

                        if _user.check_key(in_key) == True:


                            #self.__call__() to check if key is valid
                            _user(key = in_key)

                            break

                        else:
                            print("wrong key")
                            opt = input("1.try again \n2.exit:")

                            while not isinstance(opt, int) or not (str(opt) in ["1", "2"]):

                                try:
                                    opt = int(opt)
                                    if not (opt in [1, 2]):
                                        opt = int(input("Input needs to be a number between 1 and 2"))

                                except ValueError:

                                    opt = input("Input needs to be a number:")


                            if opt == 1:
                                in_key = input("give key:")

                            else:
                                break



                elif in_name == "2":
                    break




                else:
                    print("account does not exist")




        elif mode == 3:
            break

















if __name__ == "__main__":
    main()

