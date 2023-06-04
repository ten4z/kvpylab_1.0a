import bge
from random import choice, randint
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
class Game():
	lista = []
	pontos = 0
	def atualizar_dashboard(self):
		if own['tmp2'] > 5 and own['tmp2'] <= 5.05:
			obj['dash_c']['indicador'] = randint(0, 100)
			self.graficos_s()
		if own['tmp2'] <= 5:
			pass
		else:
			own['tmp2']	 = 0
	def graficos_s(self):
		ep = obj['Empty_Plotador']
		eo = obj['Empty_Origem']
		#if cont.sensors['tap'].positive:
		lista = [[0,0]]
		ep.localPosition = [4.05 +lista[0][0]*1.5, 2.05544, 7.01727 +  1.5*lista[0][1]]
		v0 = scn.addObject('v_inicio', ep)
		own['pontos'] += 1
		v0['id'] = 5 - own['pontos']
		v0.setParent(eo)
		eo.localPosition.x -= 4.05
		
		
		
		self.pontos += 1
		lista.pop(0)
		px = randint(0,5)
		py = randint(0,5)
		lista.append([px, py])
		ep.localPosition = [4.05 +lista[0][0]*1.5, 2.05544, 7.01727 +  1.5*lista[0][1]]
		v1 = scn.addObject('v_fim', ep)
		#v0.endObject()
		#v1['id'] -= 1
		print(lista)
		'''
		own.localPosition.x  = 0
        own.localPosition.z  = a*0+b
        orig = sc.addObject('orig_reta', own)        
        own.localPosition.x  = 30
        own.localPosition.z  = a*30+b
        ext = sc.addObject('ext_reta', own)        
        own.localPosition.x  = (orig.localPosition.x + ext.localPosition.x)/2
        own.localPosition.z  = (orig.localPosition.z + ext.localPosition.z)/2
        r = sc.addObject('reta', own)        
        direction = ext.localPosition - orig.localPosition                   
        AXIS_X = 0                           
        r.localScale = [direction.length,0.1, 0.1]                                        
        r.alignAxisToVect(direction, AXIS_X)
        '''
		#v1 = scn.addObject('v_inicio', )
	def iniciar(self):
		#print('Game iniciando...')	
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
		'''
		print(len(self.lista))
		print(self.lista)			
		#print(own['tmp1'])
		'''
def run():
	g = Game()
	g.iniciar()
	g.atualizar_dashboard()