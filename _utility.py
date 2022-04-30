import json












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