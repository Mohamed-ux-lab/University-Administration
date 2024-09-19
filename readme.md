# Administration de university
## Modèle :

  ### Etudiant
    - Nom
    - Prenom 
    - Age
    - Classe
    - Filière

  ### Professeur
    - Nom
    - Prenom
    - Classe (foreignKey)
    - Cours

  ### Classes 
    - Niveau
    - Etudiants (foreignKey)
    - Professeur (foreignKey)

  ### Filières 
    - Spécialité
    - Description
    - Etudiants (foreignKey)

## Fonctionnalité :
    [] - Ajouter des etudians
    [] - Modifier des etudiants
    [] - Supprimer des etudiants
    [] - Afficher tout les etudians
    [] - Ajouter des professeur
    [] - Modifier des professeur
    [] - Supprimer des professeur
    [] - Afficher tout les professeur
    [] - Attribuer un professeur permanent à une filière
    