# TP2: Gestion de base de données d'un hôpital

## Directives

⏰ Date de remise : 

📬 À remettre sur Moodle

## Objectifs

L'objectif de ce travail pratique est d'apprendre à manipuler une base de données en utilisant Python. Ce TP vous permettra de découvrir et de maîtriser :  

- Les structures de contrôle, telles que les structures conditionnelles (`if`, `else`, etc.) et les structures de répétition (`for`, `while`, etc.)  
- Les différentes structures de données, comme les listes, les dictionnaires, et les tuples.
- Le module python `csv` permettant d'ouvrir et d'enregister des fichiers csv.

Ces notions seront explorées à travers différentes parties présentant chacunes différentes utilisations pratiques de ces outils.

## Introduction

Vous avez récemment été engagé par un hôpital pour gérer plusieurs bases de données dont la liste des patients ayant donné leur consentement pour participer à une recherche en IRM. Cette base de données, accessible dans le fichier `subjects.csv`, contient les informations suivantes:
- `participant_id`: identifiant unique associé au patient
- `age`: âge du patient
- `sex`: sexe bilogique du patient
- `height`: taille du patient (cm)
- `weight`: masse du patient (kg)
- `date_of_scan`: date de scan (YYYY-MM-DD)
- `pathology`: pathologie
  - HC: Healthy Control (patient sain)
  - DCM: Degenerative Cervical Myelopathy (myelopathie cervicale degenerative)
  - MildCompression: Mild Spinal Cord Copression (compression moyenne de la moelle épinière)

## Partie 1: Initialisation des données

Dans cette section, vous devrez charger les données contenues dans le fichier `subjects.csv` à l'aide du module python [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) et constituer un dictionnaire python appelé `patients` utilisant:
- `participant_id` comme clé principale
- un deuxième dictionnaire comprenant le reste des informations en guise de valeur.

## Partie 2: Fusion des données

Vous vous apercevez qu'un collègue à vous dispose également d'une liste de patients et vous souhaiteriez regrouper tous ces dernier au sein d'un unique dictionnaire python appelé `patients` comme précédemment. Dans cette partie, vous devrez regrouper l'ensemble des patients provenant des fichiers `subjects.csv` et `extra_subjects.csv` tout en **ÉVITANT LES DUPLICATIONS** en suivant la même construction que dans la partie 1.

## Partie 3: Changements de convention

L'hôpital dans lequel vous travaillez décide de mettre à jour l'ensemble de ses base de données pour suivre une nouvelle convention au niveau des dates. Cette nouvelle convention impose:
- d'utiliser des slashs `/` à la place des tirets `-`
- de remplacer les mentions `n/a` par l'objet python **None**

Afin de respecter ces nouvelles conventions, créer un nouveau dictionnaire appelé `new_convention` pour mettre à jour la gestion des dates du dictionnaire `patients` créé dans la partie 2.

## Partie 4: Recherche de candidats pour une étude

Dans le cadre d'une nouvelles étude, un groupe de chercheurs travaillant dans votre hôpital souhaite faire appel à vos services afin d'identifier des patients pour faire un nouveau scan IRM. Cependant, les candidats sélectionnés doivent satisfaire à quelques critères:
Dans le cadre d'une nouvelle étude, un groupe de chercheurs de votre hôpital sollicite votre expertise pour identifier des patients pour un scan IRM. Cependant, ces candidats doivent répondre aux critères suivants :
| Sexe | Âge | Taille |
|:---:|:---:|:---:|
|Feminin|25 ≤ âge ≤ 32| taille > 170|

En suivant ces critères, créer une liste composée des `participant_id` de l'ensemble des candidats possibles.

## Partie 5: Statistiques

L'hôpital souhaiterait obtenir les statistiques par sexe de votre base de données. Pour cela, calculez la moyenne et l'écart type de `l'âge`, de `la taille` et de `la masse` pour chacun des deux groupes. Les statistiques devront être rangées au sein d'un nouveau dictionnaire appelé `metrics` composé de 3 niveaux.

Par exemple:
- la moyenne de la taille dans le groupe masculin sera obtenue de la manière suivante:
```python
print(metrics['M']['height']['mean'])
```
- l'écart type de l'âge dans le groupe feminin sera obtenue de la manière suivante:
```python
print(metrics['F']['age']['std'])
```

## Références

Les données utilisées dans les fichiers csv de ce TP sont extraites de la base de données [data-multi-subject](https://github.com/spine-generic/data-multi-subject).  

 
