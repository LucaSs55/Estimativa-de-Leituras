import os
import json

class Usuario:
    def __init__(self, nome, idade, cidade, estado,            
         livros_digitais, livros_fisicos,
         preferencia_leitura, horas_estudo, horas_entretenimento,
         outro_atributo="Não informado"):
         self.nome = nome
         self.idade = int(idade)
         self.cidade = cidade
         self.estado = estado
         self.livros_digitais = int(livros_digitais)
         self.livros_fisicos = int(livros_fisicos)
         self.preferencia_leitura = preferencia_leitura
         self.horas_estudo = int(horas_estudo)
         self.horas_entretenimento = int(horas_entretenimento)

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

    def gerar_relatorio(self):
          total_livros_ano = self.livros_digitais + self.livros_fisicos
          estimativa_5_anos = total_livros_ano * 5

          horas_estudo_ano = self.horas_estudo * 52
          horas_leitura_ano = self.horas_entretenimento * 52

          print(f"\n\033[34mOlá, {self.nome}! Seja bem-vindo(a)!")
          print(f"Você tem {self.idade} anos e mora em {self.cidade} - {self.estado}.")
          print("Aproveite os dados abaixo para acompanhar sua rotina de leitura e estudo.\n")

          # Estimativas de leitura
          if total_livros_ano >= 20:
               nivel_leitura = "Você tem um ótimo ritmo de leitura!"
          elif total_livros_ano >= 10:
               nivel_leitura = "Seu ritmo de leitura é bom, continue assim!"
          else:
               nivel_leitura = "Você pode tentar ler um pouco mais a cada mês."

          print(f"Livros lidos no último ano: {total_livros_ano}")
          print(f"Estimativa para os próximos 5 anos: {estimativa_5_anos} livros")
          print(f"Análise: {nivel_leitura}\n")

          # Estudo e leitura por ano
          print(f"Estimativa de estudo por ano: {horas_estudo_ano} horas")
          print(f"Estimativa de leitura por ano: {horas_leitura_ano} horas\n")

          livros_por_mes = total_livros_ano / 12 if total_livros_ano else 0
          diferenca_estudo_entretenimento = horas_estudo_ano - horas_leitura_ano

          print(f"Estimativa de livros por mês: {livros_por_mes:.2f} \033[m")
        
          if diferenca_estudo_entretenimento > 0:
               print(f"\033[34mVocê estuda {diferenca_estudo_entretenimento} horas a mais por ano do que lê por entretenimento.\033[m")
          elif diferenca_estudo_entretenimento < 0:
               print(f"\033[31mVocê lê por entretenimento {-diferenca_estudo_entretenimento} horas a mais do que estuda por ano.\033[m")
          else:
               print(f"\033[34mSeu tempo de estudo e de leitura por entretenimento estão equilibrados!\033[m")

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
          cidade = input("Digite sua Cidade: ").strip().lower()
          estado = input("Digite seu Estado: ").strip().lower()
          livros_digitais = input("Quantidade de livros digitais lidos no último ano:")
          livros_fisicos = input("Quantidade de livros físicos lidos no último ano:")
          preferencia_leitura = input("Preferência de leitura(digital, kindle ou livro físico):")
          horas_estudo = input("Número de horas que dedicadas aos livros por estudo por semana:")
          horas_entretenimento = input("Número de horas dedicadas aos livros por entretenimento por semana:")
          novo_usuario = Usuario(nome, idade, cidade,estado,livros_digitais,livros_fisicos,preferencia_leitura,horas_estudo,horas_entretenimento)
          self.usuarios.append(novo_usuario) # Salva o novo usuário na lista
          self.salvar_dados_usuarios()
          print("\033[32m Novo Usuário cadastrado com sucesso! \033[m")

     def listar_usuarios(self):   
          if not self.usuarios:
               print("\033[31mNenhum usuário cadastrado ainda.\033[m")
               return

          print("\n\033[34m=== Lista de Usuários Cadastrados ===\033[m")
          for i, usuario in enumerate(self.usuarios, 1):
               print(f"{i}. {usuario}")

     def login_e_gerar_relatorio(self):
          nome = input("Digite seu nome para fazer login: ").strip()
          for usuario in self.usuarios:
               if usuario.nome.lower() == nome.lower():
                    print("\n\033[34mLogin bem-sucedido!\033[m")
                    usuario.gerar_relatorio()
                    return
          print("\033[31mUsuário não encontrado. Verifique o nome digitado.\033[m")

     

          