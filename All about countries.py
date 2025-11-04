class Pakistan():
    def capital (self):
        print('Islamabad is the capital of Pakistan') 
    def language (self):
        print('The language of Pakistan is Urdu') 
class China():
    def capital (self):
        print('Beijing is the capital of China') 
    def language (self):
        print('The language of China is Chinese') 
obj_pakistan = Pakistan()
obj_china = China() 
for country in (obj_pakistan , obj_china):
    country.capital() 
    country.language()