import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

class AES_Encryption(object):
    def __init__(self):
        self.__blocksize = 64*1024

    #----------Hash Password User Inputted And Make Into Key----------#
    def gen_key(self,password):
        hasher = SHA256.new(password.encode('utf-8')) 
        return hasher.digest()


    #----------Padding Function----------#
    def add_padding(self,block):
       if len(block) % 16 != 0:
           block = b' ' * (16-(len(block) % 16))
           return block
       else:
           return 0

    #----------Encrypt Function----------#
    def encrypt(self,filename,password):
        filesize = str(os.path.getsize(filename))
        filesize = filesize.zfill(16)
        encrypted_file = "encrypted"+filename
        IV = Random.new().read(16)

        encryptor = AES.new(password,AES.MODE_CBC, IV)
        binaryFile = open(filename,'rb')
        eFile = open(encrypted_file,'wb')

        try:
            eFile.write(filesize.encode('utf-8'))
            eFile.write(IV)
            while True:
                block = binaryFile.read(self.__blocksize)
                if(len(block) == 0):
                    break
                elif(len(block) % 16 != 0):
                    block = block + b' ' * (16-(len(block) % 16))
                eFile.write(encryptor.encrypt(block))
        except Exception,e:
            print e

        binaryFile.close()
        eFile.close()


    #----------Decrypt Function----------#
    def decrypt(self,filename,password):
        decrypted_file = "decrypted" + filename

        binaryFile = open(filename,'rb')
        dFile = open(decrypted_file,'wb')

        filesize = int(binaryFile.read(16))
        IV = binaryFile.read(16)

        decryptor = AES.new(password,AES.MODE_CBC,IV)

        while True:
            block = binaryFile.read(self.__blocksize)
            if(len(block) == 0):
                break
            dFile.write(decryptor.decrypt(block))

        dFile.truncate(filesize)


        binaryFile.close()
        dFile.close()
