# Corrigé de l'exercice 2

### 1. Veuillez écrire la partie algorithmique de la fonction  mesurer_longueur

```
@Fonction mesurer_longueur @Entrées texte_1, texte_2 @Sortie Entier
    @DebutBloc
    @Si texte_1 = '' @Ou texte_2 = ''
        @DebutBloc
        @Retourner 0
        @FinBloc
    @Sinon
        @DebutBloc
        resultat <- 0

        premiere_lettre_1 <- texte_1[0]
        premiere_lettre_2 <- texte_2[0]
        reste_du_texte_1 <- texte_1[1:]
        reste_du_texte_2 <- texte_2[1:]

        @Si premiere_lettre_1 = premiere_lettre_2
            @DebutBloc
            resultat <- 1 + mesurer_longueur(reste_du_texte_1, reste_du_texte_2)
            @FinBloc
        @Sinon
            @DebutBloc
            possibilite_1 <- mesurer_longueur(texte_1, reste_du_texte_2)
            possibilite_2 <- mesurer_longueur(reste_du_texte_1, texte_2)
            @Si possibilite_1 > possibilite_2
                @DebutBloc
                resultat <- possibilite_1
                @FinBloc
            @Sinon
                @DebutBloc
                resultat <- possibilite_2
                @FinBloc
            @FinBloc
        @Retourner resultat
        @FinBloc
```

### 2. Expliquez l'utilité de la programmation dynamique

La programmation dynamique permet de résoudre des problèmes d'optimisation lorsque le problème peut être décomposé en sous-problèmes qui sont de même "nature" que le problème initial et qui sont fréquents. Le but de la programmation dynamique est donc :
1. établir un algorithme pour résoudre le problème global
2. diviser le problème global en sous-problèmes identiques et appliquer le même algorithme
3. utiliser la memoization en top-down ou la tabulation en bottom-up pour mettre en cache les résultats des sous-problèmes et les ré-utiliser pour résoudre le problème global
