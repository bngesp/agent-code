#!/usr/bin/env python3

from src.agents.smart_manager import SmartManager

def example_simple_project():
    """Exemple d'utilisation pour un projet simple"""
    print("📝 Exemple 1: Projet simple - To-Do App")
    print("-" * 40)
    
    smart_manager = SmartManager()
    user_prompt = "Je veux créer une simple application de to-do list avec React"
    
    result = smart_manager.execute_dynamic_project(user_prompt)
    print(f"Résultat: {result[:200]}...")

def example_complex_project():
    """Exemple d'utilisation pour un projet complexe"""
    print("\n🏢 Exemple 2: Projet complexe - E-commerce Platform")
    print("-" * 50)
    
    smart_manager = SmartManager()
    user_prompt = """
    Je veux créer une plateforme e-commerce complète avec :
    - Frontend React avec panier et paiement
    - Backend Node.js avec API REST 
    - Base de données PostgreSQL
    - Authentification JWT
    - Tests automatisés
    - Déploiement Docker
    """
    
    result = smart_manager.execute_dynamic_project(user_prompt)
    print(f"Résultat: {result[:300]}...")

def example_data_project():
    """Exemple d'utilisation pour un projet data"""
    print("\n📊 Exemple 3: Projet Data - Analytics Dashboard")
    print("-" * 45)
    
    smart_manager = SmartManager()
    user_prompt = """
    Développer un dashboard d'analytics avec :
    - Ingestion de données en temps réel
    - API Python FastAPI pour les données
    - Frontend avec graphiques D3.js
    - Machine Learning pour prédictions
    - Base de données time-series
    """
    
    result = smart_manager.execute_dynamic_project(user_prompt)
    print(f"Résultat: {result[:300]}...")

def example_custom_analysis():
    """Exemple d'analyse manuelle des besoins"""
    print("\n🔍 Exemple 4: Analyse manuelle des besoins")
    print("-" * 45)
    
    smart_manager = SmartManager()
    user_prompt = "Application de chat vidéo avec WebRTC et React Native"
    
    # Étape 1: Analyser seulement
    analysis = smart_manager.analyze_project_needs(user_prompt)
    print("Analyse brute:")
    print(analysis[:400] + "...")
    
    # Étape 2: Parser l'analyse
    parsed = smart_manager.parse_analysis_result(analysis)
    print(f"\nAgents identifiés: {len(parsed.get('agents_needed', []))}")
    for agent in parsed.get('agents_needed', []):
        print(f"- {agent.get('role', 'N/A')} ({agent.get('priority', 'N/A')})")

if __name__ == "__main__":
    print("🤖 Exemples d'utilisation du SmartManager")
    print("=" * 50)
    
    try:
        # Exécuter les exemples
        example_simple_project()
        example_complex_project() 
        example_data_project()
        example_custom_analysis()
        
    except Exception as e:
        print(f"❌ Erreur dans les exemples : {e}")
    
    print("\n✅ Exemples terminés")