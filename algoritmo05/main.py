from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	numero: numero
	MDLabel:
		text: "Verificar se o número é positivo."		
	MDTextField:
		id: numero
		hint_text: "Informe um número:"		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.verificar(numero.text)	
"""
class Positivo(MDApp):
	def verificar(self, numero):
		try:
			numero = float(numero)
			if  numero > 0: 
				self.root.ids.lbl_saida.text = "O número " + str(numero) + " é positivo"
				toast("É positivo")				
			else:
				self.root.ids.lbl_saida.text = "O número " + str(numero) + " não é positivo"
				toast("Não é positivo")				

		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 05"
		return Builder.load_string(kv)		
if __name__ == "__main__":
	Positivo().run()