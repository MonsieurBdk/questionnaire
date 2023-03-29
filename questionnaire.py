# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json

class Question:
    def __init__(self, titre, choix, index): #je change la config ancienne, je préfère m'adapter à la structure des données reçues
        self.titre = titre
        self.choix = choix
        self.index = index

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print(f"QUESTION {self.index + 1}")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0]) # j'affiche juste le choix sans dire s'il est correct ou pas

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1][1]: #la vérification devient plus simple ici, je n'ai qu'à vérifier le booléen associé
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self,categorie ,questions, title, level): # j'ajoute les variables d'instance title et level
        self.questions = questions
        self.title = title
        self.level = level
        self.categorie = categorie

    def lancer(self):
        score = 0
        print("CATEGOGIE: ",self.categorie)
        print("TITRE: ",self.title) #j'affiche le titre 
        print("NIVEAU: ",self.level) # j'affiche le niveau de difficulté
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score :", score, "sur", len(self.questions))
        return score
    


def get_questions_from_json(file):
    with open(file): # j'ouvre le fichier json, conserve dans des variables afin d'en exploiter le contenu
        data = json.load(open(file))
    return data

def convert_dict_to_question(data): # je transforme les questions qui sont des dicts en Question
    questions = [Question(titre=question["titre"], choix=question["choix"], index=data["questions"].index(question)) for question in data["questions"]]
    return questions

data_debutant = get_questions_from_json('animaux_leschats_debutant.json')
data_confirme = get_questions_from_json('animaux_leschats_confirme.json')
data_expert = get_questions_from_json('animaux_leschats_expert.json')

def lancer_questionnaire(data): #je lance ici le questionnaire à partir des données entrées
    liste_questions = convert_dict_to_question(data)
    questionnaire = Questionnaire(categorie=data["categorie"],questions=liste_questions,title=data["titre"], level=data["difficulte"])
    score = questionnaire.lancer()
    print("-"*40)
    return score

score1 = lancer_questionnaire(data_debutant)

score2 = lancer_questionnaire(data_confirme)
score3 = lancer_questionnaire(data_expert)
print(f"SCORE FINAL: {score1+score2+score3} ")
