from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	nota1: nota1
	nota2: nota2
	MDLabel:
		text: "Verificar média de aluno."		
	MDTextField:
		id: nota1
		hint_text: "Informe a primeira nota:"	
	MDTextField:
		id: nota2
		hint_text: "Informe a segunda nota:"		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.verificar(nota1.text, nota2.text)	
"""
class NotaAluno(MDApp):
	def verificar(self, nota1, nota2):
		try:
			media = (float(nota1) +  float(nota2) )/ 2
			if media >= 7:
				toast("Aprovado")
				self.root.ids.lbl_saida.text = "média = " + str(media) + " aprovado"
			elif media > 4:
				toast("Prova Final")
				self.root.ids.lbl_saida.text = "média = " + str(media) + " prova final"
			else:
				toast("Reprovado")
				self.root.ids.lbl_saida.text = "média = " + str(media) + " reprovado"
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 06"
		return Builder.load_string(kv)		
if __name__ == "__main__":
	NotaAluno().run()