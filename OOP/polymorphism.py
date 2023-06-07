from abc import ABC, abstractmethod
# 登入抽象類別
class Login(ABC):
    @abstractmethod
    def login(self):
        pass
# Facebook登入機制
class FacebookLogin(Login):
    def login(self):
        print("Facebook login implementation.")
#Google登入機制
class GoogleLogin(Login):
    def login(self):
        print("Google login implementation.")
#Twitter登入機制
class TwitterLogin(Login):
    def login(self):
        print("Twitter login implementation.")
        
fb = FacebookLogin()
fb.login()
google = GoogleLogin()
google.login()
twitter = TwitterLogin()
twitter.login()
