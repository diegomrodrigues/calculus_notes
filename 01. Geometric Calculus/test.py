import os
import re
from dotenv import load_dotenv

load_dotenv()

from pollo.agents.draft.writer import generate_drafts_from_topics

# Define the base directory where topic folders are located
base_dir = "."  # Change this to your actual base directory path

# Define directories to exclude from processing
EXCLUDE_DIRS = [
]

# Get all directories in the base directory
all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Filter directories matching the pattern "[0-9+]. [Topic Name]"
topic_dirs = [d for d in all_dirs if re.match(r"^\d+\.\s+.+$", d)]

# Exclude directories that are in the EXCLUDE_DIRS list
topic_dirs = [d for d in topic_dirs if d not in EXCLUDE_DIRS]

# Define the perspectives for all topics
basic_perspective = "Foque nos conceitos fundamentais do cálculo geométrico, incluindo geometria de mapas lineares, aproximações, derivadas e suas interpretações geométricas. Explique como calcular integrais duplas e integrais de superfície, a importância de funções implícitas e pontos críticos, e como aplicar o Teorema de Stokes em contextos práticos. Apresente os conceitos de forma intuitiva, com exemplos visuais e aplicações em problemas básicos."
advanced_perspective = "Foque na teoria matemática rigorosa do cálculo geométrico, incluindo a geometria diferencial de mapas lineares, análise de funções inversas, aproximações de alta ordem e o significado geométrico da derivada. Cubra métodos avançados para avaliar integrais duplas e de superfície, a teoria de funções implícitas, análise de pontos críticos, e demonstrações formais do Teorema de Stokes com aplicações em física e engenharia."

# Process each topic directory
for directory in topic_dirs:
    print(f"Processing directory: {directory}")
    generate_drafts_from_topics(
        directory=directory,
        perspectives=[
            basic_perspective,
            advanced_perspective
        ],
        json_per_perspective=1,
        branching_factor=1
    )
    
print(f"Processed {len(topic_dirs)} topic directories")