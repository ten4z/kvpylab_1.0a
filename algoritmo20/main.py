from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
kv = """
BoxLayout:  
    orientation: "vertical"
    padding: 10
    spacing: 10
    lbl_saida: lbl_saida    
    txt_nome: txt_nome
    txt_idade: txt_idade
    txt_salario: txt_salario
    MDLabel:
        text: "Informações pessoais."  
    MDTextField:        
        id: txt_nome
        hint_text: "Informe seu nome"
    MDTextField:        
        id: txt_idade
        hint_text: "Informe sua idade"
    MDTextField:        
        id: txt_salario
        hint_text: "Informe seu salário" 
    MDLabel:
        id: lbl_saida
        text: "Aguardando interação..."                            
    MDBoxLayout:
        orientation: "horizontal"
        spacing: 5
        padding: 5      
        MDRaisedButton:
            text: "Imprimir informações"   
            on_press: app.imprimir(txt_nome.text, txt_idade.text, txt_salario.text)   
        MDRaisedButton:
            text: "Sair"    
            on_press: app.stop()
        """
class InformacoesPessoais(MDApp):
    lista = []
    soma = 0         
    def imprimir(self, nome, idade, salario):  
        try:               
            self.root.ids.lbl_saida.text = "Seu nome é: " + nome + "\n" 
            self.root.ids.lbl_saida.text += "Sua idade é: " + idade + " anos\n" 
            self.root.ids.lbl_saida.text += "Seu salario é: R$ " + salario 
        except:
            self.root.lbl_saida.text = "Ops! algum erro ocorreu."
        
    def sair(self):
        MDApp.close()
    def build(self):
        MDApp.title = "Algoritmo 19"
        return Builder.load_string(kv)
if __name__ == "__main__":
    InformacoesPessoais().run()