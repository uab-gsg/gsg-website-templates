import yaml
from jinja2 import Environment, FileSystemLoader
import os

# Define paths
data_file = os.path.join('data', 'officers.yml')
template_dir = 'templates'
output_file = os.path.join('output', 'officers.html')

# Load the YAML data
with open(data_file, 'r') as file:
    data = yaml.safe_load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load the templates
card_template = env.get_template('officers_card_template.html')
layout_template = env.get_template('officers_layout_template.html')

# Render the HTML content
html_content = layout_template.render(officers=data['officers'], officer_card_template=card_template)

# Save the generated HTML to a file
with open(output_file, 'w') as file:
    file.write(html_content)

print(f"HTML content generated and saved to {output_file}")
