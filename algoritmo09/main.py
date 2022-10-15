from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	num1: num1
	num2: num2
	num3: num3	
	MDLabel:
		text: "Verificar números."		
	MDTextField:
		id: num1
		hint_text: "Informe o primeiro número:"	
	MDTextField:
		id: num2
		hint_text: "Informe o segundo número:"	
	MDTextField:
		id: num3
		hint_text: "Informe o terceiro número:"			
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Verificar"	
		on_press: app.verificar(num1.text, num2.text, num3.text)	
"""
class Numeros(MDApp):
	def verificar(self, num1, num2, num3):
		try:
			lista = [int(num1),int(num2),int(num3)]
			nmax = max(lista)
			nmin = min(lista)
			nint = 0
			for n  in lista:
				if n != nmax and n != nmin:
					nint = n
			self.root.ids.lbl_saida.text = "menor número: " + str(nmin) +"\n"
			self.root.ids.lbl_saida.text += "maior número: " + str(nmax) +"\n"
			self.root.ids.lbl_saida.text += "número intermediário: " + str(nint)
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 09"
		return Builder.load_string(kv)
if __name__ == "__main__":
	Numeros().run()