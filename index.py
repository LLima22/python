texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

# Encontrar a posição do primeiro ponto (.)
posicao_ponto = texto.find('.')
# Encontrar a posição da primeira vírgula (,)
posicao_virgula = texto.find(',')

# Verificar se o ponto e a vírgula foram encontrados no texto
if posicao_ponto != -1 and posicao_virgula != -1:
    # Inicializar uma lista para armazenar os textos extraídos
    textos_extraidos = []

    # Iterar sobre o texto para encontrar todas as ocorrências
    # de ponto (.) e vírgula (,) e extrair os textos entre eles
    while posicao_ponto != -1 and posicao_virgula != -1:
        texto_extraido = texto[posicao_ponto + 1:posicao_virgula]
        texto_extraido = texto_extraido.strip()  # Remover espaços em branco adicionais
        textos_extraidos.append(texto_extraido)

        # Atualizar as posições para encontrar a próxima ocorrência
        posicao_ponto = texto.find('.', posicao_virgula)
        posicao_virgula = texto.find(',', posicao_virgula + 1)

    # Imprimir os textos extraídos
    print("Textos entre o primeiro ponto (.) e a primeira vírgula (,):")
    for texto_extraido in textos_extraidos:
        print(texto_extraido)
else:
    print("Ponto (.) ou vírgula (,) não encontrados no texto.")