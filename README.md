# Projet Docker : Plateforme de Gestion et d'Analyse de Données

## Objectif
Ce projet fournit une infrastructure conteneurisée pour la gestion et l'analyse de données en utilisant MongoDB, Flask, Streamlit et Jupyter.

## Structure du Projet
```plaintext
docker-project/
│
├── data/
│   └── mongo_data/
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── streamlit_app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── jupyter/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── notebooks/
│       ├── insert_data.py
│       └── insert_data.ipynb
│
├── docker-compose.yml
└── README.md
```

## Étapes pour lancer le programme

1. **Récupérer le dossier et l'ouvrir dans VSCode par exemple**
    https://github.com/Mohamedi-Ahmed/docker-project

2. **Ouvrir Docker Desktop**

3. **Arrêter et supprimer les conteneurs existants**
   dans le terminal : docker-compose -p docker-project down -v

4. **Démarrer les services**
   dans le terminal : docker-compose -p docker-project up --build -d

5. **Si premier lancement : Insérer des données dans MongoDB**
    - Ouvrez le notebook insert_data.ipynb dans Jupyter : http://localhost:8887 (token demandé)
    - Utilisez ce notebook pour exécuter le script insert_data.py, qui se trouve dans le même répertoire : lancer la cellule avec %run insert_data.py
    - Vous pouvez vérifier l'insertion des données ici http://localhost:8081/ (username et mdp par défaut : admin)

6. **Accéder à Streamlit**
    dans le navigateur : http://localhost:8501

7. **Arrêt des services :**
    dans le terminal : docker-compose down
