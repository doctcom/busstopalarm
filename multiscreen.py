import kivy
from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

kv='''
<MyScreenManager>:
	ScreenOne:
		name:"home"
	ScreenTwo:
		name:"beforetime"

	ScreenThree:
		name:"beforedist"
	ScreenFour:
		name:"finalscreen"
<ScreenOne>:
	BoxLayout:
		spacing:50
		orientation:"vertical"
		BoxLayout:
			gps_location:app.gps_location
			gps_status:app.gps_status
			Label:
				text:"Welcome to the app"
				font_size:18
			Label:
				text:app.gps_location
			Label:
				text:app.gps_status
			ToggleButton:
				text:'Start'if self.state=='normal'else 'Stop'
				on_state:app.gps.start() if self.state=='down'else app.gps.stop()
		BoxLayout:
			orientation:"vertical"
			Label:
				text:"Select bus stops"
				font_size:12
			Spinner:
				id:Spinner1
				text:"From"
				values:('stop1', 'stop2', 'stop3')
				size_hint_y:None

				height:40
				background_color:(0,0,0,0)
			Spinner:
				id:Spinner2
				text:"To"
				values:('stop1', 'stop2', 'stop3')
				background_color:(0,0,0,0)
				size_hint_y:None
				height:40
			Widget:
			Widget:
			Button:
				text:"Wake me up before a duration of:"
				size_hint_y:None
				height:40
				on_press:root.manager.current="beforetime"
			Button:
				text:"Wake me up before a distance of:"
				size_hint_y:None
				height:40
				on_press:root.manager.current="beforedist"
<ScreenTwo>:
	BoxLayout:
		orientation:"vertical"
		Slider:
			id:beforetimeslider
			min:5
			max:30
			value:5
			value_track:True
			value_track_color:[1,1,0,1]
		Button:
			text:"GO"
			size_hint_y:None
			height:40
			on_release:root.manager.current="finalscreen"
<ScreenThree>:
	BoxLayout:
		orientation:"vertical"
		Slider:
			id:beforedistslider
			min:5
			max:30
			value:5
			value_track:True
			value_track_color:[1,1,0,1]
		Button:
			text:"GO"
			size_hint_y:None
			height:40

			on_release:root.manager.current="finalscreen"
<ScreenFour>:
	BoxLayout:
		orientation:"vertical"	
		Label:
			text:"done"
'''


class ScreenOne(Screen):
	def whenspinnerchange(self,Spinner,text):
		Spinner=self.Spinner
		text=self.Spinner.text
		print("hello man")
class ScreenTwo(Screen):
	pass
class ScreenThree(Screen):
	pass
class ScreenFour(Screen):
	pass

class MyScreenManager(ScreenManager):
	pass


#comments start here
#what i would do
#get current gps location as a variable called as source
#take to bus stop gps location as a variable called as destination
#start a while/for loopp
#declare a variable time_reqd
#calculate time_reqd as time between source and destination
#inside loop, if time__reqd==5000ms:ring alarm
#else update source variable every 5000ms





def mainthread(func):
	def delayed_func(args, **kwargs):
		def callback_func(dt):
			func(args, **kwargs)
		Clock.schedule_once(callback_func, 0)
	return delayed_func

class BusstopalarmApp(App):
	
	gps_location=StringProperty()
	gps_status=StringProperty('click start to get GPS Location updates')

	def build(self):
		self.gps=gps
		try:
			self.gps.configure(on_location=self.on_location, on_status=self.on_status)
		except NotImplementedError:
			import traceback;traceback.print_exc()
			self.gps_status='gps is not included in ur platform'

	
		return Builder.load_string(kv)

	@mainthread
	def on_location(self, **kwargs):
		self.gps_location='\n'.join(['{}={}'.format(k,v) for k,v in kwargs.items()])
		
	@mainthread
	def on_status(self, stype, status):
		self.gps_status='type={}\n{}'.format(stype, status)	



if __name__=="__main__":
	BusstopalarmApp().run()
