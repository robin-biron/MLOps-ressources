# MLOps — ressources de formation

Supports de cours et exercices réalisés dans le cadre de la formation **Machine Learning Engineer chez DataScientest, désormais Lyora**.

Ce dépôt regroupe les ressources de formation et le projet Rains : la création d'une **API REST dockerisée de prédiction de pluie**, qui constituait un exercice du cursus.

## Ressources

| Dossier | Contenu |
| --- | --- |
| [FastAPI](FastAPI/) | Introduction aux API, requêtes HTTP et exercice FastAPI |
| [Git](Git/) | Gestion de versions |
| [Github](Github/) | Prise en main, workflows et processus GitHub |
| [Kubernetes](Kubernetes/) | Exercice de déploiement, services et ingress |
| [Linux & Bash](Linux%20%26%20Bash/) | Shell, fichiers, processus, utilisateurs et tâches planifiées |
| [Prise en main VM](Prise%20en%20main%20VM/) | Environnement de travail |
| [Python avancé](Python%20avanc%C3%A9%20%28d%C3%A9corateurs%2C%20annotations%29/) | Décorateurs, annotations, asynchronisme et parallélisme |
| [Tests unitaires](Test%20Unitaires/) | Supports sur les tests |

## Exercice : API REST dockerisée de prédiction de pluie

Le projet auparavant conservé dans le dépôt `mlops_project_rains` est intégré dans **[exercises/rain-prediction-api](exercises/rain-prediction-api/)**.

Il rassemble :

- un notebook de préparation des données et d'entraînement de plusieurs modèles ;
- une API FastAPI permettant de sélectionner un modèle et un échantillon météo pour prédire la pluie du lendemain ;
- des exemples JSON, les Dockerfiles, un fichier Compose et des scripts de test d'authentification et de prédiction.

Consulter le [README de l'exercice](exercises/rain-prediction-api/README.md) pour son organisation et ses limites de reproduction. Les données d'entraînement et les modèles `.pkl` étaient déjà exclus de Git dans le dépôt d'origine.

## Historique Git

Les historiques des deux dépôts sont conservés, sans réécriture ni squash. La version intégrée de Rains provient de la branche `api`, qui contient la dockerisation. Les trois branches d'origine restent consultables grâce aux tags :

- `archive/rains-main` : notebook et première ébauche d'API ;
- `archive/rains-api` : version dockerisée intégrée ici ;
- `archive/rains-feature-robin` : variante de développement de l'API.

Les supports et autres exercices existants restent à leur emplacement d'origine. Les caches Python générés ont été exclus de la version intégrée.

## Docker Compose

Pour installer Docker Compose, suivre la [documentation officielle](https://docs.docker.com/compose/install/).
