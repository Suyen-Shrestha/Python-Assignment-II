class SuperMario:

    def __init__(self, playername, color):
        self.playername = playername
        self.color = color
        print('Hello! It\'s me Mario!!')



    def get_playerdetails(self):
        print('Your player details: \n')
        print(f'PlayerName: {self.playername}')
        print(f'MarioColor: {self.color}')


    def action(self,action):
        move = input("""Enter a move you want your mario to make:\n
                        'J' for jump
                        'D' for doublejump
                        'L' for moving left
                        'R' for moving right
                        'RL' for running left
                        'RR' for running right """)
        if move in ("L","R"):
            self.walk(move)
        elif move in ("J","D"):
            if move == 'J':
                self.jump()
            else:
                self.double_jump()    
        if move in ("RL","RR"):
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

        print('Yippee!! Your Mario just duble jumped!!')


    def run(self,direction):
        if direction == 'RL':
            print(f'Mario "{self.playername}" Running left...')
        else:
            print(f'Mario "{self.playername}" Running right...')                  



name = input('Enter player name: ')
color = input('Enter your mario\'s color: ')
        
mario1 = SuperMario(name,color)
mario1.get_playerdetails()

option = input('Please enter an action you want your mario to perform next: ')
mario1.action(option)


