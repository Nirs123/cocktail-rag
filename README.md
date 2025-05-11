# Cocktail-RAG

Bienvenue sur ce projet de Cocktail RAG où l'objectif est de retrouver un cocktail à partir d'un texte entré quelconque grâce à une base de données vectorielle.

Vous trouverez dans ce projet un compte rendu au format Makdown et PDF.

Ce projet a été organisé en 5 étapes, correspondant aux 5 notebooks dans le dossier `notebooks` :

- **1-web_scrapping** : récupération des données de cocktails
- **2-exploration-data** : exploration des données avec visualisations
- **3-creation_bd_vectorielle** : création de la base de données vectorielle
- **4-dataset_eval** : création du dataset d'évaluation pour les méthodes de recherche
- **5-benchmark_distance** : comparaison des méthodes de recherche de distance

De plus, il y a une application Streamlit permettant de tester le projet, et ce dans le dossier `streamlit_app`.

En étant dans ce dossier, il suffit d'exécuter la commande `streamlit run app.py` pour lancer l'application.

Il y a aussi deux dossier `geo` et `img` qui sont utiles à certains notebooks.

Et enfin il y a le dossier `data` qui contient les données de cocktails et le dataset d'évaluation.

**Conseil pour découvrir le projet** : pour découvrir le projet, je vous conseille les étapes suivantes dans l'ordre:

1. Lire le compte rendu
2. Explorer les 5 notebooks dans l'ordre de leur numérotation pour comprendre le code derrière le projet
3. Tester l'application Streamlit pour expérimenter le projet
