from crewai import Crew,Process
from tasks import uml_task,code_task
from agents import uml_generator,code_generator

crew=Crew(
    agents=[uml_generator,code_generator],
    tasks=[uml_task,code_task],
    process=Process.sequential,

)


result=crew.kickoff(inputs={'topic':'Create a To-do react application that uses FastAPI in the backend and have a login and signup components inside it'})
print(result)