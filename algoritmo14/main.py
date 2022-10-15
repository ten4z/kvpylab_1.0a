from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	nome: nome
	cpf: cpf
	MDLabel:
		text: "Listar nome de usuário."	
	MDTextField:
		id: nome
		hint_text: "Nome de usuário:"	
	MDTextField:
		id: cpf
		hint_text: "CPF de usuário:"	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDBoxLayout:
		orientation: "horizontal"
		spacing: 5
		padding: 5
		MDRaisedButton:
			text: "Exibir"	
			on_press: app.listar(nome.text, cpf.text)	
		MDRaisedButton:
			text: "Sair"	
			on_press: app.stop()	
		"""
class DetalhesUsuario(MDApp):	
	def listar(self, nome, cpf):		
		self.root.ids.lbl_saida.text = "Seu nome: " + nome + "\nSeu CPF: "+ cpf
	def sair(self):
		MDApp.close()
	def build(self):
		MDApp.title = "Algoritmo 14"
		return Builder.load_string(kv)
if __name__ == "__main__":
	DetalhesUsuario().run()