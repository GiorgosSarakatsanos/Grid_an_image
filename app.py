import sys
import os  # Import the os module
from config import IMAGE_PATH, PDF_OUTPUT_FOLDER,PNG_NO_ALPHA_FOLDER, PYTHON_MODULES_PATH, CONTOUR_IMAGE_FILE, CONTOUR_PDF_FILE, PNG_OUTPUT_FOLDER, PNG_NO_ALPHA_FILE, IMAGE_PATH, PYTHON_MODULES_PATH, UPLOADS_FOLDER
from contour import generate_contour, save_contour_image
from pdf_print import generate_pdf
from trans_bg import replace_alpha_with_transparent
sys.path.append(PYTHON_MODULES_PATH)

# Generate the contour image
contour_image = generate_contour(IMAGE_PATH)
save_contour_image(contour_image)  # Save the contour image
# Open the contour image in a new tab
contour_image.show()  # Open the contour image in a new tab

# Import the generate_pdf function from pdf_print.py

# Generate the PDF
pdf = generate_pdf(IMAGE_PATH, PDF_OUTPUT_FOLDER)

transparent_image_path = replace_alpha_with_transparent(IMAGE_PATH, PNG_NO_ALPHA_FOLDER)