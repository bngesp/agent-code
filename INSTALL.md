# Installation et Utilisation CLI

## Installation

### Option 1: Installation en mode développement
```bash
cd /path/to/agent-code
pip install -e .
```

### Option 2: Installation depuis le répertoire
```bash
cd /path/to/agent-code
pip install .
```

### Option 3: Installation avec pipx (recommandé)
```bash
cd /path/to/agent-code
pipx install .
```

## Configuration

Définissez votre clé API OpenAI :
```bash
export OPENAI_API_KEY='votre-clé-api-openai'
```

Pour une configuration permanente, ajoutez à votre `.bashrc` ou `.zshrc` :
```bash
echo 'export OPENAI_API_KEY="votre-clé-api-openai"' >> ~/.bashrc
source ~/.bashrc
```

## Utilisation

### Mode interactif
```bash
agent-code --interactive
```

### Mode direct
```bash
agent-code "Créer une API REST pour un e-commerce"
```

### Options disponibles
```bash
agent-code --help
```

### Exemples d'usage
```bash
# Génération dans le répertoire courant
cd /mon/projet
agent-code "Application React avec authentification"

# Mode verbose pour voir les détails
agent-code "Bot Discord avec commandes" --verbose

# Spécifier un répertoire de sortie
agent-code "Dashboard analytics" --output-dir ./nouveau-projet
```

## Désinstallation

```bash
pip uninstall agent-code
# ou avec pipx
pipx uninstall agent-code
```

## Fonctionnement

1. L'outil utilise le **répertoire courant** comme base
2. Crée un dossier `{nom_projet}_{timestamp}` 
3. Organise le code en sous-dossiers : `frontend/`, `backend/`, `config/`, etc.
4. Génère un résumé du projet `PROJECT_SUMMARY.md`

## Résolution des problèmes

- **Erreur API Key** : Vérifiez que `OPENAI_API_KEY` est définie
- **Erreur d'import** : Réinstallez avec `pip install -e .`
- **Permissions** : Utilisez `pipx` pour une installation isolée