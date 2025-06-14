# run_project.py
from crewai import Crew
from setup import manager, dev_backend, dev_frontend, qa_agent
from tasks_setup import task_planification, task_backend, task_frontend, task_qa

crew = Crew(
    agents=[manager, dev_backend, dev_frontend, qa_agent],
    tasks=[task_planification, task_backend, task_frontend, task_qa],
    verbose=True
)

results = crew.kickoff()
print("=== Résultat final ===")
print(results)
