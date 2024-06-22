import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for images and PDFs
IMAGE_PATH = os.path.join(BASE_DIR, 'static', 'images', 'Flios-logo-03.png')
PDF_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'pdf_output')

# Path for python modules
PYTHON_MODULES_PATH = os.path.join(BASE_DIR, 'static', 'python')
