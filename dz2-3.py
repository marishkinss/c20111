import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def play(self):
         print("Time to play")
         self.progress+=0.12
         self.gladness+=3
    def sleep(self):
         print("Time to sleep")
         self.gladness+=3
    def chill(self):
         print("Time to eat")
         self.gladness+=5
         self.progress-=0.1
    def is_alive(self):
        if self.progress< -0.5:
            print("Cast out...")
            self.alive=False
        elif self.gladness<=0:
            print("depresion")
            self.alive=False
        elif self.progress>5:
            print("Pessed externall...")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self,day):
        day="Day" +str(day)+ "of" + self.name +"life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.play()
        elif live_cube==2:
            self.sleep()
        elif live_cube==3:
            self.eat()
        self.end_of_day()
        self.is_alive()
nick=Cat(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)