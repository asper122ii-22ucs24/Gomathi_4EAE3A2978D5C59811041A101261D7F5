#Define the back class player
class player:
     def play(self):
         print ("The player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")
#define the derived class bowler
class Bowler(player):
     def play(self):
         print("The bowler is bowling.")
#create object of  Batsman and bowler classes
batsman=Batsman()
bowler=Bowler()
#call the paly() method for each object 
batsman.play()
bowler. play()
