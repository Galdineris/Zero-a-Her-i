rank = [["Mabel", 10],["Shadow", 8],["Shinigami": 5 ],["Mick": 3]]

#def mostrar_ranking():
#    return rank


def pontuacao():
    name = str(input("Insira seu nome: "))
    pontos = 0
    
    rank.append([name, pontos])
        
def high_scores():
    print ("_________Highscores_______")
    rank.sort
    for i in range (len(rank)):
        print ("Nome: ", rank[i][0], " Pontos: ", rank[i][1])
        
        
        
        
    
    
       
        
    
    



#inicializar_ranking()
high_scores()
#pontuacao()
print (rank)