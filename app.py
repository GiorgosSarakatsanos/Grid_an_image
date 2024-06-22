import sys
import os
from config import IMAGE_PATH, PDF_OUTPUT_FOLDER, PYTHON_MODULES_PATH

# Add the directory containing contour.py and trans_bg.py to the Python path
sys.path.append(PYTHON_MODULES_PATH)

from contour import generate_contour, save_contour_as_pdf

# Generate the contour image and save it as a PDF
contour_image = generate_contour(IMAGE_PATH)
pdf_output_file = save_contour_as_pdf(contour_image, IMAGE_PATH, PDF_OUTPUT_FOLDER)

print(f'Contour PDF saved to: {pdf_output_file}')
