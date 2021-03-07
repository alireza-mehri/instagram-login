#pip3 install InstagramAPI
from InstagramAPI import InstagramAPI
api = InstagramAPI("mahnaz.khanoum1" ,"Borhan")

if(api.login()):
    print("loged in")
else:
    print("some error with login")