from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida
	n1: n1
	n2: n2
	MDLabel:
		text: "Informe dois números para fazer a soma."		
	MDTextField:
		id: n1
		hint_text: "Primeiro Número"		
	MDTextField:
		id: n2
		hint_text: "Segundo Número"	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.somar(n1.text, n2.text)	
"""
 
class Somare(MDApp):
	def somar(self, a, b):
		if a != "" and b != "":
			self.root.ids.lbl_saida.text = str(int(a)+int(b))
		else:
			self.root.ids.lbl_saida.text = "Por favor apenas valores numéricos."
	def build(self):
		MDApp.title = "Algoritmo 01"
		return Builder.load_string(kv)

if __name__ == "__main__":
	Somare().run()