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
        self.activeDeck = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
        self.faceDownDeck = []
        self.faceUpDeck = []
        self.usedCards = []
        self.finished = False
        stage.position_array[self.position[0]][self.position[1]] = 1

    def move(self):
        lastPos = self.position
        [self.pick,self.faceDownDeck,self.faceUpDeck] = card_picker.rouleur(self.activeDeck,self.faceUpDeck,self.usedCards)
        stage.position_array[self.position[0]][self.position[1]] = 0
        
        i = self.pick
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
                    print("{0} rouleur is taking their turn, moving to {1}; they drew {2} and moved {3}".format(self.team,self.position,self.pick,self.position[0]-lastPos[0]))
                    break
            
            if self.finished == True:
                print("{0} rouleur has finished the race!".format(self.team))

            if moved == True:
                break
            
            else:
                i -= 1

class sprinteur:
    def __init__(self,team,pos):
        print("{0} sprinteur initialised at {1}!".format(team,pos))
        self.name = "{0} sprinteur".format(team)
        self.team = team
        self.position = pos
        self.activeDeck = [2,2,2,3,3,3,4,4,4,5,5,5,5,9,9,9]
        self.faceDownDeck = []
        self.faceUpDeck = []
        self.usedCards = []
        self.finished = False
        stage.position_array[self.position[0]][self.position[1]] = 1

    def move(self):
        lastPos = self.position
        [self.pick,self.faceDownDeck,self.faceUpDeck] = card_picker.rouleur(self.activeDeck,self.faceUpDeck,self.usedCards)
        stage.position_array[self.position[0]][self.position[1]] = 0
        
        i = self.pick
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
                    print("{0} sprinteur is taking their turn, moving to {1}; they drew {2} and moved {3}".format(self.team,self.position,self.pick,self.position[0]-lastPos[0]))
                    break
            
            if self.finished == True:
                print("{0} sprinteur has finished the race!".format(self.team))

            if moved == True:
                break
            
            else:
                i -= 1

def slipStream(racers):
    for r in racers:
        print("{0}: {1}, {2}".format(r.name,r.position,stage.route[r.position[0]].slipstream))
    row = 0
    while row < stage.length-2:
        thisRow = stage.position_array[row]
        nextRow = stage.position_array[row+1]
        followingRow = stage.position_array[row+2]
        
        if 1 not in thisRow:
            row += 1
            continue

        else:
            if (1 in followingRow) and (1 not in nextRow) and (stage.route[row].slipstream == True):
                i = 0
                while i < len(nextRow):
                    if stage.position_array[row][i] == 1:
                        stage.position_array[row][i] = 0
                        for r in racers:
                            if r.position == (row,i):
                                r.position = (row+1, i)
                                print("{0} slipstreamed to {1}!".format(r.name,r.position))

                    i+=1

                #Should only run if player still left in row after slipstream
                if 1 in stage.position_array[row]:
                    for r in racers:
                        if r.position[0] == row:
                            r.position = (row, 0)

        row += 1
    
    i = 0
    while i < stage.length:
        row = stage.position_array[i]

        j = 0
        while j < len(row):
            stage.position_array[i][j] = 0
            j += 1
        i += 1
    
    for r in racers:
        place = r.position
        stage.position_array[place[0]][place[1]] = 1

def nameArray():
    placeholder = stage.position_array
    for r in racers:
        placeholder[r.position[0]][r.position[1]] = r.name
    return placeholder

greenRouleur = rouleur("green",(4,0))
greenSprinteur = sprinteur("green",(4,1))
redRouleur = rouleur("red",(3,0))
redSprinteur = sprinteur("red",(3,1))
pinkRouleur = rouleur("pink",(2,0))
pinkSprinteur = sprinteur("pink",(2,1))
blackRouleur = rouleur("black",(1,0))
blackSprinteur = sprinteur("black",(1,1))
whiteRouleur = rouleur("white",(0,0))
whiteSprinteur = sprinteur("white",(0,1))
racers = [greenRouleur, greenSprinteur, redRouleur, redSprinteur, blackRouleur, blackSprinteur, pinkRouleur, pinkSprinteur, whiteRouleur, whiteSprinteur]

# Moving in order
order = []

for racer in racers:
    order.append([racer, racer.position])

order.sort(key=lambda x: x[1][1])
order.sort(key=lambda x: x[1][0], reverse=True)

for i in order:
    i[0].move()

print(stage.position_array)
nameArray()

s = True
while s == True:
    before = stage.position_array
    slipStream(racers)
    slipStream(racers)
    after = stage.position_array
    #Unfinished
