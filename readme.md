# Administration de university
## Modèle :

  ### Etudiant
    - Nom
    - Prenom 
    - Age
    - Classe (ForeignKey)
    - Filière (ForeignKey)

  ### Professeur
    - Nom
    - Prenom
    - Spécialité
    - classes (ManyToMany)
    - filiere (ManyToMany)

  ### Classes 
    - Niveau

  ### Filières 
    - Spécialité
    - Description

## Fonctionnalité :
    [x] - Ajouter des etudians
    [x] - Modifier des etudiants
    [x] - Supprimer des etudiants
    [x] - Afficher tout les etudians
    [x] - Ajouter des professeur
    [x] - Modifier des professeur
    [x] - Supprimer des professeur
    [x] - Afficher tout les professeur
    [] - Stylise Interface Utilisateur
    [] - Integrer HTMX dans le projet
    [] - Gerer la pagination
    [] - Ajouter un tableaux de bord
        - Afficher le total des profs et etudiant
        - Afficher le total des des filieres
        - Afficher un graphique avec pour data prof et etudiant
    [] - Une page pour afficher les infos de user et permettre de modifier
    [] - Ajouter des cours et assigner au filiere
    [] - Generer un programme des cours de l'annee 