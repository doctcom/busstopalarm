import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.slider import Slider


b=BoxLayout(orientation="vertical")
dropdown=DropDown()
dropdown2=DropDown()

for index in range(10):
	btn=Button(text="From stop %i" %index, size_hint_y=None, height=40, background_color=(0,0,0,1))
	
	dropdown.add_widget(btn)
	btn.bind(on_release=lambda btn:dropdown.select(btn.text))
	btn2=Button(text="To stop %i" %index, size_hint_y=None, height=40, background_color=(0,0,0,1))
	btn2.bind(on_release=lambda btn2:dropdown2.select(btn2.text))

	dropdown2.add_widget(btn2)
mainbtn=Button(text="From", size_hint_y=0.33, background_color=(0,0,0,0))
mainbtn.bind (on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x:setattr(mainbtn, "text",x))
mainbtn2=Button(text="To", size_hint_y=0.33, background_color=(0,0,0,0))
mainbtn2.bind(on_release=dropdown2.open)
dropdown2.bind(on_select=lambda instance, x:setattr(mainbtn2, "text", x))

w0=Widget()
w1=Widget()
w2=Widget()
w3=Widget()
l1=Label(text="Alarm Before Distance:")
l2=Label(text="Alarm Before Time:")

s1=Slider(min=1, max=5, value=1, value_track=True, value_track_color=[0,1,0,1])
s2=Slider(min=1, max=30, value=5, value_track=True, value_track_color=[0,1,0,1])

ls1=Label(text="%s kms"% int(s1.value))
ls2=Label(text="%s mins"% int(s2.value))
def OnSlider1ValueChange(instance, value):
	ls1.text=str(value)
s1.bind(value=OnSlider1ValueChange)
def OnSlider2ValueChange(instance, value):
	ls2.text=str(value)
s2.bind(value=OnSlider2ValueChange)


b.add_widget(w0)
b.add_widget(mainbtn)

b.add_widget(mainbtn2)
b.add_widget(w3)
b.add_widget(l1)
b.add_widget(s1)
b.add_widget(ls1)
b.add_widget(l2)
b.add_widget(s2)
b.add_widget(ls2)
b.add_widget(w2)


class BusstopalarmApp(App):
	def build(self):
		return b 

if __name__=='__main__':
	BusstopalarmApp().run()
