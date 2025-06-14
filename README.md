# Agent Code - Système Multi-Agents avec CrewAI

Un projet Python utilisant CrewAI pour orchestrer une équipe d'agents IA spécialisés dans le développement logiciel. Chaque agent a un rôle spécifique : Project Manager, Backend Developer, Frontend Developer, et QA Tester.

## Fonctionnalités

- **Manager** : Analyse les besoins et crée un plan de projet structuré
- **Backend Developer** : Développe les API et la logique serveur
- **Frontend Developer** : Crée l'interface utilisateur
- **QA Tester** : Teste et valide la conformité du projet

## Structure du Projet

```
agent-code/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── project_agents.py      # Définition des 4 agents IA
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── project_tasks.py       # Tâches assignées à chaque agent
│   ├── crews/
│   │   ├── __init__.py
│   │   └── project_crew.py        # Configuration de l'équipe d'agents
│   ├── config/
│   │   ├── __init__.py
│   │   └── llm_config.py          # Configuration des modèles LLM
│   └── __init__.py
├── tests/                         # Tests unitaires
├── main.py                        # Point d'entrée principal
├── requirements.txt               # Dépendances Python
├── .env.example                   # Variables d'environnement
├── .gitignore                     # Fichiers ignorés par Git
└── README.md                      # Documentation
```

##  Installation

### 1. Cloner le repository
```bash
git clone <repository-url>
cd agent-code
```

### 2. Créer l'environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration des variables d'environnement
```bash
cp .env.example .env
```

Modifiez le fichier `.env` avec vos clés API :
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-4
OPENAI_API_BASE=https://api.openai.com/v1
```

##  Utilisation

### Lancement du projet
```bash
python main.py
```

### Personnalisation des tâches
Modifiez le fichier `src/tasks/project_tasks.py` pour adapter les tâches :
```python
user_input = "Votre idée de projet ici"
```

##  Agents Disponibles

### 1. Project Manager
- **Rôle** : Planification et organisation
- **Objectif** : Décomposer le projet en tâches claires
- **Spécialités** : Gestion de projet agile, coordination d'équipe

### 2. Backend Developer  
- **Rôle** : Développement serveur
- **Objectif** : Créer des API robustes et sécurisées
- **Spécialités** : Node.js, Express, bases de données

### 3. Frontend Developer
- **Rôle** : Développement interface utilisateur
- **Objectif** : Créer des interfaces intuitives
- **Spécialités** : React, UX/UI, intégration API

### 4. QA Tester
- **Rôle** : Assurance qualité
- **Objectif** : Détecter bugs et valider conformité
- **Spécialités** : Tests fonctionnels, automatisés, manuels

##  Configuration Avancée

### Modification des agents
Personnalisez les agents dans `src/agents/project_agents.py` :
```python
manager = Agent(
    role="Votre rôle personnalisé",
    goal="Votre objectif",
    backstory="Votre contexte",
    verbose=True,
    llm=llm
)
```

### Configuration LLM
Ajustez les paramètres dans `src/config/llm_config.py` :
```python
def get_llm(model="gpt-4", temperature=0.3):
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
```

## Tests

```bash
# Lancer les tests
python -m pytest tests/

# Avec couverture
python -m pytest tests/ --cov=src
```

##  Dépendances Principales

- **crewai** : Framework multi-agents
- **langchain** : Intégration LLM
- **python-dotenv** : Gestion variables d'environnement
- **pydantic** : Validation des données

##  Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Consultez la documentation CrewAI
- Vérifiez les logs d'exécution

---

**Développé avec ❤️ en utilisant CrewAI et LangChain**