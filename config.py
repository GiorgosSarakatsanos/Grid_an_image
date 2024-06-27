import os
from datetime import datetime

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for images and PDFs
IMAGE_PATH = os.path.join(BASE_DIR, 'static', 'uploads', 'png', 'Flios-logo-03.png')
PDF_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'output', 'pdf_output')
PNG_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'output', 'contours', 'png_contours')
PNG_NO_ALPHA_FOLDER = os.path.join(BASE_DIR, 'static', 'output', 'images', 'no_alpha')
UPLOADS_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

# File names for images and PFDs
CONTOUR_PDF_FILE = os.path.join(PDF_OUTPUT_FOLDER, os.path.basename(IMAGE_PATH).split('.')[0] + '_contour.pdf')
CONTOUR_IMAGE_FILE = os.path.join(PNG_OUTPUT_FOLDER, os.path.basename(IMAGE_PATH).split('.')[0] + '_contour.png')
PNG_NO_ALPHA_FILE = os.path.join(PNG_NO_ALPHA_FOLDER, os.path.basename(IMAGE_PATH).split('.')[0] + '_no-alpha.png')

# Path for python modules
# PYTHON_MODULES_PATH = os.path.join(BASE_DIR, 'static', 'python')

