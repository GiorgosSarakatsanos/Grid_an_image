from PIL import Image
from fpdf import FPDF
from config import IMAGE_PATH, CONTOUR_IMAGE_FILE, CONTOUR_PDF_FILE, A3_WIDTH_PT, A3_HEIGHT_PT, IMG_WIDTH_PT, IMG_HEIGHT_PT, CONTOUR_PDF_FILE, PDF_OUTPUT_FOLDER
import os


# 
def generate_pdf(image_path):
    # Open the image
    img = Image.open(image_path)
    
    pdf = FPDF(format='A3')     # Create a PDF object
    pdf.add_page()  # Add a page to the PDF
    
    # Calculate the number of columns and rows that fit in an A3 page
    margin_long_edge = 15  # in mm
    margin_short_edge = 35  # in mm
    
    a3_width_pt = A3_WIDTH_PT - 2 * margin_long_edge
    a3_height_pt = A3_HEIGHT_PT - 2 * margin_short_edge
    
    img_width_pt = IMG_WIDTH_PT
    img_height_pt = IMG_HEIGHT_PT
    
    num_columns = int(a3_width_pt // img_width_pt)
    num_rows = int(a3_height_pt // img_height_pt)
    
    # Iterate over each position and place the image    
    for row in range(num_rows):     # Iterate over each row
        for col in range(num_columns):  # Iterate over each column
            x = margin_long_edge + col * img_width_pt    # Calculate the x position
            y = margin_short_edge + row * img_height_pt  # Calculate the y position
            pdf.image(image_path, x, y, img_width_pt, img_height_pt) # Place the image in the PDF
    
    # Create a unique filename based on the original image filename
    image_filename = os.path.basename(image_path)
    pdf_filename = os.path.splitext(image_filename)[0] + '.pdf'

    # Save the PDF file
    pdf.output(os.path.join(PDF_OUTPUT_FOLDER, pdf_filename), 'F')