from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class BGTCGame(FloatLayout):
	player1 = ObjectProperty(None)
	#all the buttons, is this necessary?
	upper_left = ObjectProperty(None)
	upper_midleft = ObjectProperty(None)
	upper_center = ObjectProperty(None)
	upper_midright = ObjectProperty(None)
	upper_right = ObjectProperty(None)
	midupper_left = ObjectProperty(None)
	midupper_right = ObjectProperty(None)
	midlower_left = ObjectProperty(None)
	midlower_right = ObjectProperty(None)
	lower_left = ObjectProperty(None)
	lower_midleft = ObjectProperty(None)
	lower_center = ObjectProperty(None)
	lower_midright = ObjectProperty(None)
	lower_right = ObjectProperty(None)
	
	def start(self, vel=(0,0)):
		self.player1.size = (50, 50)
		self.player1.center = self.center
		self.player1.velocity = vel

class Player(Widget):
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	

	def move(self):
		self.pos = Vector(*self.velocity) + self.pos

class BGTCApp(App):
	def build(self):
		game = BGTCGame()
		game.start()
		return game

if __name__ == '__main__':
	BGTCApp().run()


