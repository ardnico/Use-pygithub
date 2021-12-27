#!/usr/bin/env python3


import string

alphabets = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation

class Enc(object):
    def __init__(self,n,enc_set=["&",")",">","x","K","A","w","f","?","z","C"]):
        if "-" in enc_set:
            print("enc set can't contain '-'")
            self.enc_set = ["&",")",">","x","K","A","w","f","?","z","C"]
        else:
            self.enc_set = enc_set
        
        if n > 10:
            print("n must lowwer than 10")
            self.n = 9
        else:
            self.n = n
        print(f'Set: {self.n}')

    def Base_10_to_n(self,X):
        X_dumy = X
        n = self.n
        out = ''
        while X_dumy>0:
            out = str(X_dumy%n)+out
            X_dumy = int(X_dumy/n)
        return out

    def Base_n_to_10(self,X):
        out = 0
        n = self.n
        X = str(X)
        for i in range(1,len(X)+1):
            out += int(X[-i])*(n**(i-1))
        return out

    def enc(self,keyword):
        num_array = ""
        for i in range(len(keyword)):
            tmp_num = alphabets.find(keyword[i])
            tmp_num += 13
            tmp_num = tmp_num % len(alphabets)
            tmp_num = self.Base_10_to_n(tmp_num)
            tmp_num = str(tmp_num)
            tmp_num = tmp_num.zfill(3)
            if len(num_array) != 0:
                num_array += "-"
            num_array += tmp_num
        for i,sym in enumerate(self.enc_set):
            num_array = num_array.replace(str(i),str(sym))
        return num_array
    
    def dec(self,keyword):
        for j,sym in enumerate(self.enc_set):
            keyword = keyword.replace(str(sym),str(j))
        num_array = ""
        for key in keyword.split("-"):
            tmp_num = int(key)
            tmp_num = self.Base_n_to_10(tmp_num)
            tmp_num -= 13
            tmp_num += len(alphabets)
            tmp_num = tmp_num % len(alphabets)
            num_array += alphabets[tmp_num]
        return num_array
    
