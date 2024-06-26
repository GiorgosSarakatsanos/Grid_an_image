from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from config import PDF_OUTPUT_FOLDER  # Assuming this is correctly pointing to your desired output folder
import os

def mm_to_points(mm):
    return mm * 2.83465

paper_sizes = {
    'C3': (458, 324),
    'A3': (420, 297),
    'A4': (297, 210)
}

paper_size_key = 'A3'  # This can be dynamically chosen based on your requirements

def generate_pdf(image_path):
    paper_width_mm, paper_height_mm = paper_sizes[paper_size_key]

    img_width_mm = 25
    img_height_mm = 25
    top_margin = 15
    left_margin = 37
    bottom_margin = 15
    right_margin = 17

    img_width_pts = mm_to_points(img_width_mm)
    img_height_pts = mm_to_points(img_height_mm)
    paper_width_pts = mm_to_points(paper_width_mm)
    paper_height_pts = mm_to_points(paper_height_mm)

    # Calculate the available space for images on the page, in points
    available_width_pts = paper_width_pts - mm_to_points(left_margin + right_margin)
    available_height_pts = paper_height_pts - mm_to_points(top_margin + bottom_margin)

    # Calculate the number of rows and columns based on available space and image size
    columns = int(available_width_pts / img_width_pts)
    rows = int(available_height_pts / img_height_pts)

    image_filename = os.path.basename(image_path)
    pdf_filename = os.path.splitext(image_filename)[0] + '.pdf'
    os.makedirs(PDF_OUTPUT_FOLDER, exist_ok=True)
    c = canvas.Canvas(os.path.join(PDF_OUTPUT_FOLDER, pdf_filename), pagesize=landscape((paper_width_pts, paper_height_pts)))

    
    
    corner_line_length = mm_to_points(40)  # Length of the corner lines in points
    c.setLineWidth(4)  # Set the line width to 3 points for bolder lines
    # Top left corner
    c.line(mm_to_points(left_margin), paper_height_pts - mm_to_points(top_margin), 
        mm_to_points(left_margin) + corner_line_length, paper_height_pts - mm_to_points(top_margin))
    c.line(mm_to_points(left_margin), paper_height_pts - mm_to_points(top_margin), 
        mm_to_points(left_margin), paper_height_pts - mm_to_points(top_margin) - corner_line_length)

    # Top right corner
    c.line(paper_width_pts - mm_to_points(right_margin), paper_height_pts - mm_to_points(top_margin), 
        paper_width_pts - mm_to_points(right_margin) - corner_line_length, paper_height_pts - mm_to_points(top_margin))
    c.line(paper_width_pts - mm_to_points(right_margin), paper_height_pts - mm_to_points(top_margin), 
        paper_width_pts - mm_to_points(right_margin), paper_height_pts - mm_to_points(top_margin) - corner_line_length)

    # Bottom right corner
    c.line(paper_width_pts - mm_to_points(right_margin), mm_to_points(bottom_margin), 
        paper_width_pts - mm_to_points(right_margin) - corner_line_length, mm_to_points(bottom_margin))
    c.line(paper_width_pts - mm_to_points(right_margin), mm_to_points(bottom_margin), 
        paper_width_pts - mm_to_points(right_margin), mm_to_points(bottom_margin) + corner_line_length)

    # Bottom left corner
    c.line(mm_to_points(left_margin), mm_to_points(bottom_margin), 
        mm_to_points(left_margin) + corner_line_length, mm_to_points(bottom_margin))
    c.line(mm_to_points(left_margin), mm_to_points(bottom_margin), 
        mm_to_points(left_margin), mm_to_points(bottom_margin) + corner_line_length)

    for row in range(rows):
        for col in range(columns):
            x = mm_to_points(left_margin) + col * img_width_pts
            y = paper_height_pts - mm_to_points(top_margin) - (row + 1) * img_height_pts
            c.drawImage(image_path, x, y, width=img_width_pts, height=img_height_pts)

    c.save()