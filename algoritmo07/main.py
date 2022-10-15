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
	idade: idade
	
	MDLabel:
		text: "Nome e idade de funcionário."		
	MDTextField:
		id: nome
		hint_text: "Informe o nome do funcionário:"	
	MDTextField:
		id: idade
		hint_text: "Informe a idade do funcionário:"		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.verificar(nome.text, idade.text)	
"""
class Funcionario(MDApp):
	def verificar(self, nome, idade):
		try:
			if int(idade) > 17:
				self.root.ids.lbl_saida.text = "O funcionário " + nome + " é Efetivo."
				toast("Funcionário efetivo")
			else:
				self.root.ids.lbl_saida.text = "O funcionário " + nome + " é Estagiário."
				toast("Funcionário estagirário")
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 07"
		return Builder.load_string(kv)		
if __name__ == "__main__":
	Funcionario().run()