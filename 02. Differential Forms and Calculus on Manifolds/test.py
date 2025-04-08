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
basic_perspective = "Foque nos conceitos fundamentais de formas diferenciais e cálculo em variedades, incluindo uma introdução intuitiva às formas diferenciais, o produto wedge e diferenciação exterior. Explique a visualização de 1-formas, 2-formas e 3-formas, o significado de push-forwards e pull-backs, e como realizar mudanças de variáveis e integração de formas. Aborde o Lema de Poincaré, a relação entre cálculo vetorial e formas diferenciais, e apresente uma introdução acessível às variedades e ao Teorema de Stokes generalizado."
advanced_perspective = "Foque na teoria matemática rigorosa das formas diferenciais e cálculo em variedades, incluindo a estrutura algébrica do produto wedge, propriedades formais da diferenciação exterior, e a interpretação geométrica de k-formas. Cubra aplicações avançadas de push-forwards e pull-backs, teoria de integração em variedades, consequências do Lema de Poincaré para a cohomologia de de Rham, a dualidade entre formas diferenciais e campos vetoriais, e demonstrações detalhadas do Teorema de Stokes generalizado. Introduza o formalismo tensorial e suas aplicações em geometria diferencial."


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