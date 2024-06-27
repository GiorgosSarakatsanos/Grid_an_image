import sys
from config import IMAGE_PATH, CONTOUR_IMAGE_FILE, IMAGE_PATH
from contour import generate_contour
from pdf_print import generate_pdf
from trans_bg import replace_alpha_with_transparent
from flask import request

# Upload Image
uploaded_image = request.files['image']
image_path = '/path/to/save/image.jpg'
uploaded_image.save(image_path)

# Generate PDF for Uploaded Image
uploaded_image_pdf = generate_pdf(image_path)

# CONTOUR Production
contour_image = generate_contour(IMAGE_PATH) # Generate the contour image

transparent_image = replace_alpha_with_transparent(IMAGE_PATH) # Generate the transparent image

images_pdf = generate_pdf(IMAGE_PATH) # Generate the PDF file for uploaded image
# no_alpha_pdf = generate_pdf(PNG_NO_ALPHA_FILE) # Generate the PDF file for contours
contours_pdf = generate_pdf(CONTOUR_IMAGE_FILE) # Generate the PDF file for contours
