import sys
from config import IMAGE_PATH, PYTHON_MODULES_PATH, CONTOUR_IMAGE_FILE, IMAGE_PATH, PYTHON_MODULES_PATH, PNG_NO_ALPHA_FILE # Import the IMAGE_PATH and PYTHON_MODULES_PATH variables
from contour import generate_contour
from pdf_print import generate_pdf
from trans_bg import replace_alpha_with_transparent
sys.path.append(PYTHON_MODULES_PATH)

# CONTOUR Production
contour_image = generate_contour(IMAGE_PATH) # Generate the contour image

transparent_image = replace_alpha_with_transparent(IMAGE_PATH) # Generate the transparent image

images_pdf = generate_pdf(IMAGE_PATH) # Generate the PDF file for uploaded image
no_alpha_pdf = generate_pdf(PNG_NO_ALPHA_FILE) # Generate the PDF file for contours
contours_pdf = generate_pdf(CONTOUR_IMAGE_FILE) # Generate the PDF file for contours



