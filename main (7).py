#2.2 implement  a class called Player that represents a cricket  Player.The Player  class should  have  a method  called Play() which prints "The Player  is playing  cricket.Drieve a  two classes,Batsman and Bowler,from the Player  class. override the Play () method in each drieved class  to print " The Batsman is batting " and  "Bowler  is bowlling "respectively.  write a program to Create objects of both the Batsman and Bowler  classes and called the Play ()method for each object.
# Define the Player class
class Player: 
    def play (self):
        print("The player is playing cricket.")
# Define the batsman class, derived from Player
class Batsman (Player):
    def play(self):
        print("The batsman is batting")
# Define the bowler class,derived from Player
class Bowler(Player):
    def play(self):
        print(" The bowler is bowlling ") 
# Create objects of bastman and bowler classes 
batsman = Batsman()
bowler = Bowler() 
# call the paly()method for each object 
batsman.play()
bowler.play() 



  

           