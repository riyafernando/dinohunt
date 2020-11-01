import random
### Die class that we previously wrote ###
class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value
'''
### end Die class ###

class DinoDie(Die):
    implements one die for Dino Hunt
    ### you need to add the code ###

class DinoPlayer:
    implements a player of Dino Hunt
    ### you need to add the code ###

def play_dino_hunt(numPlayers,numRounds):
    play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player
    ### you need to add the code ###
    '''
class DinoDie(Die):

    def __init__(self, color):
        '''Makes one die for Dino Hunt'''
        Die.__init__(self)
        self.color = color
        self.sides = []
        if self.color == 'green':
            self.sides += ['dino']*3 + ['leaf']*2 + ['foot']
        elif self.color == 'yellow':
            self.sides += ['dino'] * 2 + ['leaf'] * 2 + ['foot'] * 2
        elif self.color == 'red':
            self.sides += ['dino'] + ['leaf'] * 2 + ['foot'] * 3

    def __str__(self):
        return 'A ' + self.color + ' die with a ' + str(self.roll()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = str(random.choice(self.sides))
        return self.top



class DinoPlayer:
    '''Implements one player of Dino Hunt'''
    def __init__(self, playername):
        self.dice_list = []
        self.dice_green = DinoDie('green')
        self.dice_yellow = DinoDie('yellow')
        self.dice_red = DinoDie('red')
        self.name = playername
        self.score = 0
        self.dice_left = self.dice_list
        self.dice_rolled = []
        self.dinos = 0
        self.feet = 0
        self.number_dice_left = 0
        self.number_dice_rolled = 0

    def __str__(self):
        '''return player's name and score'''
        return self.name + ' has a score of ' + str(self.score)

    def make_dice(self):
        '''Makes all 13 dice and put all objects in a list'''
        for i in range(0, 6):
            self.dice_list += [self.dice_green]
        for i in range(0, 4):
            self.dice_list += [self.dice_yellow]
        for i in range(0, 3):
            self.dice_list += [self.dice_red]
        random.shuffle(self.dice_list)
        self.dice_left = self.dice_list

    def find_colors(self):
        green = 0
        yellow = 0
        red = 0
        for i in self.dice_list:
            if i.color == 'green':
                green += 1
            if i.color == 'yellow':
                yellow += 1
            if i.color == 'red':
                red += 1
        return str(green) + " green  " + str(yellow) + " yellow  " + str(red) + " red "

    def take_turn(self):
        '''Make 13 dice, roll 3 dice, set aside, ask player if they want to roll again, exit if 3 feet'''

        self.make_dice()
        self.number_dice_left = len(self.dice_left)
        self.number_dice_rolled = len(self.dice_rolled)
        print(self.name + ", it's your turn!")
        print('You have ' + str(self.number_dice_left) + ' dice left.')
        add_score = 0


        while True:

            raw_input("Press enter to select dice and roll.")

            if len(self.dice_left) == 1:
                y = 1
            elif len(self.dice_left) == 2:
                y = 2
            else:
                y = 3

            for i in range(0, y):
                x = random.choice(self.dice_left)


                roll = x.roll()
                if roll == 'leaf':
                    print('        A ' + x.color + ' Dino Die with a ' + x.top + ' on top.')
                elif roll == 'dino':
                    self.dinos += 1
                    print('        A ' + x.color + ' Dino Die with a ' + x.top + ' on top.')
                    self.dice_rolled += [x]
                    self.dice_left = self.dice_left[:self.dice_left.index(x)] + \
                                     self.dice_left[self.dice_left.index(x) + 1:]
                elif roll == 'foot':
                    self.feet += 1
                    print('        A ' + x.color + ' Dino Die with a ' + x.top + ' on top.')
                    self.dice_rolled += [x]
                    self.dice_left = self.dice_left[:self.dice_left.index(x)] + \
                                     self.dice_left[self.dice_left.index(x) + 1:]


            if self.feet >= 3:
                print("Too bad -- You got stomped!")
                add_score = 0
                break
            elif len(self.dice_left) == 0:
                print('This turn so far: ' + str(self.dinos) + ' dinos and ' + str(self.feet) + ' feet')
                add_score += self.dinos
                print('You have ' + str(len(self.dice_left)) + ' dice left.')
                print("Aw, you're out of dice!")
                self.score += add_score
                break
            else:
                print('This turn so far: ' + str(self.dinos) + ' dinos and ' + str(self.feet) + ' feet')
                add_score += self.dinos
                print('You have ' + str(len(self.dice_left)) + ' dice left.')
                yes_no = raw_input("Do you want to roll again? (y/n) ")
                if yes_no == 'n':
                    self.score += add_score
                    break
    def reset(self):
        self.dice_list = []
        self.dice_left = self.dice_list
        self.dice_rolled = []
        self.dinos = 0
        self.feet = 0
        self.number_dice_left = 0
        self.number_dice_rolled = 0


def play_dino_hunt(numPlayers, numRounds):
    '''plays a game of Dino Hunt'''
    playerlist = []
    for i in range(1, numPlayers+1):
        playername = raw_input("Player " + str(i) + ", enter your name:")
        Player = DinoPlayer(playername)
        playerlist += [Player]
    for y in range(0, numRounds):
        print("ROUND " + str(y+1))
        for player in playerlist:
            player.take_turn()
            player.reset()

    z = 0
    if playerlist[0].score == playerlist[1].score:
        print("It's a tie! Congratulations!")

    for player in playerlist:
        if player.score > y:
            y = player.score
            x = player.name
    print( x + ' has won with a score of ' + str(y) + '!')

play_dino_hunt(2,2)