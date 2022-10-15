from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	usuario: usuario
	senha: senha
	MDLabel:
		text: "Login de usuários."		
	MDTextField:
		id: usuario
		hint_text: "Usuário:"	
	MDTextField:
		id: senha
		hint_text: "Senha:"		
		password: True		
		password_mask: "*"
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Verificar"	
		on_press: app.verificar(usuario.text, senha.text)	
"""
class Login(MDApp):
	data = ["fulano", "abc123"]
	def verificar(self, us, pw):
		try:
			print(us, pw)
			if (us == self.data[0]) and (pw == self.data[1]):
				self.root.ids.lbl_saida.text = "Login efetuado com sucesso."
				toast("Redirecionando para a home page...")
			else:
				self.root.ids.lbl_saida.text = "Login inválido"
				toast("Usuário ou senha incorretos.")
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 11"
		return Builder.load_string(kv)
if __name__ == "__main__":
	Login().run()