from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:  
    orientation: "vertical"
    padding: 10
    spacing: 10
    lbl_saida: lbl_saida    
    tecla: tecla
    MDLabel:
        text: "Tecla pressionada."  
    MDTextField:        
        id: tecla
        hint_text: "Informe um dígito de 1 a 9"
        on_text: app.verificar(self.text)
          
    MDLabel:
        id: lbl_saida
        text: "Esperando interação..."  
    MDBoxLayout:
        orientation: "horizontal"
        spacing: 5
        padding: 5      
        MDRaisedButton:
            text: "Verificar"   
            on_press: app.verificar(tecla.text)   
        MDRaisedButton:
            text: "Sair"    
            on_press: app.stop()
        """
class VerificarTecla(MDApp):
    lista = []
    soma = 0         
    def verificar(self, tecla):  
        try:               
            if tecla == "1":           
                self.root.ids.lbl_saida.text =  "a tecla [um] foi pressionada."                 
            elif tecla == "2":           
                self.root.ids.lbl_saida.text =  "a tecla [dois] foi pressionada."                 
            elif tecla == "3":           
                self.root.ids.lbl_saida.text =  "a tecla [três] foi pressionada."                 
            elif tecla == "4":           
                self.root.ids.lbl_saida.text =  "a tecla [quatro] foi pressionada."                 
            elif tecla == "5":           
                self.root.ids.lbl_saida.text =  "a tecla [cinco] foi pressionada."                 
            elif tecla == "6":           
                self.root.ids.lbl_saida.text =  "a tecla [seis] foi pressionada."                 
            elif tecla == "7":           
                self.root.ids.lbl_saida.text =  "a tecla [sete] foi pressionada."                
            elif tecla == "8":           
                self.root.ids.lbl_saida.text =  "a tecla [oito] foi pressionada."                 
            elif tecla == "9":           
                self.root.ids.lbl_saida.text =  "a tecla [nove] foi pressionada."                 
            else:
                self.root.ids.tecla.text = "" 
        except:
            self.root.lbl_saida.text = "Por favor apenas números."
        
    def sair(self):
        MDApp.close()
    def build(self):
        MDApp.title = "Algoritmo 19"
        return Builder.load_string(kv)
if __name__ == "__main__":
    VerificarTecla().run()