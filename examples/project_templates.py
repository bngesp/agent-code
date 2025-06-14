#!/usr/bin/env python3

"""
Templates de projets prédéfinis pour tester le SmartManager
"""

PROJECT_TEMPLATES = {
    "web_app": {
        "name": "Application Web Complète",
        "description": "Créer une application web avec frontend React, backend Node.js, base de données PostgreSQL et authentification",
        "complexity": "medium",
        "expected_agents": ["Frontend Developer", "Backend Developer", "QA Engineer"]
    },
    
    "mobile_app": {
        "name": "Application Mobile",
        "description": "Développer une application mobile cross-platform avec React Native, API REST et push notifications",
        "complexity": "medium", 
        "expected_agents": ["Mobile Developer", "Backend Developer", "QA Engineer"]
    },
    
    "api_service": {
        "name": "Service API",
        "description": "Créer une API REST robuste avec FastAPI, documentation OpenAPI, tests automatisés et containerisation Docker",
        "complexity": "simple",
        "expected_agents": ["Backend Developer", "DevOps Engineer"]
    },
    
    "data_pipeline": {
        "name": "Pipeline de Données",
        "description": "Construire un pipeline ETL avec ingestion temps réel, traitement Apache Spark, stockage data lake et dashboard Grafana",
        "complexity": "complex",
        "expected_agents": ["Data Engineer", "Backend Developer", "DevOps Engineer", "QA Engineer"]
    },
    
    "ml_project": {
        "name": "Projet Machine Learning",
        "description": "Développer un modèle ML avec preprocessing des données, entraînement, API de prédiction et monitoring MLOps",
        "complexity": "complex",
        "expected_agents": ["Data Scientist", "Backend Developer", "DevOps Engineer"]
    },
    
    "ecommerce": {
        "name": "Plateforme E-commerce",
        "description": "Créer une plateforme e-commerce avec catalogue produits, panier, paiement Stripe, gestion commandes et admin panel",
        "complexity": "complex",
        "expected_agents": ["Frontend Developer", "Backend Developer", "QA Engineer", "DevOps Engineer"]
    },
    
    "blog_cms": {
        "name": "CMS/Blog",
        "description": "Développer un système de gestion de contenu avec éditeur WYSIWYG, gestion utilisateurs et SEO",
        "complexity": "simple",
        "expected_agents": ["Frontend Developer", "Backend Developer"]
    },
    
    "chat_app": {
        "name": "Application de Chat",
        "description": "Créer une application de chat temps réel avec WebSocket, salles de discussion, partage de fichiers",
        "complexity": "medium",
        "expected_agents": ["Frontend Developer", "Backend Developer", "QA Engineer"]
    },
    
    "iot_platform": {
        "name": "Plateforme IoT",
        "description": "Développer une plateforme IoT avec ingestion de données capteurs, dashboard temps réel, alertes et contrôle à distance",
        "complexity": "complex", 
        "expected_agents": ["Backend Developer", "Frontend Developer", "Data Engineer", "DevOps Engineer"]
    },
    
    "game_backend": {
        "name": "Backend de Jeu",
        "description": "Créer un backend de jeu multijoueur avec matchmaking, leaderboards, micro-transactions et anti-triche",
        "complexity": "complex",
        "expected_agents": ["Backend Developer", "Game Developer", "DevOps Engineer", "QA Engineer"]
    }
}

def get_template(template_name: str) -> dict:
    """Récupère un template de projet par son nom"""
    return PROJECT_TEMPLATES.get(template_name, {})

def list_templates() -> list:
    """Liste tous les templates disponibles"""
    return list(PROJECT_TEMPLATES.keys())

def get_template_description(template_name: str) -> str:
    """Récupère la description d'un template"""
    template = get_template(template_name)
    return template.get("description", "Template non trouvé")

if __name__ == "__main__":
    print("📋 Templates de projets disponibles :")
    print("=" * 50)
    
    for name, template in PROJECT_TEMPLATES.items():
        print(f"\n🎯 {template['name']} ({name})")
        print(f"   Complexité: {template['complexity']}")
        print(f"   Description: {template['description']}")
        print(f"   Agents attendus: {', '.join(template['expected_agents'])}")