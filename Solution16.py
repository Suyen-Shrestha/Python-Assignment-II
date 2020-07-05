class SuperMario:

    def __init__(self, playername, color):
        self.playername = playername
        self.color = color
        print('\nHello! It\'s me Mario!!\n')



    def get_playerdetails(self):
        print('Your player details: ')
        print(f'PlayerName: {self.playername}')
        print(f'MarioColor: {self.color}\n')


    def action(self):
        move = input("""Enter a move you want your mario to make:\n
                        'J' for jump
                        'D' for doublejump
                        'L' for moving left
                        'R' for moving right
                        'RL' for running left
                        'RR' for running right \n""").upper()
        if move in ("L","R"):
            self.walk(move)
        elif move in ("J","D"):
            if move == 'J':
                self.jump()
            else:
                self.double_jump()    
        elif move in ("RL","RR"):
            self.run(move)
        else:
            print('Invalid action selected!')                            



    def walk(self,direction):
        if direction == 'L':
            print(f'Mario "{self.playername}" Walking left...')
        else:
            print(f'Mario "{self.playername}" Walking right...')    


    def jump(self):
        print('Yippee!! Your Mario just jumped!!')
        

    def double_jump(self):

        print('Yippee!! Your Mario just double jumped!!')


    def run(self,direction):
        if direction == 'RL':
            print(f'Mario "{self.playername}" Running left...')
        else:
            print(f'Mario "{self.playername}" Running right...')                  


exit = False

name = input('Enter player name: ')
color = input('Enter your mario\'s color: ')
        
mario1 = SuperMario(name,color)
mario1.get_playerdetails()


while exit == False:
    print('Do you wanna continue playing?(Y/N)')
    yesno = input().upper()

    if yesno == 'Y':
        mario1.action()
    else:
        exit = True