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
	MDLabel:
		text: "Listar nome de usuário."	
	MDTextField:
		id: usuario
		hint_text: "Nome de usuário:"	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Listar"	
		on_press: app.listar(usuario.text)	
"""
class ListarUsuario(MDApp):	
	def listar(self, usuario):		
		self.root.ids.lbl_saida.text = ""
		for n in range(0,5):			
			self.root.ids.lbl_saida.text += usuario + "\n"
			
	def build(self):
		MDApp.title = "Algoritmo 13"
		return Builder.load_string(kv)
if __name__ == "__main__":
	ListarUsuario().run()