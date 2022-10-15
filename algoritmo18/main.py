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
    check_soma: check_soma
    check_diferenca: check_diferenca
    check_produto: check_produto
    check_razao: check_razao
    MDLabel:
        text: "Somar dez números."  
    MDTextField:        
        id: num1
        hint_text: "Informe o primeiro número"
    MDTextField:        
        id: num2
        hint_text: "Informe o segundo número"
    MDBoxLayout:
        orientation: "horizontal"
        Check:
            id: check_soma
            active: True
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text: "Soma"
    MDBoxLayout:
        orientation: "horizontal"
        Check:
            id: check_diferenca
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text: "Diferença" 
    MDBoxLayout:
        orientation: "horizontal"
        Check:
            id: check_produto
            size_hint: None, None
            size: "48dp", "48dp"            
            pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text: "Produto" 
    MDBoxLayout:
        orientation: "horizontal"
        Check:
            id: check_razao
            size_hint: None, None
            size: "48dp", "48dp"            
            pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text: "Razão"         
    MDLabel:
        id: lbl_saida
        text: "Esperando interação..."  
    MDBoxLayout:
        orientation: "horizontal"
        spacing: 5
        padding: 5      
        MDRaisedButton:
            text: "Calcular"   
            on_press: app.calcular(num1.text, num2.text)   
        MDRaisedButton:
            text: "Sair"    
            on_press: app.stop()
<Check@MDCheckbox>: 
    group: 'operacao'    
    """
class QuatroOps(MDApp):
    lista = []
    soma = 0         
    def calcular(self, num1, num2):  
        try:   
            if self.root.ids.check_soma.active == True:
                self.root.lbl_saida.text = "Resultado: " + str(int(num1)+int(num2))
            elif self.root.check_diferenca.active == True:
                self.root.lbl_saida.text = "Resultado: " + str(int(num1) - int(num2))
            elif self.root.check_produto.active == True:
                self.root.lbl_saida.text = "Resultado: " + str(int(num1) * int(num2))
            elif self.root.check_razao.active == True:
                if int(num2) != 0:
                    self.root.lbl_saida.text = "Resultado: " + str(int(num1) / int(num2))
                else:
                    self.root.lbl_saida.text = "Impossivel dividir por zero."                   
        except:
            self.root.lbl_saida.text = "Por favor apenas números."    
    def sair(self):
        MDApp.close()
    def build(self):
        MDApp.title = "Algoritmo 18"
        return Builder.load_string(kv)
if __name__ == "__main__":
    QuatroOps().run()