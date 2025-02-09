from crewai import Agent,LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()
import os
import plantuml

OPENAI_API_KEY="sk-proj-111"
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

llm=LLM(model="gemini/gemini-2.0-flash-exp",
                           verbose=True,
                           temperature=0.2)


uml_generator=Agent(
    role="PlantUML Designer",
    goal='PlantUML class and sequence diagram {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

def code_generator_agent(context, *args, **kwargs):
    uml_output = context.output
    print("PlantUML Output:\n", uml_output)

    
    try:
        diagram = plantuml.PlantUML(uml_output)
        class_names = [c.name for c in diagram.classes]
        function_names = []
        for c in diagram.classes:
            for m in c.methods:
                function_names.append(m.name)


        print("Extracted Class Names:", class_names)
        print("Extracted Function Names:", function_names)

    except plantuml.PlantUMLParseError as e:
        print(f"Error parsing PlantUML: {e}")
        return "Error: Could not parse PlantUML" 

    generated_code = ""
    for class_name in class_names:
        generated_code += f"class {class_name}:\n"
        for function_name in function_names:
            generated_code += f"    def {function_name}():\n"
            generated_code += f"        try:\n"
            generated_code += f"            # Your code logic here (replace with actual code)\n"
            generated_code += f"            pass  # Placeholder\n"
            generated_code += f"        except Exception as e:\n"
            generated_code += f"            print(f'Error in {function_name}: {{e}}')\n"
            generated_code += f"            raise  # Or handle as needed\n"
        generated_code += "\n"


    return generated_code


code_generator = Agent(
  role='Senior Software Engineer',
  goal='Generate code for the following PlantUML Diagrams{topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False,
  agent_function=code_generator_agent
)
