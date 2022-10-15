from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:	
	orientation: "vertical"
	padding: 10
	spacing: 10
	lbl_saida: lbl_saida	
	txtnum: txtnum	
	MDLabel:
		text: "Somar dez números."	
	MDBoxLayout:
		orientation: "horizontal"
		padding: 5
		spacing: 5
		MDTextField:
			size_hint_x: 0.5
			id: txtnum
			hint_text: "Informe dez números"			
		MDRaisedButton:
			size_hint_x: 0.5
			text: "Adicionar"	
			on_press: app.listar(txtnum.text)		
	MDLabel:
		id: lbl_saida
		text: "Esperando interação..."	
	MDBoxLayout:
		orientation: "horizontal"
		spacing: 5
		padding: 5		
		MDRaisedButton:
			text: "Somar"	
			on_press: app.somar()	
		MDRaisedButton:
		    text: "Recomeçar"
		    on_press: app.reiniciar()
		MDRaisedButton:
			text: "Sair"	
			on_press: app.stop()
		"""
class SomarDez(MDApp):	
	lista = []
	soma = 0
	def listar(self, num):	
		try:	
			if len(self.lista) < 10:
				self.root.lbl_saida.text = "Pares: "
				self.lista.append(int(num)) 
				self.root.txtnum.text = ""
				self.root.lbl_saida.text = "Adicionado: " + num + " [" + str(len(self.lista)) + " de 10]"
				if len(self.lista) == 10:
					self.somar()			
		except:
			self.root.lbl_saida.text = "Por favor apenas números."
	def somar(self):
		for k in self.lista:
			self.soma += int(k) 
		self.root.lbl_saida.text = "Números: " + str(self.lista) + "\n"
		self.root.lbl_saida.text += "Soma total: " + str(self.soma)
	def reiniciar(self):
		self.lista = []
		self.soma = 0
		self.root.txtnum.text = ""
		self.root.lbl_saida.text = ""
	def sair(self):
		MDApp.close()
	def build(self):
		MDApp.title = "Algoritmo 17"
		return Builder.load_string(kv)
if __name__ == "__main__":
	SomarDez().run()