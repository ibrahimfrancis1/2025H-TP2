"""
TP2 : Gestion d'une base de données d'un hôpital

Groupe de laboratoire : 02
Numéro d'équipe :  06
Noms et matricules : Ibrahim Francis Coulibaly (2350383), Yassine Bouchbika (2338694)
"""
import math
import csv

########################################################################################################## 
# PARTIE 1 : Initialisation des données (2 points)
##########################################################################################################

def load_csv(csv_path):
    """
    Fonction python dont l'objectif est de venir créer un dictionnaire "patients_dict" à partir d'un fichier csv

    Paramètres
    ----------
    csv_path : chaîne de caractères (str)
        Chemin vers le fichier csv (exemple: "/home/data/fichier.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans le fichier csv
    """

    patients_dict = {}
        
    # TODO : Écrire votre code ici

    with open(csv_path, 'r') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
    
        for ligne in lecteur_csv:
            id = ligne['participant_id']
            patients_dict[id] = {
                'sex': ligne['sex'],
                'age': ligne['age'],
                'height': ligne['height'],
                'weight': ligne['weight'],
                'date_of_scan': ligne['date_of_scan'],
                'pathology': ligne['pathology']
            }

    # Fin du code

    return patients_dict

########################################################################################################## 
# PARTIE 2 : Fusion des données (3 points)
########################################################################################################## 

def load_multiple_csv(csv_path1, csv_path2):
    """
    Fonction python dont l'objectif est de venir créer un unique dictionnaire "patients" à partir de deux fichier csv

    Paramètres
    ----------
    csv_path1 : chaîne de caractères (str)
        Chemin vers le premier fichier csv (exemple: "/home/data/fichier1.csv")
    
    csv_path2 : chaîne de caractères (str)
        Chemin vers le second fichier csv (exemple: "/home/data/fichier2.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans les deux fichier csv SANS DUPLICATIONS
    """
    patients_dict = {}
    doublon = False

    # TODO : Écrire votre code ici

    with open(csv_path1, 'r') as fichier_csv1:
        lecteur_csv = csv.DictReader(fichier_csv1)
    
        for ligne in lecteur_csv:
            id = ligne['participant_id']
            patients_dict[id] = {
                'sex': ligne['sex'],
                'age': ligne['age'],
                'height': ligne['height'],
                'weight': ligne['weight'],
                'date_of_scan': ligne['date_of_scan'],
                'pathology': ligne['pathology']
            }


    with open(csv_path2, 'r') as fichier_csv2:
        lecteur_csv2 = csv.DictReader(fichier_csv2)
    
        for ligne in lecteur_csv2:
            id = ligne['participant_id']
            
            for identifiant in patients_dict:
                
                if identifiant == id:
                    doublon == True
                    break
            
            if doublon == False:
                patients_dict[id] = {
                    'sex': ligne['sex'],
                    'age': ligne['age'],
                    'height': ligne['height'],
                    'weight': ligne['weight'],
                    'date_of_scan': ligne['date_of_scan'],
                    'pathology': ligne['pathology']
                }


    # Fin du code

    return patients_dict

########################################################################################################## 
# PARTIE 3 : Changements de convention (4 points)
########################################################################################################## 

def update_convention(old_convention_dict):
    """
    Fonction python dont l'objectif est de mettre à jour la convention d'un dictionnaire. Pour ce faire, un nouveau dictionnaire
    est généré à partir d'un dictionnaire d'entré.

    Paramètres
    ----------
     old_convention_dict : dictionnaire python (dict)
         Dictionnaire contenant les informations des "patients" suivant l'ancienne convention
    
    Résultats
      ---------
    new_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant la nouvelle convention
    """
    new_convention_dict = {}

    # TODO : Écrire votre code ici
    for id, donnees in old_convention_dict.items():
        for cle, valeur in donnees.items():
            if cle == "date_of_scan" and valeur == "n/a":
                donnees[cle] = None
                new_convention_dict[id] = donnees
                break
            elif cle == "date_of_scan" and '-' in valeur:
                #new_date = valeur.replace("-", "/")
                donnees[cle] = valeur.replace("-", "/")
                new_convention_dict[id] = donnees
                break

    # Fin du code

    return new_convention_dict

########################################################################################################## 
# PARTIE 4 : Recherche de candidats pour une étude (5 points)
########################################################################################################## 

def fetch_candidates(patients_dict):
    """
    Fonction python dont l'objectif est de venir sélectionner des candidats à partir d'un dictionnaire patients et 3 critères:
    - sexe = femme
    - 25 <= âge <= 32
    - taille > 170

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    candidates_list : liste python (list)
        Liste composée des `participant_id` de l'ensemble des candidats suivant les critères
    """
    candidates_list = []

    # TODO : Écrire votre code ici

    
    for i in patients_dict:
        if (patients_dict[i].get("sex") == 'F'):
            if (int(patients_dict[i].get("age"))) >= 25 and (int(patients_dict[i].get("age"))) <= 32:
                if (int(patients_dict[i].get("height")) > 170):     
                    candidates_list.append(i)    
    

    # Fin du code

    return candidates_list

########################################################################################################## 
# PARTIE 5 : Statistiques (6 points)
########################################################################################################## 

def fetch_statistics(patients_dict):
    """
    Fonction python dont l'objectif est de venir calculer et ranger dans un nouveau dictionnaire "metrics" la moyenne et 
    l'écart type de l'âge, de la taille et de la masse pour chacun des sexes présents dans le dictionnaire "patients_dict".

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux contenant:
            - au premier niveau: le sexe --> metrics.keys() == ['M', 'F']
            - au deuxième niveau: les métriques --> metrics['M'].keys() == ['age', 'height', 'weight'] et metrics['F'].keys() == ['age', 'height', 'weight']
            - au troisième niveau: la moyenne et l'écart type --> metrics['M']['age'].keys() == ['mean', 'std'] ...
    
    """
    metrics = {'M':{}, 'F':{}}

    # TODO : Écrire votre code ici
    metrics.update({'M' : {'age' : {'mean' : {}, 'std' : {}}, 'height' : {'mean' : {}, 'std': {}}, 'weight' : {'mean' : {}, 'std' : {}}}})
    metrics.update({'F' : {'age' : {'mean' : {}, 'std' : {}}, 'height' : {'mean' : {}, 'std': {}}, 'weight' : {'mean' : {}, 'std' : {}}}})

    #Calcul des moyennes 'M'
    counter1 = 0
    counter2 = 0
    sum_M1 = 0
    sum_M2 = 0
    sum_M3 = 0
    for i in patients_dict:

        if patients_dict[i].get('sex') == 'M':
            sum_M1 += int(patients_dict[i].get('age'))
       
            sum_M3 += float(patients_dict[i].get('weight'))
            counter1+=1

            if patients_dict[i].get('height')!= 'n/a':
                sum_M2 += int(patients_dict[i].get('height'))
                counter2+=1

    metrics['M']['age']['mean'] = sum_M1//counter1
    metrics['M']['height']['mean'] = sum_M2//counter2
    metrics['M']['weight']['mean'] = int(sum_M3//counter1)

    #Calcul des moyennes 'F'
    counter3 = 0
    sum_F1 = 0
    sum_F2 = 0
    sum_F3 = 0
    for i in patients_dict:

        if patients_dict[i].get('sex') == 'F':
            sum_F1 += int(patients_dict[i].get('age'))
            sum_F2 += int(patients_dict[i].get('height'))
            sum_F3 += int(patients_dict[i].get('weight'))
            counter3+=1

    metrics['F']['age']['mean'] = sum_F1//counter3
    metrics['F']['height']['mean'] = sum_F2//counter3
    metrics['F']['weight']['mean'] = sum_F3//counter3


    #Écars-types chez 'M'
    MAge = metrics['M']['age']['mean']
    MHeight = metrics['M']['height']['mean']
    MWeight = metrics['M']['weight']['mean']

    pre1 = 0
    pre2 = 0
    pre3 = 0
    counter4 = 0
    counter5 = 0

    for i in patients_dict:
        if patients_dict[i].get('sex') == 'M':
            pre1 += (MAge-int(patients_dict[i].get('age')))**2
            pre3 += (MWeight-float(patients_dict[i].get('weight')))**2
            counter4 += 1

            if patients_dict[i].get('height') != 'n/a':
                pre2 += (MHeight-int(patients_dict[i].get('height')))**2
                counter5 += 1

    
    metrics['M']['age']['std'] = int((pre1/counter4)**(1/2))
    metrics['M']['height']['std'] = int((pre2/counter5)**(1/2))
    metrics['M']['weight']['std'] = int((pre3/counter4)**(1/2))

        #Écars-types chez 'F'
    FAge = metrics['F']['age']['mean']
    FHeight = metrics['F']['height']['mean']
    FWeight = metrics['F']['weight']['mean']

    pre4 = 0
    pre5 = 0
    pre6 = 0
    counter6 = 0

    for i in patients_dict:
        if patients_dict[i].get('sex') == 'F':
            pre4 += (FAge-int(patients_dict[i].get('age')))**2
            pre5 += (FHeight-int(patients_dict[i].get('height')))**2
            pre6 += (FWeight-float(patients_dict[i].get('weight')))**2
            counter6 += 1

    
    metrics['F']['age']['std'] = int((pre4/counter6)**(1/2))
    metrics['F']['height']['std'] = int((pre5/counter6)**(1/2))
    metrics['F']['weight']['std'] = int((pre6/counter6)**(1/2))











    


            










    # Fin du code

    return metrics

########################################################################################################## 
# PARTIE 6 : Bonus (+2 points)
########################################################################################################## 

def create_csv(metrics):
    """
    Fonction python dont l'objectif est d'enregister le dictionnaire "metrics" au sein de deux fichier csv appelés
    "F_metrics.csv" et "M_metrics.csv" respectivement pour les deux sexes.

    Paramètres
    ----------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux généré lors de la partie 5
    
    Résultats
    ---------
    paths_list : liste python (list)
        Liste contenant les chemins des deux fichiers "F_metrics.csv" et "M_metrics.csv"
    """
    paths_list = []

    # TODO : Écrire votre code ici


    # Fin du code

    return paths_list

########################################################################################################## 
# TESTS : Le code qui suit permet de tester les différentes parties 
########################################################################################################## 

if __name__ == '__main__':
    ######################
    # Tester la partie 1 #
    ######################

    # Initialisation de l'argument
    csv_path = "subjects.csv"

    # Utilisation de la fonction
    patients_dict = load_csv(csv_path)

    # Affichage du résultat
    print("Partie 1: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 2 #
    ######################

    # Initialisation des arguments
    csv_path1 = "subjects.csv"
    csv_path2 = "extra_subjects.csv"

    # Utilisation de la fonction
    patients_dict_multi = load_multiple_csv(csv_path1=csv_path1, csv_path2=csv_path2)

    # Affichage du résultat
    print("Partie 2: \n\n", patients_dict_multi, "\n")

    ######################
    # Tester la partie 3 #
    ######################

    # Utilisation de la fonction
    new_patients_dict = update_convention(patients_dict)

    # Affichage du résultat
    print("Partie 3: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 4 #
    ######################

    # Utilisation de la fonction
    patients_list = fetch_candidates(patients_dict)

    # Affichage du résultat
    print("Partie 4: \n\n", patients_list, "\n")

    ######################
    # Tester la partie 5 #
    ######################

    # Utilisation de la fonction
    metrics = fetch_statistics(patients_dict)

    # Affichage du résultat
    print("Partie 5: \n\n", metrics, "\n")

    ######################
    # Tester la partie 6 #
    ######################

    # Initialisation des arguments
    dummy_metrics = {'M':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}, 
                     'F':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}}
    
    # Utilisation de la fonction
    paths_list = create_csv(metrics)

    # Affichage du résultat
    print("Partie 6: \n\n", paths_list, "\n")

