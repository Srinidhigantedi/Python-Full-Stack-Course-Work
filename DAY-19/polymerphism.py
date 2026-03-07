class hotstar:
    def __init__(self,username):
        print(f'hey {username}, welcome to the hotstar')
    def playvideo(self):
        print("ads will be run")
        print("quality is low")
        print("no download option")
        print("no multiple logins")
    def search(self):
        print("you can search for the programs")
    def watchlist(self):
        print("you can add the movies to watchlist")
    def notifications(self):
        print("you can push the notifications")
    def login(self):
        print("you can login into hotstar")
class premiumhotstar(hotstar):
    def __init__(self,username):
        print(f'hey {username}, welcome to the hotstar')
    def playvideo(self):
        print("ads wont run")
        print("quality is high")
        print("download option")
        print("multiple login")

saaketh=hotstar("saaketh")
saaketh.playvideo()
saaketh.search()
saaketh.watchlist()
saaketh.notifications()
saaketh.login()

sandeep=premiumhotstar("sandeep")
sandeep.playvideo()
sandeep.search()
sandeep.watchlist()
sandeep.notifications()
sandeep.login()




  
