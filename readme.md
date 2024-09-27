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