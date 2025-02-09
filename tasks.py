from crewai import Task
from tools import tool
from agents import uml_generator,code_generator

uml_task = Task(
  description=(
    "Generate Plantuml class and sequence diagram {topic}."
    "The class diagram should have the classes App, Controller, Services, Repository,"
    "The function names should follow camelCasing,"
    "The same set of functions generated in the class diagram should be used for generating the sequence diagram,"
    "The sequence diagram should contain the actor user and participants as app, controller, services and repository,"
    "Use autonumber 1.0 so that the count of sequence lines will be there, use group keyword for functions, use alt keyword for each function's try and except block, use proper activate and deactivate,"
    "Each sequence line should have more than 20 words describing the entire logic (code-wise and it's explanation as well) for each and every sequence lines,"
    "Mandatory use of alt try and except for all the grouped functions,"
    "The sequence diagram should start from the user level and the diagram should cover every logic till the repository and how the data/output gets returned back to the user,"
    "App file logic: has the routing function (just gets the input and passes it to controller function),"
    "Controller file logic: Receives the input and validates it and if so, passes it to services function,"
    "Services file logic: This is where the actual business logic happens and passes to repository (if there any any database related operations),"
    "Repository file logic: Database related operations will happen here and returns the result back to services function."
    ""
  ),
  expected_output='PlantUML code for the class and sequence diagram',
  tools=[tool],
  agent=uml_generator,
  output_file='uml_diagram.txt'
)

code_task = Task(
  description=(
    "Generate code in reference with the PlantUML diagrams {topic}."
    "Mandatorily use try and except block for all the functions"
    "Generate code for all the files app, controller, services and repository"
    "Use the same function names mentioned in the sequence digram (dont hallucinate)"
  ),
  context=[uml_task],
  expected_output='Generate code for all the files based on the plantuml diagram {topic}',
  tools=[tool],
  agent=code_generator,
  async_execution=False,
  output_file='code.txt' 
)