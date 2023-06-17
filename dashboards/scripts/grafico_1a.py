import bge
from random import choice, randint
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
scl = bge.logic.getSceneList()
obj = scn.objects
class Game():
	lista = []
	tempo = 1.0
	pontos_id = 0
	def atualizar_dashboard(self):
		if own['tmp2'] > self.tempo and own['tmp2'] <= self.tempo + 0.05:
			self.graficos_s()
		if own['tmp2'] <= self.tempo:
			pass
		else:
			own['tmp2']	 = 0
	
	def graficos_s(self):
		ep = obj['Empty_Plotador']
		eo = obj['Empty_Origem']
		em = obj['Empty_Media']		
		self.lista = [0]
		self.lista.pop(0)
		py = randint(0,5)
		self.lista.append(py)
		ep.localPosition = [18.615, 2.0, 6.99416 + self.lista[0]]
		if own['pontos'] % 2 == 1:
			own['pontos'] += 1
			v1 = scn.addObject('pt_inicio', ep, 985)
			v1['id'] = own['pontos']
			v1.setParent(eo)
		else:
			own['pontos'] += 1
			v0 = scn.addObject('pt_fim', ep, 985)
			v0['id'] = own['pontos']
			v0.setParent(eo)
		for ob in obj:
			if 'id' in ob:
				if ob['id'] == own['pontos']:
					fim = ob
				if ob['id'] == own['pontos'] - 1:
					inicio = ob
				if 'inicio' in locals() and 'fim' in locals():
					#em.localPosition = (fim.localPosition + inicio.localPosition)/2
					em.localPosition.x = (fim.localPosition.x + inicio.localPosition.x + 18.615)/2
					em.localPosition.y = (fim.localPosition.y + inicio.localPosition.y + 4)/2
					em.localPosition.z = (fim.localPosition.z + inicio.localPosition.z + 13.98832)/2
					meio =scn.addObject('v_meio', em, 985)
					direction = fim.localPosition - inicio.localPosition                   
					AXIS_X = 0                           
					meio.localScale = [direction.length*2, 0.25, 0.25]                                        
					meio.alignAxisToVect(direction, AXIS_X)					
					meio.setParent(eo)
					eo.localPosition.x -= 1.2
				
def run():
	g = Game()			
	g.main_sc()

def series():
	g2 = Game()
	g2.atualizar_dashboard()