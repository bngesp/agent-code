from crewai import Crew
from src.agents.project_agents import manager, dev_backend, dev_frontend, qa_agent
from src.tasks.project_tasks import task_planification, task_backend, task_frontend, task_qa

crew = Crew(
    agents=[manager, dev_backend, dev_frontend, qa_agent],
    tasks=[task_planification, task_backend, task_frontend, task_qa],
    verbose=True
)

def run_project():
    results = crew.kickoff()
    print("=== Résultat final ===")
    print(results)
    return results