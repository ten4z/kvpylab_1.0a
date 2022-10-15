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
		text: "Listar pares."	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDBoxLayout:
		orientation: "horizontal"
		spacing: 5
		padding: 5
		MDRaisedButton:
			text: "Listar"	
			on_press: app.listar()
		MDRaisedButton:
			text: "Sair"	
			on_press: app.stop()
		"""
class ListarPares(MDApp):	
	lista = []
	soma = 0
	def listar(self):
		self.root.lbl_saida.text  = ""	
		for n in range(0,10):
			if n % 2 == 0:
				self.root.lbl_saida.text += str(n) + ", "	
	def sair(self):
		MDApp.close()
	def build(self):
		MDApp.title = "Algoritmo 16"
		return Builder.load_string(kv)
if __name__ == "__main__":
	ListarPares().run()