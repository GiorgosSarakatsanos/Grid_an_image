from PIL import Image, ImageFilter
from fpdf import FPDF
from PIL import ImageOps

# # Open an image file
image_path = 'static/images/Flios-logo-03.png'

# Set pdf output folder
pdf_output_folder = 'static/pdf_output/'

# Set pdf output file name for contour image depending on the image name
pdf_output_file = pdf_output_folder + image_path.split('/')[-1].split('.')[0] + '_contours.pdf'

# def get_image_shape(image_path):
#     image = Image.open(image_path)
#     alpha = image.split()[-1]
#     bbox = alpha.getbbox()
#     return bbox


# Create the borders of the image #
def generate_contour(image_path):
    image = Image.open(image_path)
    alpha = image.split()[-1]
    contour_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    contour_image.paste(alpha, mask=alpha)
    contour_image = contour_image.filter(ImageFilter.FIND_EDGES)
    return contour_image


contour_image = generate_contour("static/images/Flios-logo-03.png")
contour_image = contour_image.convert('RGB')  # Convert to RGB mode for easier color manipulation

# # Apply dilation to make the contour lines bolder
# contour_thickness = 3
# # Adjust this value to change the thickness
# contour_image = contour_image.filter(ImageFilter.MaxFilter(contour_thickness))

# Contour color
contour_color = (0, 0, 0)  # Change the contour color to black (RGB value)
contour_image = contour_image.convert('RGBA')  # Convert back to RGBA mode
contour_pixels = contour_image.load()

# Iterate over each pixel in the contour image
for x in range(contour_image.width):
    for y in range(contour_image.height):
        r, g, b, a = contour_pixels[x, y]
        if r > 0 or g > 0 or b > 0:  # Check if the pixel is part of the contour
            contour_pixels[x, y] = contour_color + (a,)  # Set the contour color and original alpha value
        else:
            contour_pixels[x, y] = (0, 0, 0, 0)  # Set non-contour pixels to transparent

image_file_path = pdf_output_file.replace('.pdf', '.png')  # Change the extension to .png
contour_image.save(image_file_path)

# Load the image to get its size
contour_image = Image.open(image_file_path)
original_width, original_height = contour_image.size

# img dimensions in mm (for example, 100 mm by 150 mm)
img_width_mm = 100
img_height_mm = 150

# Convert mm to points (1 mm = 0.352778 points)
img_width_pt = img_width_mm * 0.352778
img_height_pt = img_height_mm * 0.352778

# Calculate the scaling factor to maintain aspect ratio
scaling_factor = min(img_width_pt / original_width, img_height_pt / original_height)

# Calculate the new dimensions
new_width = original_width * scaling_factor
new_height = original_height * scaling_factor

# Convert the new dimensions back to mm for FPDF
new_width_mm = new_width / 0.352778
new_height_mm = new_height / 0.352778

# Initialize FPDF instance
pdf = FPDF()

# Add a page to the PDF
pdf.add_page()

# Insert the saved image into the PDF with specific dimensions
# Note: Adjust the x, y position as needed
pdf.image(image_file_path, 55, 55, new_width_mm, new_height_mm)

# Save the PDF to the output file
pdf.output(pdf_output_file)

# # calculate how many images will fit in a page
# def calculate_images_per_page(image_shape, page_shape):
#     image_width, image_height = image_shape
#     page_width, page_height = page_shape
#     images_per_row = page_width // image_width
#     images_per_col = page_height // image_height
#     return images_per_row * images_per_col


# # Example usage
# image_path = 'static/images/Flios-logo-03.png'
# border_width = 5
# border_color = (255, 255, 255, 255)  # Black border


# border_image = generate_border(image_path, border_width, border_color)
# border_image.show()