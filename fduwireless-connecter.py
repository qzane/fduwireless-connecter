import requests
class fduwireless(object):
    def __init__(self,username='',password=''):
        super(fduwireless,self).__init__()
        self.url_login = r'https://1.1.1.1/login.html'
        self.url_logout = r'https://1.1.1.1/logout.html'
        self.data_login = dict(buttonClicked='4',username=username,password=password)
        self.data_logout = dict(userStatus='1')
        
    def login(self,username=None,password=None):
        if username:
            self.data_login['username']=username
        if password:
            self.data_login['password']=password
        res = requests.post(self.url_login,data=self.data_login,verify=False) 
        #if you don't want use Fudan CA
        print(res)
        
    def logout(self):
        res = requests.post(self.url_logout,data=self.data_logout,verify=False)
        #if you don't want use Fudan CA
        print(res)
        
        
if __name__ == '__main__':
    connect = fduwireless('your ID','your password')
    connect.login()
    #import time
    #time.sleep(60)
    #connect.logout()
    
