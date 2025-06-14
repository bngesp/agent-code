from crewai import Agent
from src.config.llm_config import get_llm

llm = get_llm()

manager = Agent(
    role="Project Manager",
    goal="Organiser et planifier le développement d'une application logicielle à partir d'une idée fournie.",
    backstory="Expert en gestion de projet agile, capable de décomposer n'importe quel projet en tâches claires pour chaque profil technique.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

dev_backend = Agent(
    role="Développeur Backend",
    goal="Écrire un backend robuste, sécurisé et scalable selon les spécifications du projet.",
    backstory="Développeur chevronné spécialisé dans les API REST, Node.js et bases de données relationnelles.",
    verbose=True,
    llm=llm
)

dev_frontend = Agent(
    role="Développeur Frontend",
    goal="Créer une interface utilisateur intuitive et réactive selon la maquette ou les consignes du projet.",
    backstory="Développeur frontend passionné par React et les bonnes pratiques UX/UI.",
    verbose=True,
    llm=llm
)

qa_agent = Agent(
    role="Testeur QA",
    goal="Tester l'application pour détecter des bugs, des erreurs de logique, et assurer la conformité avec les spécifications.",
    backstory="Expert en tests fonctionnels, automatisés, et manuels, garant de la qualité logicielle.",
    verbose=True,
    llm=llm
)