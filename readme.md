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
    [] - Ajouter des etudians
    [] - Modifier des etudiants
    [] - Supprimer des etudiants
    [] - Afficher tout les etudians
    [] - Ajouter des professeur
    [] - Modifier des professeur
    [] - Supprimer des professeur
    [] - Afficher tout les professeur