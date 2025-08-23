from tabulate import tabulate

class Busca:
    def __init__(self, Grafo):
        if not Grafo:
            raise ValueError("Jovem, sem grafo não dá para fazer nada!")
        self.Grafo = Grafo
        self.todosNos = set(Grafo.keys())
        for nosAdjacentes in Grafo.values():
            self.todosNos.update(nosAdjacentes)
        print(f"Grafo carregado, pontos para visitar: {sorted(self.todosNos)}")

    def gerar_filhos(self, no_pai):
        return list(self.Grafo.get(no_pai, set()))

    def objetivo(self, caminho):                    # verifica se o caminho um ciclo que visita todos os nos
        return (len(caminho) == len(self.todosNos) + 1 and 
                caminho[0] == caminho[-1])

    def formatar_caminhos(self, lista_caminhos):                     # dexando masi bonito as possibilidades de caminho
        return ["→".join(caminho) for caminho in lista_caminhos]

    def busca_backtracking(self, no_inicial):
        EC= None                 #estado corrente
        LE = [no_inicial]        #basicamente o caminho
        LNE = [[no_inicial]]     #nos a serem explorados
        BSS = []                #nos que ja foram explorados famoso beso sem saida
        it = 0                  #it a coisa, zuera, iterações
        log = []                #log para debugar esse role depois

        while LNE:
            caminho_atual = LNE.pop(0)  
            EC = caminho_atual[-1]     

            log.append([
                it, 
                EC, 
                "→".join(caminho_atual), 
                self.formatar_caminhos(LNE), 
                self.formatar_caminhos(BSS)
            ])
            it += 1

            if self.objetivo(caminho_atual):
                print(" haee !!!foi possível encontrar uma solução")
                print(tabulate(log, headers=["IT", "EC", "LE", "LNE", "BSS"], tablefmt="grid"))
                return caminho_atual

            filhos = self.gerar_filhos(EC)
            
            filhos_validos = [
                f for f in filhos 
                if f not in caminho_atual or 
                (len(caminho_atual) == len(self.todosNos) and f == no_inicial)
            ]

            if filhos_validos:
                novos_caminhos = [caminho_atual + [f] for f in filhos_validos]
                LNE = novos_caminhos + LNE
            else:
                BSS.append(caminho_atual)

        print(tabulate(log, headers=["IT", "EC", "LE", "LNE", "BSS"], tablefmt="grid"))
        return "A busca falhou miseravelmente, acontece "


Grafo = {
    "A": {"B", "C", "D", "E"},
    "B": {"A", "C", "D", "E"},
    "C": {"A", "B", "D", "E"},
    "D": {"A", "B", "C", "E"},
    "E": {"A", "B", "C", "D"}
}

buscador = Busca(Grafo)
resultado = buscador.busca_backtracking("A")
print("Busca Backtracking:", resultado)


Grafo_incompleto = {
    "A": {"B", "C"},
    "B": {"A", "C", "D"},
    "C": {"A", "B", "D"},
    "D": {"B", "C", "E"},
    "E": {"D"} # E e um beco sem saida
}

buscador2 = Busca(Grafo_incompleto)
resultado2 = buscador2.busca_backtracking("A")
print("Busca Backtracking:", resultado2)

Grafo_completo_grande = {
    "A": {"B", "C", "D", "E", "F", "G"},
    "B": {"A", "C", "D", "E", "F", "G"},
    "C": {"A", "B", "D", "E", "F", "G"},
    "D": {"A", "B", "C", "E", "F", "G"},
    "E": {"A", "B", "C", "D", "F", "G"},
    "F": {"A", "B", "C", "D", "E", "G"},
    "G": {"A", "B", "C", "D", "E", "F"}
}
buscador3 = Busca(Grafo_completo_grande)
resultado3 = buscador3.busca_backtracking("A")
print("Busca Backtracking em grafo completo grande:",resultado3)

Grafo_incompleto_grande = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "E"},
    "D": {"B", "F"},
    "E": {"C"},
    "F": {"D", "G"},
    "G": {"F"}  # G é um beco sem saida
}
buscador4 = Busca(Grafo_incompleto_grande)
resultado4 = buscador4.busca_backtracking("A")
print("Busca Backtracking em grafo incompleto grande:",resultado4)
