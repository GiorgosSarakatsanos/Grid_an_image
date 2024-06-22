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

# A3 page size in points (1 point = 1/72 inch)
A3_WIDTH_PT = 841.89  # 297 mm
A3_HEIGHT_PT = 1190.55  # 420 mm

# Image dimensions in mm (for example, 100 mm by 150 mm)
IMG_WIDTH_MM = 100
IMG_HEIGHT_MM = 150

# Convert mm to points (1 mm = 0.352778 points)
IMG_WIDTH_PT = IMG_WIDTH_MM * 0.352778
IMG_HEIGHT_PT = IMG_HEIGHT_MM * 0.352778