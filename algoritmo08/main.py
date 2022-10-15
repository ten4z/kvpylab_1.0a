from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	num1: num1
	num2: num2	
	MDLabel:
		text: "Informe dois números."		
	MDTextField:
		id: num1
		hint_text: "Informe o primeiro número:"	
	MDTextField:
		id: num2
		hint_text: "Informe o segundo número:"		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Verificar"	
		on_press: app.verificar(num1.text, num2.text)	
"""
class DoisNumeros(MDApp):
	def verificar(self, num1, num2):
		try:
			if int(num1) > int(num2):
				self.root.ids.lbl_saida.text = "O número " + num1 + " é maior que " + num2
				toast("maior")
			if int(num1) < int(num2):
				self.root.ids.lbl_saida.text = "O número " + num1 + " é menor que " + num2
				toast("menor")
			if int(num1) == int(num2):
				self.root.ids.lbl_saida.text = "O número " + num1 + " é igual a " + num2				
				toast("igual")
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 08"
		return Builder.load_string(kv)
if __name__ == "__main__":
	DoisNumeros().run()