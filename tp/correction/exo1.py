'''
# EXERCICE 1 : Le tri casier

1. Veuillez expliquer le fonctionnement du tri casier ou tri comptage

C'est un tri **sans comparaison** qui vise à **bucketer** les elements d'un tableau et **reconstruire le tableau** 
résultat grâce aux **comptes** de chacun des éléments, pourvu que ces éléments soient discrets et finis.

[3, 2, 2, 3, 2, 3, 1]

(1) : 1
(2) : 3
(3) : 3

[1, 2, 2, 2, 3, 3, 3]
'''

'''
2. Veuillez écrire la partie algorithmique du tri casier [-1, 1]

@Fonction triCasier @Entrées tablo @Sortie Tableau
    @DebutBloc
    count <- [0, 0, 0]
    @PourChaque element @Dans tablo
        @DebutBloc
        count[element + 1] <- count[element + 1] + 1
        @FinBloc

    tableauTrie <- []
    @Pour k @De 0 @A 3
        @DebutBloc
        @Pour i @De 0 @A count[k]
            @DebutBloc
            tableauTrie.ajouter k - 1
            @FinBloc
        @FinBloc

    @Retourner tableauTrie
    @FinBloc

@Fonction triCasier @Entrées tablo @Sortie Tableau
    @DebutBloc
    compteMoinsUn <- 0
    compteZero <- 0
    compteUn <- 0

    @PourChaque element @Dans tablo
        @DebutBloc
        @Si element = -1
            @DebutBloc
            compteMoinsUn <- compteMoinsUn + 1
            @FinBloc
        @Sinon @Si element = 0
            @DebutBloc
            compteZero <- compteZero + 1
            @FinBloc
        @Sinon
            @DebutBloc
            compteUn <- compteUn + 1
            @FinBloc
        @FinBloc

    tableauTrie <- []
    @Pour i @De 0 @A compteMoinsUn
        @DebutBloc
        tableauTrie.ajouter -1
        @FinBloc

    @Pour i @De 0 @A compteZero
        @DebutBloc
        tableauTrie.ajouter 0
        @FinBloc

    @Pour i @De 0 @A compteUn
        @DebutBloc
        tableauTrie.ajouter 1
        @FinBloc

    @Retourner tableauTrie

    @FinBloc
'''

'''
3. Veuillez implémenter une fonction, permettant de trier un tableau de nombres entiers dans l'intervalle suivant [-1, 1] en utilisant le tri casier en Python.
'''

def tri_casier(tablo):
    compteMoinsUn = 0
    compteZero = 0
    compteUn = 0

    for element in tablo:
        if element == -1:
            compteMoinsUn = compteMoinsUn + 1
        elif element == 0:
            compteZero = compteZero + 1
        else:
            compteUn = compteUn + 1
    
    tableauTrie = []
    for i in range(compteMoinsUn):
        tableauTrie.append(1)
    
    for i in range(compteZero):
        tableauTrie.append(0)
    
    for i in range(compteUn):
        tableauTrie.append(1)
    
    return tableauTrie
