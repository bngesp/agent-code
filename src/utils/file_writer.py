import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class FileWriter:
    def __init__(self, output_directory: str = "output"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(exist_ok=True)
        self.project_directory = None
        
    def set_project_directory(self, project_name: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.project_directory = self.output_directory / f"{project_name}_{timestamp}"
        self.project_directory.mkdir(exist_ok=True)
        
    def extract_code_blocks(self, text: str) -> List[Dict[str, str]]:
        code_blocks = []
        
        # Pattern pour les blocs de code avec langage spécifié
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.findall(pattern, text, re.DOTALL)
        
        for language, code in matches:
            if language and code.strip():
                code_blocks.append({
                    'language': language,
                    'code': code.strip()
                })
        
        return code_blocks
    
    def extract_file_structure(self, text: str) -> Dict[str, str]:
        files = {}
        
        # Recherche de structures de fichiers mentionnées
        file_patterns = [
            r'# ([^/\n]+\.(?:js|jsx|ts|tsx|py|html|css|json|md|yml|yaml|dockerfile))\n```\w*\n(.*?)\n```',
            r'## ([^/\n]+\.(?:js|jsx|ts|tsx|py|html|css|json|md|yml|yaml|dockerfile))\n```\w*\n(.*?)\n```',
            r'### ([^/\n]+\.(?:js|jsx|ts|tsx|py|html|css|json|md|yml|yaml|dockerfile))\n```\w*\n(.*?)\n```',
            r'`([^/\n]+\.(?:js|jsx|ts|tsx|py|html|css|json|md|yml|yaml|dockerfile))`:\n```\w*\n(.*?)\n```'
        ]
        
        for pattern in file_patterns:
            matches = re.findall(pattern, text, re.DOTALL)
            for filename, content in matches:
                files[filename.strip()] = content.strip()
        
        return files
    
    def write_code_file(self, filename: str, content: str, subdirectory: str = None):
        if not self.project_directory:
            raise ValueError("Project directory not set. Call set_project_directory first.")
        
        target_dir = self.project_directory
        if subdirectory:
            target_dir = target_dir / subdirectory
            target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path
    
    def write_agent_output(self, agent_role: str, output: str) -> List[str]:
        if not self.project_directory:
            raise ValueError("Project directory not set. Call set_project_directory first.")
        
        created_files = []
        
        # Créer le dossier pour l'agent
        agent_dir = self.project_directory / agent_role.lower().replace(' ', '_')
        agent_dir.mkdir(exist_ok=True)
        
        # Sauvegarder la sortie brute
        raw_output_file = agent_dir / "output.md"
        with open(raw_output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Sortie de l'agent: {agent_role}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(output)
        created_files.append(str(raw_output_file))
        
        # Extraire et sauvegarder les fichiers de code
        extracted_files = self.extract_file_structure(output)
        
        for filename, content in extracted_files.items():
            # Déterminer le sous-dossier basé sur le type de fichier
            subdirectory = self._get_subdirectory_for_file(filename)
            file_path = self.write_code_file(filename, content, subdirectory)
            created_files.append(str(file_path))
        
        # Si aucun fichier structuré n'est trouvé, extraire les blocs de code
        if not extracted_files:
            code_blocks = self.extract_code_blocks(output)
            for i, block in enumerate(code_blocks):
                extension = self._get_extension_for_language(block['language'])
                filename = f"code_{i+1}.{extension}"
                subdirectory = self._get_subdirectory_for_language(block['language'])
                file_path = self.write_code_file(filename, block['code'], subdirectory)
                created_files.append(str(file_path))
        
        return created_files
    
    def _get_subdirectory_for_file(self, filename: str) -> str:
        if filename.endswith(('.js', '.jsx', '.ts', '.tsx', '.html', '.css')):
            return 'frontend'
        elif filename.endswith('.py'):
            return 'backend'
        elif filename.endswith(('.json', '.yml', '.yaml', '.dockerfile')):
            return 'config'
        elif filename.endswith('.md'):
            return 'docs'
        else:
            return 'misc'
    
    def _get_subdirectory_for_language(self, language: str) -> str:
        frontend_languages = ['javascript', 'typescript', 'jsx', 'tsx', 'html', 'css', 'scss', 'sass']
        backend_languages = ['python', 'node', 'nodejs']
        config_languages = ['json', 'yaml', 'yml', 'dockerfile', 'docker']
        
        if language.lower() in frontend_languages:
            return 'frontend'
        elif language.lower() in backend_languages:
            return 'backend'
        elif language.lower() in config_languages:
            return 'config'
        else:
            return 'misc'
    
    def _get_extension_for_language(self, language: str) -> str:
        extensions = {
            'javascript': 'js',
            'typescript': 'ts',
            'jsx': 'jsx',
            'tsx': 'tsx',
            'python': 'py',
            'html': 'html',
            'css': 'css',
            'scss': 'scss',
            'sass': 'sass',
            'json': 'json',
            'yaml': 'yml',
            'yml': 'yml',
            'dockerfile': 'dockerfile',
            'docker': 'dockerfile',
            'bash': 'sh',
            'shell': 'sh',
            'sql': 'sql'
        }
        return extensions.get(language.lower(), 'txt')
    
    def write_project_summary(self, project_name: str, agents_used: List[str], files_created: Dict[str, List[str]]):
        if not self.project_directory:
            raise ValueError("Project directory not set. Call set_project_directory first.")
        
        summary_file = self.project_directory / "PROJECT_SUMMARY.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# {project_name}\n\n")
            f.write(f"Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Agents utilisés\n\n")
            for agent in agents_used:
                f.write(f"- {agent}\n")
            
            f.write("\n## Fichiers créés\n\n")
            for agent, files in files_created.items():
                f.write(f"### {agent}\n\n")
                for file_path in files:
                    f.write(f"- `{file_path}`\n")
                f.write("\n")
            
            f.write("## Structure du projet\n\n")
            f.write("```\n")
            self._write_tree_structure(f, self.project_directory, prefix="")
            f.write("```\n")
    
    def _write_tree_structure(self, f, directory: Path, prefix: str = ""):
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name))
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            
            current_prefix = "└── " if is_last else "├── "
            f.write(f"{prefix}{current_prefix}{item.name}\n")
            
            if item.is_dir():
                next_prefix = prefix + ("    " if is_last else "│   ")
                self._write_tree_structure(f, item, next_prefix)