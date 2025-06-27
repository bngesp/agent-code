from crewai import Agent, Task, Crew
from src.config.llm_config import get_llm
from src.utils.file_writer import FileWriter
import re
import json
from typing import List, Dict

class SmartManager:
    def __init__(self):
        self.llm = get_llm()
        self.manager_agent = self._create_manager_agent()
        self.file_writer = FileWriter()
        
    def _create_manager_agent(self) -> Agent:
        return Agent(
            role="Smart Project Manager",
            goal="Analyser intelligemment les projets logiciels et orchestrer dynamiquement des équipes d'agents spécialisés.",
            backstory="""Expert en architecture logicielle et gestion agile avec 15 ans d'expérience. 
            Capable d'analyser la complexité d'un projet, d'identifier les compétences requises et de structurer 
            des équipes optimales. Maîtrise parfaitement les patterns de développement modernes.""",
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )
    
    def analyze_project_needs(self, user_prompt: str) -> str:
        planning_task = Task(
            description=f"""
            Analyse approfondie du projet suivant : "{user_prompt}"
            
            Tu dois :
            1. Évaluer la complexité technique du projet
            2. Identifier tous les composants nécessaires (frontend, backend, database, auth, tests, etc.)
            3. Déterminer les rôles d'agents requis pour chaque composant
            4. Proposer un plan d'exécution avec priorités
            
            Format de réponse attendu (JSON) :
            {{
                "complexity": "simple|medium|complex",
                "components": ["frontend", "backend", "database", "auth", "tests", "devops", "documentation"],
                "agents_needed": [
                    {{
                        "role": "Backend Developer",
                        "priority": "high",
                        "skills": ["API", "Database", "Authentication"],
                        "tasks": ["Créer l'API REST", "Configurer la base de données"]
                    }}
                ],
                "execution_plan": "Description du plan d'exécution"
            }}
            """,
            expected_output="Analyse complète du projet au format JSON avec agents requis et plan d'exécution",
            agent=self.manager_agent
        )
        
        # Exécuter l'analyse
        crew = Crew(agents=[self.manager_agent], tasks=[planning_task], verbose=False)
        result = crew.kickoff()
        return str(result)
    
    def parse_analysis_result(self, analysis_result: str) -> Dict:
        try:
            # Extraire le JSON de la réponse
            json_match = re.search(r'\{.*\}', analysis_result, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                return json.loads(json_str)
        except:
            pass
        
        # Fallback: parsing manuel si JSON invalide
        return self._fallback_parsing(analysis_result)
    
    def _fallback_parsing(self, analysis_result: str) -> Dict:
        agents_needed = []
        text_lower = analysis_result.lower()
        
        # Détection des besoins par mots-clés
        if any(word in text_lower for word in ['api', 'backend', 'serveur', 'base de données']):
            agents_needed.append({
                "role": "Backend Developer",
                "priority": "high",
                "skills": ["API", "Database", "Security"],
                "tasks": ["Développer l'API REST", "Configurer la persistance des données"]
            })
        
        if any(word in text_lower for word in ['interface', 'frontend', 'ui', 'react', 'vue']):
            agents_needed.append({
                "role": "Frontend Developer", 
                "priority": "high",
                "skills": ["React", "UI/UX", "Integration"],
                "tasks": ["Créer l'interface utilisateur", "Intégrer avec l'API"]
            })
        
        if any(word in text_lower for word in ['test', 'qa', 'qualité']):
            agents_needed.append({
                "role": "QA Engineer",
                "priority": "medium", 
                "skills": ["Testing", "Automation", "Quality"],
                "tasks": ["Écrire les tests", "Valider la qualité"]
            })
        
        if any(word in text_lower for word in ['déploiement', 'devops', 'docker', 'ci/cd']):
            agents_needed.append({
                "role": "DevOps Engineer",
                "priority": "medium",
                "skills": ["Docker", "CI/CD", "Cloud"],
                "tasks": ["Configurer le déploiement", "Optimiser l'infrastructure"]
            })
        
        return {
            "complexity": "medium",
            "agents_needed": agents_needed,
            "execution_plan": "Plan d'exécution adaptatif basé sur l'analyse"
        }
    
    def create_dynamic_agents(self, agents_specs: List[Dict]) -> List[Agent]:
        agents = []
        
        for spec in agents_specs:
            role = spec.get("role", "Generic Developer")
            skills = spec.get("skills", [])
            
            agent = Agent(
                role=role,
                goal=f"Exceller dans le rôle de {role} en utilisant les compétences : {', '.join(skills)}",
                backstory=self._generate_backstory(role, skills),
                verbose=True,
                llm=self.llm
            )
            agents.append(agent)
        
        return agents
    
    def _generate_backstory(self, role: str, skills: List[str]) -> str:
        backstories = {
            "Backend Developer": f"Développeur backend expert avec 8+ ans d'expérience. Spécialisé en {', '.join(skills)}. Passionné par l'architecture scalable et la sécurité.",
            "Frontend Developer": f"Développeur frontend créatif avec expertise en {', '.join(skills)}. Obsédé par l'expérience utilisateur et les performances.",
            "QA Engineer": f"Ingénieur QA rigoureux spécialisé en {', '.join(skills)}. Expert en détection de bugs et amélioration continue.",
            "DevOps Engineer": f"Ingénieur DevOps avec expertise en {', '.join(skills)}. Spécialiste de l'automatisation et de l'infrastructure cloud.",
            "Data Scientist": f"Data Scientist avec expertise en {', '.join(skills)}. Passionné par l'analyse de données et l'IA.",
            "Security Engineer": f"Expert en cybersécurité spécialisé en {', '.join(skills)}. Gardien de la sécurité des applications."
        }
        
        return backstories.get(role, f"Expert {role} avec compétences en {', '.join(skills)}")
    
    def create_dynamic_tasks(self, agents: List[Agent], agents_specs: List[Dict]) -> List[Task]:
        tasks = []
        
        for agent, spec in zip(agents, agents_specs):
            role = spec.get("role", "Generic Developer")
            task_descriptions = spec.get("tasks", [f"Exécuter les tâches du rôle {role}"])
            
            for task_desc in task_descriptions:
                enhanced_description = f"""
                {task_desc}
                
                IMPORTANT: Votre réponse doit contenir du code prêt à être utilisé.
                Formatez votre code dans des blocs avec le langage spécifié :
                ```javascript
                // Code JavaScript ici
                ```
                
                ```python
                # Code Python ici
                ```
                
                Organisez votre réponse de manière structurée avec :
                1. Description de la solution
                2. Code source avec noms de fichiers explicites
                3. Instructions d'installation/utilisation si nécessaire
                
                Exemple de format attendu:
                ## app.js
                ```javascript
                const express = require('express');
                // ... reste du code
                ```
                
                ## package.json  
                ```json
                {{
                  "name": "mon-projet",
                  // ... reste de la configuration
                }}
                ```
                """
                
                task = Task(
                    description=enhanced_description,
                    expected_output=f"Code source fonctionnel et structuré pour : {task_desc}",
                    agent=agent
                )
                tasks.append(task)
        
        return tasks
    
    def execute_dynamic_project(self, user_prompt: str) -> str:
        print(f"🧠 Analyse du projet : {user_prompt}")
        
        # Préparer le répertoire de sortie
        project_name = self._generate_project_name(user_prompt)
        self.file_writer.set_project_directory(project_name)
        print(f"📁 Répertoire de sortie créé : {self.file_writer.project_directory}")
        
        # 1. Analyser les besoins
        analysis_result = self.analyze_project_needs(user_prompt)
        print("📋 Analyse terminée")
        
        # 2. Parser le résultat
        parsed_analysis = self.parse_analysis_result(analysis_result)
        
        # Afficher le plan d'exécution
        execution_plan = parsed_analysis.get("execution_plan", "Aucun plan d'exécution détaillé fourni.")
        print("\n" + "="*70)
        print("🎯 PLAN D'ÉXÉCUTION")
        print("="*70)
        print(execution_plan)
        print("="*70 + "\n")
        
        # 3. Créer les agents dynamiquement
        agents_specs = parsed_analysis.get("agents_needed", [])
        if not agents_specs:
            print("⚠️ Aucun agent spécialisé requis, utilisation du manager seul")
            # ... (gestion du cas sans agent)
            return "Aucun agent spécialisé n'a été jugé nécessaire pour ce projet."

        agents = self.create_dynamic_agents(agents_specs)
        tasks = self.create_dynamic_tasks(agents, agents_specs)
        
        # 4. Exécuter le projet séquentiellement
        print(f"🚀 Lancement de l'exécution séquentielle de {len(tasks)} tâches")
        
        execution_context = []
        final_result = ""

        for i, task in enumerate(tasks):
            agent_role = task.agent.role
            print(f"\n" + "-"*70)
            print(f"Étape {i+1}/{len(tasks)} : Exécution par {agent_role}")
            print(f"Tâche : {task.description.split('IMPORTANT')[0].strip()}")
            print("-" * 70)

            # Injecter le contexte des tâches précédentes
            if execution_context:
                task.description = f"Contexte des étapes précédentes :\n{''.join(execution_context)}\n\n{task.description}"

            # Exécuter la tâche
            crew = Crew(agents=[task.agent], tasks=[task], verbose=False)
            task_output = crew.kickoff()
            
            # Sauvegarder le résultat de la tâche
            execution_context.append(f"Résultat de {agent_role}:\n{task_output}\n")
            final_result += f"--- Résultat de {agent_role} ---\n{task_output}\n\n"
            
            print(f"✅ Étape {i+1} terminée.")

        # 5. Sauvegarder les résultats et extraire les fichiers de code
        print("\n💾 Sauvegarde des fichiers générés...")
        created_files = self.file_writer.write_agent_output("Combined_Output", final_result)
        
        # 6. Créer le résumé du projet
        agents_used = [agent.role for agent in agents]
        files_created_summary = {"Combined_Output": created_files}
        self.file_writer.write_project_summary(project_name, agents_used, files_created_summary)
        
        total_files = len(created_files)
        print(f"🎉 Projet terminé ! {total_files} fichiers créés dans {self.file_writer.project_directory}")
        
        return final_result
    
    def _generate_project_name(self, user_prompt: str) -> str:
        # Générer un nom de projet basé sur le prompt utilisateur
        words = user_prompt.lower().split()
        # Garder les mots significatifs et enlever les mots vides
        stop_words = {'le', 'la', 'les', 'un', 'une', 'des', 'de', 'du', 'avec', 'pour', 'et', 'ou', 'dans', 'sur'}
        meaningful_words = [word for word in words if word not in stop_words and len(word) > 2][:3]
        
        if meaningful_words:
            return "_".join(meaningful_words)
        else:
            return "projet_agent"
    