def calcula_matriz(arquivo):
    import os

    # Obtém o diretório do arquivo Python atual
    diretorio_atual = os.path.dirname(__file__)

    # Calcula o caminho relativo ao arquivo
    nome_arquivo = os.path.join(diretorio_atual, "../instancias/" + arquivo)
    # declaração da matriz inicial auxiliar vazia
    matriz = []

    # Abre o arquivo para leitura
    with open(nome_arquivo, "r") as arquivo:
        # Lê o valor da primeira linha (qunativade de vertices) e o converte para int
        num_vertices = int(arquivo.readline().strip())

        # Lê o restante das linhas do arquivoos converte para int e os adiciona na matriz auxiliar
        for linha in arquivo:
            valores = linha.split()
            valores = [int(valor) for valor in valores]
            matriz.append(valores)

    # Declaração e preenchimento da matriz ponderado com zeros com base na quantidade de vertices
    matriz_ponderada = [[0 for i in range(num_vertices)] for i in range(num_vertices)]
    # Preenchimento da matriz ponderada com os valores da matriz lida
    for origem, destino, peso in matriz:
        matriz_ponderada[origem - 1][destino - 1] = peso
    return matriz_ponderada, num_vertices


def imprime_matriz():
    matriz_ponderada, num_vertices = calcula_matriz("inst-13")
    # Impressão da matriz ponderada
    # Imprime o cabeçalho das colunas
    print("   ", end="")
    for i in range(1, num_vertices + 1):
        print(f"{i:2d} ", end="")
    print()

    # Imprime as linhas da matriz
    for i in range(num_vertices):
        # Imprime o cabeçalho das linhas
        print(f"{i + 1:2d} ", end="")
        # Imprime os pesos das arestas
        for j in range(num_vertices):
            print(f"{matriz_ponderada[i][j]:2d} ", end="")
        print()


# imprime_matriz()
