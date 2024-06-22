import os
from PIL import Image
from fpdf import FPDF
from config import CONTOUR_IMAGE_FILE, PDF_OUTPUT_FOLDER, CONTOUR_PDF_FILE

def generate_pdf(image_path, output_folder):
    image = Image.open(image_path)
    pdf = FPDF()
    
    
    
    # PDF filename and path
    pdf.output(CONTOUR_PDF_FILE)
    return output_folder + CONTOUR_PDF_FILE