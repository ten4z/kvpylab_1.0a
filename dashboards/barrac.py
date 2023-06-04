import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
malha = own.meshes[0]
verts = malha.getVertexArrayLength(0)
def atualizar(cont):
    for v in range(0, verts):
        ponto = malha.getVertex(0, v)
        uv = ponto.getUV()
        uv[1] = own['indicador']*0.00989 + 0.00398
        obj['txt_indicador_circulo']['Text'] = own['indicador']
        ponto.setUV(uv)
    
