from Senior_Project_Class import AES_Encryption
import os
import os.path


def checkFile(fname):
    if(os.path.isfile(fname)) and (os.access(fname,os.R_OK)):
        print("[+] File exist and is readable")
        return True
    else:
        print("[-] File is missing or is not able to be read!")
        return False


def main():
    obj1 = AES_Encryption()
    while True:
        print("AES Encryption (E)NCRPYT | (D)ECRYPT")
        c = raw_input()
        if c == "E":
            efile = raw_input("What File Do You Want To Encrypt:")
            if(checkFile(efile) == True):
                password = raw_input("Must Create Key. Please Enter A Password:")
                if password:
                    print("[+] Ready to Encrypt")
                    key = obj1.gen_key(password)
                    obj1.encrypt(efile,key)
                    print("[+] Success")
                    break
                else:
                    print("Invalid Password")
            else:
                break
        elif c == "D":
            dfile = raw_input("What File Do You Want To Decrypt:")
            if(checkFile(dfile) == True):
                password = raw_input("Enter Password Used To Encrypt:")
                if password:
                    print("[+] Ready To Decrypt")
                    key = obj1.gen_key(password)
                    obj1.decrypt(dfile,key)
                    print("Success")
                    break
                else:
                    print("[-] Invalid Password")
            else:
                break
        else:
            print("[-] Invalid User Response")


if __name__ == '__main__':
    main()
