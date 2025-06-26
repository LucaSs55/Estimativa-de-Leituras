import os
import json
class Usuario:
    def __init__(self, nome, idade, cidade, estado,            
         livros_digitais, livros_fisicos,
         preferencia_leitura, horas_estudo, horas_entretenimento,
         outro_atributo="Não informado"):
         self.nome = nome
         self.idade = idade
         self.cidade = cidade
         self.estado = estado
         self.livros_digitais = livros_digitais
         self.livros_fisicos = livros_fisicos
         self.preferencia_leitura = preferencia_leitura
         self.horas_estudo = horas_estudo
         self.horas_entretenimento = horas_entretenimento

    def modelar_usuario(self):
         return {
              "nome":self.nome,
              "idade":self.idade,
              "cidade":self.cidade,
              "estado":self.estado,
              "livros_digitais":self.livros_digitais,
              "livros_fisicos":self.livros_fisicos,
              "preferencia_leitura":self.preferencia_leitura,
              "horas_estudo":self.horas_estudo,
              "horas_entretenimento":self.horas_entretenimento
         }
    
    def __str__(self):
         return f"Nome:{self.nome} | idade:{self.idade} | cidade:{self.cidade}"
    
class SistemaDeUsuarios:
     def __init__(self,arquivo_externo_usuarios = "usuarios.json"):

          self.arquivo_externo_usuarios = arquivo_externo_usuarios
          self.usuarios = []
          self.carregar_usuarios()

     def menu_principal(self):
          print( "+=+=+=+=+=+=+=+=+=+=+=+=> Menu Principal <=+=+=+=+=+=+=+=+=+=+=+=+")
          print(45*"=-")
          print("[1] - Adicionar Usuário")
          print("[2] - Listar Usuários")
          print("[3] - Receber relatório completo")
          return input("Escolha uma das opções acima:")
     
     def carregar_usuarios(self):
          if os.path.exists(self.arquivo_externo_usuarios):
               with open(self.arquivo_externo_usuarios,"r") as d:
                    try:
                         dados = json.load(d)
                         self.usuarios = []
                         for item in dados:
                              nome = item.get("nome")
                              idade = item.get("idade")
                              cidade = item.get("cidade")
                              estado = item.get("estado")
                              livros_digitais = item.get("livros_digitais")
                              livros_fisicos = item.get("livros_fisicos")
                              preferencia_leitura = item.get("preferencia_leitura")
                              horas_estudo = item.get("horas_estudo")
                              horas_entretenimento = item.get("horas_entretenimento")
                              usuario = Usuario(nome,idade,cidade,estado,livros_digitais,livros_fisicos,preferencia_leitura,horas_estudo,horas_entretenimento)
                              self.usuarios.append(usuario)
                    except json.JSONDecodeError:
                         print("Arquivo Json inválido")
                         self.usuarios = []
          else:
               self.usuarios = []
     def salvar_dados_usuarios(self):
          with open(self.arquivo_externo_usuarios,"w") as d:
               json.dump([item.modelar_usuario() for item in self.usuarios],d,indent=4)

     def adicionar_usuarios(self):
          nome = input("Digite seu nome: ").strip()
          idade = input("Digite seu sua idade: ").strip()
          cidade = input("Digite sua Cidade: ").strip()
          estado = input("Digite seu Estado: ").strip()
          livros_digitais = input("Quantidade de livros digitais lidos no último ano:")
          livros_fisicos = input("Quantidade de livros físicos lidos no último ano:")
          preferencia_leitura = input("Preferência de leitura(digital, kindle ou livro físico):")
          horas_estudo = input("Número de horas que dedicadas aos livros por estudo por semana:")
          horas_entretenimento = input("Número de horas dedicadas aos livros por entretenimento por semana:")

          novo_usuario = Usuario(nome, idade, cidade,estado,livros_digitais,livros_fisicos,preferencia_leitura,horas_estudo,horas_entretenimento)
          self.usuarios.append(novo_usuario) # Salva o novo usuário na lista
          self.salvar_dados_usuarios()
          print("\033[32m Novo Usuário cadastrado com sucesso! \033[m")

          