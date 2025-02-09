# CrewAI-PlantUML-and-Code-Agent

# CrewAI-Powered PlantUML and Code Generation

This repository demonstrates a system for automated generation of PlantUML diagrams and corresponding code from high-level textual descriptions, leveraging the CrewAI framework for agent orchestration.  It showcases the use of Large Language Models (LLMs), task management, and PlantUML parsing to streamline the software design and development process.

## Overview

This project utilizes CrewAI to define and manage a multi-agent workflow. The system takes a natural language description of a software feature as input and produces:

1. A PlantUML class and sequence diagram, capturing the design.
2. Python code implementing the specified functionality.

The system employs LLMs (Gemini, configurable) to perform both diagram generation and code synthesis.  Crucially, PlantUML parsing extracts design information from the generated diagrams, ensuring consistency between the design and the final code.

## Features

* Automated PlantUML diagram generation from natural language descriptions.
* Automated code generation based on PlantUML diagrams.
* Multi-agent task orchestration with CrewAI.
* Configurable LLM backend.
* PlantUML parsing for design-consistent code generation.

## Technologies Used

* **Agent Orchestration:** CrewAI
* **Large Language Model (LLM):** Gemini (configurable via `agents.py`)
* **Diagramming:** PlantUML
* **PlantUML Parsing:** `plantuml` Python library
* **Dependencies:** `crewai_tools`, `python-dotenv`, (list all dependencies in `requirements.txt`)

## Technical Details
1. Agents
uml_generator: This agent, defined in agents.py, is responsible for generating the PlantUML diagram.  It leverages the LLM to interpret the input description and create a valid PlantUML representation.

code_generator: This agent generates Python code based on the PlantUML diagram.  It uses the plantuml library to parse the diagram and extract relevant information (classes, methods, relationships). The code_generator_agent function implements the logic for converting PlantUML elements into code constructs.  It receives the PlantUML output via the context parameter.

2. Tasks
uml_task: This task uses the uml_generator agent. Its description provides the prompt for the PlantUML generation.

code_task: This task uses the code_generator agent.  Critically, it defines context=[uml_task].  This instructs CrewAI to execute uml_task before code_task and to pass the output of uml_task (the PlantUML code) as the context to code_task.

3. CrewAI Workflow (crew.py)
The Crew object defines the agents and tasks. The Process.sequential setting ensures that tasks are executed in the order they are defined. The crew.kickoff() method initiates the workflow.

4. PlantUML Parsing
The plantuml library is used within the code_generator_agent function to parse the generated PlantUML diagram.  This enables the code generation process to be driven by the design captured in the diagram, promoting consistency and reducing the risk of discrepancies between design and implementation.
