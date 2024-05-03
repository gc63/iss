class Restuarantchatbot:
    def __init__(self):
        self.greetings=["Hello there!","Hii"]
        self.menu=["\n1.Vada Pav(Rs.15) \n2.Bhel(Rs.25) \n3.Panipuri(Rs.45)"]
        self.goodbye=["Thanks For Your Visit"]
        self.unknown=["Sorry i Did Not Understood"]

    def greet(self):
        return self.greetings[0]
    
    def provide_menu(self):
        return self.menu[0]
    
    def reservation(self):
        return "reservation is available today!"

    def say_bye(self):
        return self.goodbye[0]
    
    def respond(self,message):
        if "reservation" in message:
            return self.reservation()
        
        elif "menu" in message:
            return self.provide_menu()
        
        elif "bye" in message:
            return self.say_bye()
        
        elif any(word in message for word in ["hi","hii","hello","heyy","namaste"]):
            return self.greet()
        
        else:
            return self.unknown[0]
        
chatbot=Restuarantchatbot()
print("Restuarant chatbot: ",chatbot.greet())
while True:
    user=input("You: ")
    if user.lower()=="exit":
        print(chatbot.say_bye)

    response=chatbot.respond(user)
    print("Restuarant chatbot: ", response)