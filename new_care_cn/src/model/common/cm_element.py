from enum import Enum
class Cmelement(Enum):
    userName = {'key':'id','value':'username'}
    passWord = {'key':'id','value':'password'}
    login = {'key':'xpath','value':'//*[@id="loginform"]/button'}
    skip = {'key':'xpath','value':'/html/body/div[15]/div/div[5]/a[1]'}