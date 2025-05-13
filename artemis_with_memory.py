# artemis_with_memory.py

import tkinter as tk
from transformers import pipeline

# Chargement du pipeline QA
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased")

# Fichier pour sauvegarder l'historique des interactions
HISTORIQUE_FICHIER = "historique.txt"

# Fonction pour charger l'historique depuis le fichier
def charger_historique():
    try:
        with open(HISTORIQUE_FICHIER, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Fonction pour sauvegarder l'historique dans un fichier
def sauvegarder_historique(question, reponse):
    with open(HISTORIQUE_FICHIER, 'a') as file:
        file.write(f"Question : {question}\nRéponse : {reponse}\n\n")

# Fonction de réponse IA avec historique
def poser_question():
    question = question_entry.get()
    if not question.strip():
        reponse_label.config(text="Pose une vraie question !")
        return

    # Charger l'historique précédent
    historique = charger_historique()

    # Définir le contexte comme étant l'historique des questions et réponses
    context = historique + """
    A.R.T.E.M.I.S est une intelligence artificielle conçue pour répondre aux questions posées par les humains.
    Elle utilise des modèles de langage basés sur des réseaux de neurones profonds, comme BERT ou ses variantes.
    """

    try:
        result = qa_pipeline(question=question, context=context)
        reponse = result['answer']
    except Exception as e:
        reponse = f"Erreur: {str(e)}"
    
    # Sauvegarder cette nouvelle interaction
    sauvegarder_historique(question, reponse)

    reponse_label.config(text="Réponse : " + reponse)

# Interface Graphique
fenetre = tk.Tk()
fenetre.title("A.R.T.E.M.I.S - IA Question Answering avec Mémoire")
fenetre.geometry("600x400")

titre = tk.Label(fenetre, text="A.R.T.E.M.I.S - Assistant IA", font=("Helvetica", 18, "bold"))
titre.pack(pady=10)

question_label = tk.Label(fenetre, text="Pose ta question ci-dessous :", font=("Helvetica", 12))
question_label.pack(pady=5)

question_entry = tk.Entry(fenetre, width=80)
question_entry.pack(pady=5)

bouton_question = tk.Button(fenetre, text="Poser la question", command=poser_question)
bouton_question.pack(pady=10)

reponse_label = tk.Label(fenetre, text="", wraplength=500, font=("Helvetica", 12), justify="left")
reponse_label.pack(pady=20)

fenetre.mainloop()
