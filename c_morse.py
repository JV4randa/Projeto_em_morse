# Importando o módulo 'winsound' para tocar sons (apenas no Windows)
import winsound
# Importando o módulo 'time' para controle de tempo (pausas)
import time
#Importando a biblioteca OS para criar arquivo
import os


# DICIONÁRIO DO CÓDIGO MORSE: associa cada letra e número ao seu equivalente em código Morse
codigos = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
           'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
           'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
           'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
           'Y': '-.--', 'Z': '--..',
           '0': '-----', '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', ' ': '/'  # Espaço tratado de forma especial
          }

# INVERSÃO DO CÓDIGO: cria um novo dicionário com os valores e chaves trocados, para decodificação
mrs_codigo = {v: k for k, v in codigos.items()}

#Criar a pasta para salvar os arquivos resultandes.
nome_pasta = "morse"

# caminho ou directório
caminho = f"C:\\{nome_pasta}\\"

if not os.path.exists(caminho):
    os.mkdir(caminho)

# função para criar arquivo
def criar_arquivo(nome_arquivo, ext, conteudo):
    with open(caminho+nome_arquivo+ext, "w") as arq_morse:
        arq_morse.write(conteudo)

# Função principal do programa
def work():
    print("-"*102)
    print("Escolhe uma opção que pretendes  \n")
    print("1: Converter texto em código morse")
    print("2: Converter código morse em texto")
    print("3: Converter código morse em áudio")
    print("-"*102)

    # Solicita ao usuário que escolha uma das opções
    escolha = int(input("Insira a opção que pretendes: "))

    if (escolha == 1):
        # Opção 1: texto para código Morse
        mensagem = str(input("Texto para ser codificado em morse: \n").upper())

        try:
            # Converte cada caractere em Morse usando o dicionário
            morse = " ".join(codigos[m] for m in mensagem)

            print("Mensagem inserida: \n" + mensagem)
            print("Mensagem saida em código morse: \n" + morse)

            conteudo = f"Texto normal => {mensagem}\nCódigo morse => {morse}"
            criar_arquivo(mensagem, ".txt", conteudo)

        except:
            # Se algum caractere não estiver no dicionário, ocorre erro
            print("Erro traduzir!")

        #Opção para executar novamente.
        opcao = input("Desejas continuar?   S/N  \n").upper()
        if opcao == "S":
            # Chama a função novamente
            work()
        else:
            print("Terminando...")

    elif(escolha == 2):
        # Opção 2: código Morse para texto
        mensagem = str(input("Codificado em morse para ser convertido em texto: \n"))
        
        try:
            # Divide a string em partes e traduz cada parte usando o dicionário invertido
            texto = "".join(mrs_codigo[m] for m in mensagem.split(" "))
            
            print("mensagem inserida: \n" + mensagem)
            print("mensagem saida em código morse: \n" + texto)

            conteudo = f"Texto normal => {mensagem}\nCódigo morse => {morse}"    
            criar_arquivo(texto+"em_morse", ".txt", conteudo)
            
        except:
            print("Erro ao traduzir")
        #Opção para executar novamente.
        opcao = input("Desejas continuar?   S/N  \n").upper()
        if opcao == "S":
            # Chama a função novamente
            work()
        else:
            print("Terminando...")
        
    elif (escolha == 3):
        # Opção 3: código Morse em som
        mensagem = str(input("Codificado em morse para ser convertido em aúdio: \n"))

        # Para cada símbolo na string
        for c in mensagem:
            if c == ".":
                # Toca um bip curto para ponto
                winsound.Beep(1000, 400)
                time.sleep(0.3)
            elif c == "-":
                # Toca um bip longo para traçoF
                winsound.Beep(1000, 900)
                time.sleep(0.3)
            elif c == "/" or c == " ":
                # Pausa entre palavras
                time.sleep(0.5)
            else:
                # Caso encontre símbolo inválido
                print("Caractere inválido detectado!")
        #Opção para executar novamente.
        opcao = input("Desejas continuar?   S/N  \n").upper()
        if opcao == "S":
            # Chama a função novamente
            work()
        else:
            print("Terminando...")

    else:
        # Se a opção inserida não for válida
        print("Opção inválida!")
        opcao = input("\n\n Desejas tentar de novo?   S/N  \n").upper()
        if opcao == "S":
            # Chama a função novamente
            work()
        else:
            print("Terminando...")

# Chamada inicial da função principal
work()