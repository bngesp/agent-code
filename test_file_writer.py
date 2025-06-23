#!/usr/bin/env python3

import os
from src.agents.smart_manager import SmartManager

def test_file_writing():
    print("🧪 Test de la fonctionnalité d'écriture de fichiers")
    print("=" * 50)
    
    # Créer le SmartManager
    smart_manager = SmartManager()
    
    # Projet de test simple
    test_project = "Créer une simple page HTML avec du CSS"
    
    print(f"📝 Projet de test : {test_project}")
    print("\n🚀 Exécution du projet...")
    
    try:
        # Exécuter le projet
        result = smart_manager.execute_dynamic_project(test_project)
        
        print(f"\n✅ Projet terminé avec succès!")
        print(f"📁 Répertoire de sortie: {smart_manager.file_writer.project_directory}")
        
        # Vérifier si des fichiers ont été créés
        if smart_manager.file_writer.project_directory and smart_manager.file_writer.project_directory.exists():
            files = list(smart_manager.file_writer.project_directory.rglob("*.*"))
            print(f"🗂️  {len(files)} fichiers créés:")
            for file in files:
                print(f"   - {file.relative_to(smart_manager.file_writer.project_directory)}")
        else:
            print("⚠️  Aucun répertoire de sortie trouvé")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Vérifier les variables d'environnement
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Variable d'environnement OPENAI_API_KEY non définie")
        print("🔧 Pour tester avec une vraie API, définissez votre clé OpenAI")
        print("💡 Pour ce test, nous utiliserons un mode simulation")
        
    test_file_writing()