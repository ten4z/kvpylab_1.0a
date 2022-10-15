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
		text: "Contagem decrescente."	
	MDTextField:
		id: numero
		hint_text: "Informe um número:"
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDBoxLayout:
		orientation: "horizontal"
		spacing: 5
		padding: 5
		MDRaisedButton:
			text: "Exibir"	
			on_press: app.listar(numero.text)	
		MDRaisedButton:
			text: "Sair"	
			on_press: app.stop()	
		"""
class ListaDecrescente(MDApp):	
	def listar(self, numero):		
		numero = int(numero)
		self.root.lbl_saida.text = ""
		for k in range(0,numero):
			self.root.lbl_saida.text += str(numero - k) + ", "
			print(numero - k)
	def sair(self):
		MDApp.close()
	def build(self):
		MDApp.title = "Algoritmo 15"
		return Builder.load_string(kv)
if __name__ == "__main__":
	ListaDecrescente().run()