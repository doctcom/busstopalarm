import kivy
from kivy.app import App
from kivy.uix.button import Button
class BusstopalarmApp(App):
	def build(self):
		return Button(text="welcome")

if __name__=='__main__':
	BusstopalarmApp().run()
