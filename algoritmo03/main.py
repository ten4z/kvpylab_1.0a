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
	MDLabel:
		text: "Retornar o nome do usuário."		
	MDTextField:
		id: nome
		hint_text: "Informe seu nome:"			
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.exibir_nome(nome.text)	
"""
class ExibirNome(MDApp):
	def exibir_nome(self, nome):
		try:
			self.root.ids.lbl_saida.text = "O seu nome é: " + nome
			toast("Olá, seja bem vindo " + nome + "!" )
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 03"
		return Builder.load_string(kv)

if __name__ == "__main__":
	ExibirNome().run()