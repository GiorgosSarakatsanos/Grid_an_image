from fpdf import FPDF
from PIL import Image
from config import CONTOUR_IMAGE_FILE, CONTOUR_PDF_FILE, A3_WIDTH_PT, A3_HEIGHT_PT, IMG_WIDTH_PT, IMG_HEIGHT_PT

def save_contour_as_pdf():
    # Load the contour image
    contour_image = CONTOUR_IMAGE_FILE.open(CONTOUR_IMAGE_FILE)
    
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

    # Save the PDF to the output file
    pdf_output_file = CONTOUR_PDF_FILE
    pdf.output(pdf_output_file)

    return pdf_output_file