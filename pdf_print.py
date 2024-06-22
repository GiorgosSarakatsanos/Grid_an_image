import os
from PIL import Image
from fpdf import FPDF
from config import CONTOUR_IMAGE_FILE, PDF_OUTPUT_FOLDER, CONTOUR_PDF_FILE
from config import CONTOUR_IMAGE_FILE, CONTOUR_PDF_FILE, A3_WIDTH_PT, A3_HEIGHT_PT, IMG_WIDTH_PT, IMG_HEIGHT_PT


def generate_pdf(image_path, output_folder):
        # Load the contour image
    contour_image = Image.open(CONTOUR_IMAGE_FILE)
    
    # Initialize FPDF instance for A3 size
    pdf = FPDF(format='A3')
    pdf.add_page()

    # Calculate the number of columns and rows that fit in an A3 page
    num_columns = int(A3_WIDTH_PT // IMG_WIDTH_PT)
    num_rows = int(A3_HEIGHT_PT // IMG_HEIGHT_PT)

    # Iterate over each position and place the image
    for row in range(num_rows):
        for col in range(num_columns):
            x = col * IMG_WIDTH_PT
            y = row * IMG_HEIGHT_PT
            pdf.image(CONTOUR_IMAGE_FILE, x, y, IMG_WIDTH_PT, IMG_HEIGHT_PT)
    # PDF filename and path
    pdf.output(CONTOUR_PDF_FILE)
    return output_folder + CONTOUR_PDF_FILE