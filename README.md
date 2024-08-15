# GSG HTML Generator

This project generates html for the GSG website using Jinja2 templates and YAML data.

## Setup Instructions

1. **Clone the repository**:

    ```sh
    git clone <repository-url>
    cd project-root
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On macOS and Linux
    #venv\Scripts\activate      # On Windows
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Generate the HTML**:

    ```sh
    python scripts/generate_html.py
    ```

5. **View the generated HTML**:
    The generated HTML file will be located in the `output` directory.
