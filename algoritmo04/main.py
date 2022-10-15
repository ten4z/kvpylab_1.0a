from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida
	valor: valor	
	diasat: diasat
	jurosdia: jurosdia
	MDLabel:
		text: "Retornar cálculo de conta."		
	MDTextField:
		id: valor
		hint_text: "Valor da dívida:"			
	MDTextField:
		id: diasat
		hint_text: "Dias de atrazo:"
	MDTextField:
		id: jurosdia
		hint_text: "Juros ao dia:"	
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDRaisedButton:
		text: "Calcular"	
		on_press: app.calcular(valor.text, jurosdia.text, diasat.text)	
"""
class Pagamentos(MDApp):
	def calcular(self, valor, jurosdia, diasat):
		try:
			valor_final = float(valor) + float(jurosdia)*int(diasat)
			self.root.ids.lbl_saida.text = "O valor total a pagar é: " + str(valor_final)
			toast("O valor total a pagar é: " + str(valor_final))
		except:	
			self.root.ids.lbl_saida.text = "Revise as entradas informadas."
	def build(self):
		MDApp.title = "Algoritmo 04"
		return Builder.load_string(kv)
if __name__ == "__main__":
	Pagamentos().run()