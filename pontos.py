rank = [["Mabel", 7],["Shadow", 5],["Shinigami", 8 ],["Mick", 3]]



def pontuacao(name, pontos):
    rank.append([name, pontos])


def buscar_pontuacao():
    nome = str(input("Insira o seu nome: "))

    for i in range(len(rank)):
        if nome == rank[i][0]:
            print ("Nome: ", rank[i][0], "     Pontos: ", rank[i][1])
        else:
            return None
            


def imprimir_ranking():
    print ("-------------Highscores---------")
    for i in range (len(rank)):
        
        print ("Nome: ", rank[i][0], "     Pontos: ", rank[i][1])
        


def ordenar_ranking():
    for i in range(len(rank)-1):
        for j in range(len(rank)-2):
            if rank[i][1] > rank[j][1]:
                aux = rank[i]
                rank[i] = rank[j]
                rank[j] = aux


def menu_principal():
    run_menu = True
    menu = ("\n---De zero a herói----\n"+
             "(1) Iniciar jogo\n" +
             "(2) Mostrar Ranking \n" +
             "(3) Buscar Jogador \n" +
            "----------------")
    
    while(run_menu):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            pass
        elif op == 2:
            imprimir_ranking()

        elif op == 3:
            buscar_pontuação()


                
                
menu_principal()
