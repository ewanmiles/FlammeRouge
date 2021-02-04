from courseBuilder import *
import card_picker

#help(Racecourse.attributes)

stage = Racecourse("stage_18",[a,black_2,h,white_4,L,o,p,c,white_5,black_6,r,white_3,g,q,J,k,s,t,e,I,U],[["black_2","wet"],["black_6","crosswind"]])
stage.attributes()


class rouleur:
    def __init__(self,team,pos):
        print("{0} rouleur initialised at {1}!".format(team,pos))
        self.name = "{0} rouleur".format(team)
        self.team = team
        self.position = pos
        self.activeDeck = card_picker.rouleur_deck
        self.faceDownDeck = []
        self.faceUpDeck = []
        self.usedCards = []
        self.finished = False
        stage.position_array[self.position[0]][self.position[1]] = 1

    def move(self):
        lastPos = self.position
        [pick,faceDown,faceUp] = card_picker.rouleur(self.activeDeck,self.faceUpDeck,self.usedCards)
        self.faceDownDeck = faceDown
        self.faceUpDeck = faceUp
        stage.position_array[self.position[0]][self.position[1]] = 0
        
        i = pick
        moved = False
        while i > 0:
            row = stage.position_array[self.position[0]+i]

            j = 0
            while j < len(row):
                index = row[j]
                if index != 0:
                    j += 1
                
                else:
                    self.position = (self.position[0]+i, j)
                    stage.position_array[self.position[0]][self.position[1]] = 1

                    tileName = stage.attributes()[self.position[0]][0]
                    if "finish" in tileName:
                        self.finished = True

                    moved = True
                    print("{0} rouleur is taking their turn, moving to {1}; they drew {2} and moved {3}".format(self.team,self.position,pick,self.position[0]-lastPos[0]))
                    break
            
            if self.finished == True:
                print("{0} rouleur has finished the race!".format(self.team))

            if moved == True:
                break
            
            else:
                i -= 1

print(stage.position_array)
greenRouleur = rouleur("green",(4,0))
redRouleur = rouleur("red",(4,1))
pinkRouleur = rouleur("pink",(3,0))
blackRouleur = rouleur("black",(3,1))
whiteRouleur = rouleur("white",(2,0))
blueRouleur = rouleur("blue",(2,1))
print(stage.position_array)
greenRouleur.move()
redRouleur.move()
pinkRouleur.move()
blackRouleur.move()
whiteRouleur.move()
blueRouleur.move()
print(stage.position_array)