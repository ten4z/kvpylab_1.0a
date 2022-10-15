from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	num: num
	MDLabel:
		text: "Verificar se par ou ímpar."		
	MDTextField:
		id: num
		hint_text: "Informe um número:"	
		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Verificar"	
		on_press: app.verificar(num.text)	
"""
class ParouImpar(MDApp):
	def verificar(self, numero):
		try:
			if int(numero) % 2 == 0:
				self.root.ids.lbl_saida.text = "O número " + numero + " é par"
			elif int(numero) % 2 == 1:
				self.root.ids.lbl_saida.text = "O número " + numero + " é ímpar"
			elif int(numero) == 0:
				self.root.ids.lbl_saida.text = "O número é zero"
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 10"
		return Builder.load_string(kv)
if __name__ == "__main__":
	ParouImpar().run()