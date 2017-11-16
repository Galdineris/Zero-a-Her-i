import Blocagemv1 as principal
rank = [["Mabel", 7],["Shadow", 5],["Shinigami", 8 ],["Mick", 3]]



def pontuacao(name, pontos):
    rank.append([name, pontos])


def buscar_pontuacao():
    nome = str(input("Insira o seu nome: "))

    temp = []
    for i in rank:
        print (i)
        print (i[0])
        if (i[0] == nome):
            temp.append(i)
        

        if temp != []:
         print ("Nome: ", rank[i][0], "     Pontos: ", rank[i][1])
        else:
          return None


def imprimir_ranking():
    print ("-------------Highscores---------")
    for i in range (len(rank)):
        
        print ("Nome: ", rank[i][0], "     Pontos: ", rank[i][1])
        


def ordenar_ranking():
    for i in range(len(rank)):
        for j in range(len(rank)-1):
            if rank[i][1] > rank[j][1]:
                aux = rank[i]
                rank[i] = rank[j]
                rank[j] = aux

def créditos():
    print("---------------------------------Créditos---------------------------------------------------")
    print ("Artur Santos -------------------------Graphics")
    print ("Rafael Marinho ----------------------Logical")
    print ("Rodrigo Nascimento ------------ Score, menus and moral support \n")

    print("Special thanks to: Profª Daniela")


    print("--------------------------------------------------------------------------------------------------")


def menu_principal():
    run_menu = True
    menu = ("\n---De zero a herói----\n"+
             "(1) Iniciar jogo\n" +
             "(2) Mostrar Ranking \n" +
             "(3) Buscar Jogador \n" +
             "(4) Créditos \n" +
            "(0) Sair do Jogo \n"+
            "----------------")
    
    while(run_menu):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            principal.main()
        elif op == 2:
            imprimir_ranking()

        elif op == 3:
            buscar_pontuacao()

        elif op == 4:
            créditos()

        elif op == 0:
            print ("Saindo do jogo")
            run_menu = False


                
                
menu_principal()
