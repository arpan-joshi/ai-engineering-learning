import os

# Clean directory structure for the AI Engineering From Scratch phases
phases = [
    "00-setup-and-tooling",
    "01-math-foundations",
    "02-ml-fundamentals",
    "03-deep-learning-basics",
    "04-nlp-and-transformers",
    "05-llm-fine-tuning",
    "06-rag-systems",
    "07-agentic-workflows",
    "08-mlops-and-deployment"
]

for phase in phases:
    # Create the phase folder
    os.makedirs(phase, exist_ok=True)
    
    # Create a placeholder README inside each phase folder
    readme_path = os.path.join(phase, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {phase.replace('-', ' ').title()}\n\nAdd your day-to-day notes, code, and exercises for this phase here.\n")

print("Successfully created your lesson directory structure!")
