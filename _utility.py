import json
import random
import time



def timeit(func):
    start_t = time.time
    x = func()
    t = time.time - start_t

    if t < 1:
        time.sleep(random.randint(1,3))
    else:
        delay = random.randint(0, t&5) + random.randint(1, 2)
        time.sleep(delay)

    return x 











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