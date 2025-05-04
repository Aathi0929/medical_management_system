from controller.check_people import patient
class view:
    def start(self):
        print("Welcome to our shop")
        print("1.login")
        print("2.register")
        print("3.view bill")
        print("view history")
        n=int(input())
        if patient(n):
            pass
        else:
            print("Invalid")
            view().start()
    def emstart():
        pass 


