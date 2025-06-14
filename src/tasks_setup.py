# tasks_setup.py
from crewai import Task
from setup import manager, dev_backend, dev_frontend, qa_agent

# Input utilisateur
user_input = "Je veux une application de prise de notes en ligne avec sauvegarde cloud."

# 1. Tâche du Manager
task_planification = Task(
    description=f"Analyse le besoin suivant : '{user_input}' et crée un plan de projet détaillé. Identifie les composants front, back, et QA.",
    expected_output="Un plan de projet structuré avec les tâches réparties entre le frontend, backend, et QA.",
    agent=manager
)

# 2. Tâches pour les Devs
task_backend = Task(
    description="Développe les endpoints backend nécessaires pour gérer les utilisateurs, les notes, et la persistance cloud. Utilise Express.js et MongoDB.",
    expected_output="Un dossier 'backend/' avec les endpoints Node.js opérationnels.",
    agent=dev_backend
)

task_frontend = Task(
    description="Crée une interface web simple avec React permettant de créer, modifier et afficher des notes. Utilise les endpoints backend existants.",
    expected_output="Un dossier 'frontend/' avec une app React fonctionnelle.",
    agent=dev_frontend
)

# 3. Tâche de QA
task_qa = Task(
    description="Teste le frontend et le backend de l'application. Vérifie que toutes les fonctionnalités marchent. Documente les bugs éventuels et vérifie la conformité avec le cahier des charges.",
    expected_output="Rapport de test avec résultats, bugs détectés, et suggestions d'amélioration.",
    agent=qa_agent
)
