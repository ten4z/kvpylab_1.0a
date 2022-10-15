from kivymd.app import MDApp
from kivy.lang import Builder
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida
	n1: n1
	n2: n2
	MDLabel:
		text: "As quatro Operações de Matemática."		
	MDTextField:
		id: n1
		hint_text: "Primeiro Número:"		
	MDTextField:
		id: n2
		hint_text: "Segundo Número:"	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.opmath(n1.text, n2.text)	
"""
class OpMath(MDApp):
	def opmath(self, a, b):
		try:
			if a != "" and b != "":
				if int(b) != 0:
					self.root.ids.lbl_saida.text = a + " + " + b + " = " + str(int(a)+int(b))  +"\n"
					self.root.ids.lbl_saida.text += a + " - " + b + " = " + str(int(a)-int(b)) +"\n"
					self.root.ids.lbl_saida.text += a + " * " + b + " = " + str(int(a)*int(b)) +"\n"
					self.root.ids.lbl_saida.text += a + " / " + b + " = " + str(round(int(a)/int(b),2))
				else:
					self.root.ids.lbl_saida.text = a + " + " + b + " = "  + str(int(a)+int(b)) +"\n"
					self.root.ids.lbl_saida.text += a + " - " + b + " = " + str(int(a)-int(b)) +"\n"
					self.root.ids.lbl_saida.text += a + " * " + b + " = " + str(round(int(a)*int(b), 2)) +"\n"
					self.root.ids.lbl_saida.text += "Impossível divir por zero."
			else:
				self.root.ids.lbl_saida.text = "Por favor apenas valores numéricos."
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 02"
		return Builder.load_string(kv)
if __name__ == "__main__":
	OpMath().run()