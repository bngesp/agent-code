#!/usr/bin/env python3

import argparse
import sys
import os
from pathlib import Path
from .agents.smart_manager import SmartManager

def main():
    parser = argparse.ArgumentParser(
        description="Agent Code - Générateur de code avec agents IA spécialisés",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'usage:
  agent-code "Créer une API REST pour un e-commerce"
  agent-code "Application React avec authentification" --verbose
  agent-code --interactive
  
Le code généré sera placé dans le répertoire courant.
        """
    )
    
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Description du projet à générer"
    )
    
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Mode interactif avec menu de sélection"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Affichage détaillé du processus"
    )
    
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Répertoire de sortie (défaut: répertoire courant)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Agent Code 1.0.0"
    )
    
    args = parser.parse_args()
    
    # Vérifier les variables d'environnement nécessaires
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Erreur: La variable d'environnement OPENAI_API_KEY est requise")
        print("   Définissez votre clé API OpenAI avec:")
        print("   export OPENAI_API_KEY='votre-clé-api'")
        sys.exit(1)
    
    try:
        if args.interactive or not args.prompt:
            result = run_interactive_mode(args.output_dir, args.verbose)
        else:
            result = run_direct_mode(args.prompt, args.output_dir, args.verbose)
            
        if args.verbose:
            print("\n" + "="*70)
            print("🎉 RÉSULTAT FINAL")
            print("="*70)
            print(result)
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Interruption utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

def run_interactive_mode(output_dir: str, verbose: bool):
    """Mode interactif avec menu de sélection"""
    print("🤖 Agent Code - Système Multi-Agents Intelligent")
    print("=" * 50)
    
    exemple_projets = [
        "Je veux une application de prise de notes avec authentification et sauvegarde cloud",
        "Créer une API REST pour un e-commerce avec gestion des produits et commandes",
        "Développer un dashboard analytics avec graphiques temps réel",
        "Application mobile de chat en temps réel avec React Native",
        "Bot Discord avec commandes personnalisées",
        "Système de gestion de tâches avec notifications"
    ]
    
    print("\n📋 Exemples de projets disponibles :")
    for i, projet in enumerate(exemple_projets, 1):
        print(f"{i}. {projet}")
    
    print("\n0. Saisir un projet personnalisé")
    
    choix = input("\nChoisissez un projet (0-{}) : ".format(len(exemple_projets))).strip()
    
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
    print(f"📁 Répertoire de sortie : {Path(output_dir).absolute()}")
    print("\n" + "="*70)
    
    return execute_project(user_prompt, output_dir, verbose)

def run_direct_mode(prompt: str, output_dir: str, verbose: bool):
    """Mode direct avec prompt en argument"""
    print("🤖 Agent Code - Génération en cours...")
    print(f"🎯 Projet : {prompt}")
    print(f"📁 Répertoire de sortie : {Path(output_dir).absolute()}")
    
    if verbose:
        print("\n" + "="*70)
    
    return execute_project(prompt, output_dir, verbose)

def execute_project(user_prompt: str, output_dir: str, verbose: bool):
    """Exécute le projet avec le SmartManager"""
    
    # Changer vers le répertoire de sortie
    original_cwd = Path.cwd()
    output_path = Path(output_dir).absolute()
    
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
    
    os.chdir(output_path)
    
    try:
        # Créer le SmartManager avec le répertoire courant
        smart_manager = SmartManager()
        
        # Configurer le FileWriter pour utiliser le répertoire courant
        smart_manager.file_writer = smart_manager.file_writer.__class__(output_directory=None)
        
        # Exécuter le projet
        result = smart_manager.execute_dynamic_project(user_prompt)
        
        return result
        
    finally:
        # Revenir au répertoire original
        os.chdir(original_cwd)

if __name__ == "__main__":
    main()