import bge
from random import choice, randint
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

class Game():
	lista = []
	def atualizar_dashboard(self):
		if own['tmp2'] > 5 and own['tmp2'] <= 5.05:
			obj['dash_c']['indicador'] = randint(0, 100)
		if own['tmp2'] <= 5:
			pass
		else:
			own['tmp2']	 = 0
	def graficos_s(self):
		ep = obj['Empty_Plotador']
		lista = [[0,0], [1,1], [2,3], [3, 1], [4,2], [5,5]]
		for k in lista:
			
			ep.localPosition = [3.97853 + k[0]*1.5, 2.05544, 7.01727 +  1.5*k[1]]
			v0 = scn.addObject('v_inicio', ep)
			#v1 = scn.addObject('v_inicio', )
			v = scn.addObject('vetor', ep)

	def iniciar(self):
		print('Game iniciando...')

		

		if own['tmp1'] >= 0 and own['tmp1'] < 0.75:
			obj['txt_titulo']['Text'] = 1
		elif own['tmp1'] >= 0.75 and own['tmp1'] <= 1.5:
			obj['txt_titulo']['Text'] = 0	

		else:
			txt = choice(['sistemas', 'cursos','conteudo','multimedia','tecnologia','produtos', 'servicos'])
			if txt not in self.lista:
				self.lista.append(txt)
				obj['txt_marca2']['Text'] = txt	
			if len(self.lista) >= 7:
				self.lista = []		
			else:
				self.lista = []
				self.lista.insert(0, 'multimedia')							
							
			own['tmp1'] = 0	
		print(len(self.lista))
		print(self.lista)			
		#print(own['tmp1'])

def run():
	g = Game()
	g.iniciar()
	g.atualizar_dashboard()
	g.graficos_s()