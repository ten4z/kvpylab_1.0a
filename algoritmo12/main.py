from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	MDLabel:
		text: "Listar números."		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Listar"	
		on_press: app.listar()	
"""
class Contar50(MDApp):	
	def listar(self):
		self.root.ids.lbl_saida.text = ""
		for n in range(1,51):			
			if n < 10:
				self.root.ids.lbl_saida.text += "0" + str(n) + ", "
			else: 
				self.root.ids.lbl_saida.text += str(n) + ", "
			if n % 5 == 0:
				self.root.ids.lbl_saida.text += "\n" 
	def build(self):
		MDApp.title = "Algoritmo 12"
		return Builder.load_string(kv)
if __name__ == "__main__":
	Contar50().run()