#!/usr/bin/env python3

from src.agents.smart_manager import SmartManager

def main():
    print("🤖 Agent Code - Système Multi-Agents Intelligent")
    print("=" * 50)
    
    # Créer le SmartManager
    smart_manager = SmartManager()
    
    # Exemple de projets
    exemple_projets = [
        "Je veux une application de prise de notes avec authentification et sauvegarde cloud",
        "Créer une API REST pour un e-commerce avec gestion des produits et commandes",
        "Développer un dashboard analytics avec graphiques temps réel",
        "Application mobile de chat en temps réel avec React Native"
    ]
    
    print("\n📋 Exemples de projets disponibles :")
    for i, projet in enumerate(exemple_projets, 1):
        print(f"{i}. {projet}")
    
    print("\n0. Saisir un projet personnalisé")
    
    try:
        choix = input("\nChoisissez un projet (0-4) : ").strip()
        
        if choix == "0":
            user_prompt = input("Décrivez votre projet : ").strip()
        elif choix.isdigit() and 1 <= int(choix) <= len(exemple_projets):
            user_prompt = exemple_projets[int(choix) - 1]
        else:
            print("Choix invalide, utilisation du projet par défaut")
            user_prompt = exemple_projets[0]
        
        if not user_prompt:
            print("Aucune description fournie, utilisation du projet par défaut")
            user_prompt = exemple_projets[0]
        
        print(f"\n🎯 Projet sélectionné : {user_prompt}")
        print("\n" + "="*70)
        
        # Exécuter le projet avec le SmartManager
        result = smart_manager.execute_dynamic_project(user_prompt)
        
        print("\n" + "="*70)
        print("🎉 RÉSULTAT FINAL")
        print("="*70)
        print(result)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Interruption utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")

if __name__ == "__main__":
    main()