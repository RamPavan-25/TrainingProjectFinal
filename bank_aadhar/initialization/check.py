def check():
    try:
        with open(r"bank_aadhar\files\firsttime.txt","r") as a:
            if a.read().strip()=="True":
                return True
            else:
                return False
    except FileNotFoundError:
        with open(r"bank_aadhar\files\firsttime.txt","w") as a:
            a.write("True")
            return True