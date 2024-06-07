## Calcul de la Transformée de Fourier Discrète (TFD) avec Tkinter
Ce projet est une application simple pour calculer la Transformée de Fourier Discrète (TFD) d'un ensemble de données en utilisant l'algorithme de la Transformée de Fourier Cooley-Tukey récursive. L'interface utilisateur est développée en utilisant le module Tkinter de Python.

## Fonctionnalités
Calcul de la TFD pour un ensemble de données donné.
Validation automatique de la taille des données (doit être une puissance de 2).
Utilisation
Lancez le programme en exécutant le fichier calcul_tfd.py.
Entrez le nombre de données (N) dans le champ prévu à cet effet. Assurez-vous que N est une puissance de 2.
Cliquez sur le bouton "OK".
Une fois le nombre de données confirmé, entrez les valeurs de chaque échantillon dans les champs de saisie qui apparaissent.
Cliquez sur le bouton "Calculer" pour obtenir les résultats de la TFD.

## Installation
Assurez-vous d'avoir Python installé sur votre système. Ce programme utilise la bibliothèque Tkinter pour l'interface graphique.

Clonez ce dépôt vers votre machine locale.
Naviguez vers le répertoire contenant les fichiers.
Exécutez python calcul_tfd.py pour lancer l'application.

## Exemple
Supposons que vous ayez N = 4 données avec les valeurs suivantes :
     x[1]: 1
     x[2]: 2
     x[3]: 3
     x[4]: 4
Après avoir cliqué sur "Calculer", vous obtiendrez les résultats de la TFD dans la zone de sortie.

## Remarques
Le nombre de données doit être une puissance de 2 pour garantir un calcul correct de la TFD.
Assurez-vous d'entrer toutes les valeurs requises pour les échantillons avant de cliquer sur "Calculer".