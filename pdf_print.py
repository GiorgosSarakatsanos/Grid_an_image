from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from config import PDF_OUTPUT_FOLDER  # Assuming this is correctly pointing to your desired output folder
import os

def mm_to_points(mm):
    return mm * 2.83465

def generate_pdf(image_path):
    # Define the dimensions in millimeters
    img_width_mm = 85
    img_height_mm = 55
    paper_width_mm = 210
    paper_height_mm = 297
    top_margin = 15
    left_margin = 37
    bottom_margin = 15
    right_margin = 17
    
    # Calculate the image and paper sizes in points
    img_width_pts = mm_to_points(img_width_mm)
    img_height_pts = mm_to_points(img_height_mm)
    
    # Calculate the number of rows and columns based on page size and margins
    rows = int((paper_height_mm - top_margin - bottom_margin) / img_height_mm)
    columns = int((paper_width_mm - left_margin - right_margin) / img_width_mm)
    
    # Calculate the paper width and height in points including margins
    paper_width_pts = mm_to_points(paper_width_mm)
    paper_height_pts = mm_to_points(paper_height_mm)
    
    # Create a unique filename based on the original image filename
    image_filename = os.path.basename(image_path)
    pdf_filename = os.path.splitext(image_filename)[0] + '.pdf'
    
    # Ensure the output folder exists
    os.makedirs(PDF_OUTPUT_FOLDER, exist_ok=True)
    
    # Create the canvas with the unique filename in the output folder
    c = canvas.Canvas(os.path.join(PDF_OUTPUT_FOLDER, pdf_filename), pagesize=landscape((paper_width_pts, paper_height_pts)))
    
    for row in range(rows):
        for col in range(columns):
            x = left_margin + col * img_width_pts
            y = paper_height_pts - top_margin - (row + 1) * img_height_pts

            img = Image.open(image_path)
            img_width, img_height = img.size

            if img_width > img_height:
                c.saveState()
                c.translate(x + img_width_pts / 2, y + img_height_pts / 2)
                c.rotate(90)
                c.drawImage(image_path, -img_width_pts / 2, -img_height_pts / 2, width=img_width_pts, height=img_height_pts)
                c.restoreState()
            else:
                c.drawImage(image_path, x, y, width=img_width_pts, height=img_height_pts)

    # Finalize the PDF file
    c.save()