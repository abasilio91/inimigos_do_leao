import json
from atualizar import *
from calcular import *
from chat import *
from constante_textos import *
from criar import *
from deletar import *
from ler import *

def chat_pagina1():
    opcao = int(input(CHAT_PAGINA1))

    if opcao not in (1,2,3,4,0):
        print(ERRO_OPCAO_INVALIDA)
        chat_pagina1()

    acao = {
        1: chama_novo_arquivo,
        2: chat_pagina2,
        3: chama_get_entrada,
        4: chat_pagina4,
        0: encerrar_programa
    }
    acao[opcao]()

def chat_pagina2():
  opcao = int(input(CHAT_PAGINA2))

  if opcao not in (1,2,3,4,5,0):
    print(ERRO_OPCAO_INVALIDA)
    chat_pagina2()

  acao = {
      1: chat_pagina3,
      2: chama_atualiza_entrada,
      3: chama_deleta_entrada,
      4: chat_pagina4,
      5: chat_pagina1,
      0: encerrar_programa
  }
  acao[opcao]()

def chat_pagina3():
  opcao = int(input(CHAT_PAGINA3))

  if opcao not in (1,2,3,4,0):
    print(ERRO_OPCAO_INVALIDA)
    chat_pagina3()

  acao = {
      1: chama_nova_receita,
      2: chama_nova_despesa,
      3: chama_novo_investimento,
      4: chat_pagina2,
      0: encerrar_programa
  }
  acao[opcao]()

def chat_pagina4():
  opcao = int(input(CHAT_PAGINA4))

  if opcao not in (1,2,3,4,5,6,0):
    print(ERRO_OPCAO_INVALIDA)
    chat_pagina4()

  acao = {
      1: chama_novo_relatorio,
      2: chama_soma_receitas,
      3: chama_soma_despesas,
      4: chama_soma_investimentos,
      5: chama_valores_futuros,
      6: chat_pagina1,
      0: encerrar_programa
  }
  acao[opcao]()

def encerrar_programa():
  print(SAIDA_ENCERRA_PROGRAMA)

def chama_novo_arquivo():
  novo_arquivo()
  chat_pagina1()

def chama_get_entrada():
  get_entrada()
  chat_pagina1()

def chama_atualiza_entrada():
  atualiza_entrada()
  chat_pagina2()

def chama_deleta_entrada():
  deleta_entrada()
  chat_pagina2()

def chama_nova_receita():
  nova_receita()
  chat_pagina3()

def chama_nova_despesa():
  nova_despesa()
  chat_pagina3()

def chama_novo_investimento():
  novo_investimento()
  chat_pagina3()

def chama_novo_relatorio():
  novo_relatorio()
  print(SAIDA_CRIAR_ARQUIVO_RELATORIO)
  chat_pagina4()

def chama_soma_receitas():
  soma = soma_receitas()
  print(SAIDA_TOTAL_RECEITAS.format(soma))
  chat_pagina4()

def chama_soma_despesas():
  soma = soma_despesas()
  print(SAIDA_TOTAL_DESPESAS.format(soma))
  chat_pagina4()

def chama_soma_investimentos():
  soma, tempo = soma_investimentos()
  print(SAIDA_TOTAL_INVESTIMENTOS.format(tempo, soma))
  chat_pagina4()

def chama_valores_futuros():
  soma, tempo = valores_futuros()
  print(SAIDA_TOTAL_VALORES_FUTUROS.format(tempo, soma))
  chat_pagina4()

def main():
  chat_pagina1()