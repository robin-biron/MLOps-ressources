# Rains — exercice d'API REST dockerisée

Exercice de la formation Machine Learning Engineer de DataScientest, désormais Lyora : exposer des modèles de machine learning dans une **API REST FastAPI conteneurisée avec Docker** pour prédire s'il pleuvra le lendemain.

## Organisation

```text
rain-prediction-api/
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py              # API, authentification et prédiction
│   │   └── sample_*.json        # Exemples météo
│   └── notebooks/
│       ├── rains (1).ipynb      # Préparation et entraînement
│       └── feature.json
├── test_authorization/         # Script HTTP et image de test d'authentification
├── test_model/                 # Script HTTP et image de test des prédictions
└── docker-compose.yml          # Définition historique des trois services
```

L'API propose `/Login` et `/select_model`, avec une sélection du modèle et d'un échantillon météo. Les modèles référencés incluent la régression logistique, SVM, KNN, un arbre de décision, AdaBoost et Random Forest.

## État de reproduction

Les fichiers sources de la branche `api` ont été conservés lors de l'intégration. Il s'agit d'un exercice historique, pas d'un service déployé.

- Le notebook attend `rains.csv`. Le jeu de données et les modèles `.pkl` n'étaient pas versionnés dans le dépôt d'origine et ne sont pas fournis ici.
- Le notebook exporte les modèles ; certains noms d'exports diffèrent de ceux attendus par l'API pour l'arbre de décision et Random Forest. Il faut les aligner avant une exécution des prédictions.
- Le fichier Compose référence les images `rains-app`, `author_test` et `model_test`, sans étape de construction ni publication de port. Les Dockerfiles se trouvent respectivement dans `api`, `test_authorization` et `test_model`.
- Les scripts de test ciblent `127.0.0.1:8000`, tandis que l'image API écoute sur le port 80. Leur adressage doit être adapté avant un lancement dans des conteneurs distincts.
- Les dépendances sont celles de l'exercice historique. La fusion du dépôt ne constitue pas une validation de fonctionnement avec les environnements actuels.

Le notebook d'origine et les variantes d'API restent accessibles aux tags `archive/rains-main`, `archive/rains-api` et `archive/rains-feature-robin` du dépôt principal.
