# Librairies import
import pandas as pd
import random as rd

# Lecture du fichier CSV comportant les questions
questions = pd.read_csv("Questions.csv", sep =";")

# Declaration des variables
score = 0
id_questions_posees = set()


def id_question(questions=questions, id_questions_posees=id_questions_posees):
    # Fonction qui retourne l'id d'une question a poser
    nbr_questions = len(questions)
    id = rd.randint(0,nbr_questions)
    while id in id_questions_posees:
        id = rd.randint(0,nbr_questions)
    id_questions_posees.add(id)
    return id

def poser_question(questions=questions, score=score):
    # Fonction qui pose la question avec plusieurs choix; recupére la réponse utilisateur et compte le score
    id = id_question(questions, id_questions_posees)
    print(questions.iloc[id,1])
    answers = list(questions.iloc[id,2:])
    answer = answers[0]
    answers_shuffle = answers.copy()
    rd.shuffle(answers_shuffle)
    for i in range(len(answers_shuffle)):
        print(f"{(i+1)}) {answers_shuffle[i]}")
    user_answer = int(input("Quelle est votre réponse ? "))
    print(answers_shuffle[user_answer-1])
    if answers_shuffle[int(user_answer)-1] == answer : 
        print("Bien joué :)\n")
        score +=1
    else : print(f"FAUX FAUX FAUX ! La bonne réponse était : {answer}\n")

def quizz():
    print("BIENVENUE DANS ... le quizz.\n")
    print("Enchainez une serie de 5 questions et tentez d'obtenir le meilleur score.\n")
    for i in range(5):
        print(f"Quesion {i+1} :")
        poser_question()
    
    print(f"Voici votre score : {score}")

quizz()