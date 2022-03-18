import kivy 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random as rd

tg = 0
win = 0
lose = 0
draw = 0  

class RPS(BoxLayout):
  def __init__(self,**kwargs):
    super(RPS,self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.padding = 20
    self.spacing = 20
    self.add_widget(Label(text='Rock Paper Scissors',font_size=40,size_hint=(.5,.03),pos_hint={'center_x':.5}))
    
    self.add_widget(Label(text='Enter your option below\n ROCK PAPER SCISSORS',font_size=40,size_hint=(.5,.02),pos_hint={'center_x':.5}))
    self.user=TextInput(multiline=False,size_hint_x=None,width=400,size_hint_y=None,height=50,pos_hint={'center_x':.5})
    self.add_widget(self.user)
    self.press=Button(text='Play',font_size=40,background_normal='',background_color=(0,0,1,1),size_hint=(.5,.01),pos_hint={'center_x':.5})
    self.press.bind(on_press=self.AI)
    self.add_widget(self.press)
    self.Declare=Label(text='',size_hint=(.5,0),pos_hint={'center_x':.5})
    self.add_widget(self.Declare)
    self.Board=Label(text='SCORE BOARD\nTOTAL GAME:0\nWIN:0\nDRAW:0\nLOSE:0',size_hint=(.5,.05),pos_hint={'center_x':.5})
    self.add_widget(self.Board)
    
    
  def AI(self,instance):
    user = (self.user.text).lower()
    declare = self.Declare
    board = self.Board
    global tg , win , draw, lose
        
    AI_list = ['rock','paper','scissors']
    AI = rd.choice(AI_list)
    if user == AI:
      tg += 1
      declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nBoth chose {AI}' 
      draw += 1
      board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
    elif user == 'rock':
      tg += 1
      if AI =='paper':
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nAI win'
        lose += 1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
      else:
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nYou win'
        win += 1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
    elif user == 'paper':
      tg += 1
      if AI == 'scissors':
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nAI win'
        lose += 1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
      else:
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nYou win'
        win += 1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
    elif user == 'scissors':
      tg += 1
      if AI == 'rock':
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nAI win'
        lose += 1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'
      else:
        declare.text = f'AI chose:{AI}\nUser chose:{self.user.text}\nYou win'
        win +=1
        board.text = f'SCORE BOARD\nTOTAL GAME:{tg}\nWIN:{win}\nDRAW:{draw}\nLOSE:{lose}'

    self.user.text = ''
    

class RockApp(App):
  def build(self):
    return RPS()
    
if __name__ == '__main__':
  RockApp().run()
