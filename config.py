import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for images and PDFs
IMAGE_PATH = os.path.join(BASE_DIR, 'static', 'uploads', 'png', 'Flios-logo-03.png')
PDF_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'output', 'contours', 'pdf_contours',)
PNG_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'output', 'contours', 'png_contours',)

# File names for images and PFDs
CONTOUR_PDF_FILE = os.path.join(PDF_OUTPUT_FOLDER, os.path.basename(IMAGE_PATH).split('.')[0] + '_contour.pdf')
CONTOUR_IMAGE_FILE = os.path.join(PNG_OUTPUT_FOLDER, os.path.basename(IMAGE_PATH).split('.')[0] + '_contour.png')

# Path for python modules
PYTHON_MODULES_PATH = os.path.join(BASE_DIR, 'static', 'python')

