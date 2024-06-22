from PIL import Image
from contours import process_contours

# # Open an image file
image_path = 'static/images/Flios-logo-03.png'

# Set pdf output folder
pdf_output_folder = 'static/pdf_output/'

# Refer to countours.py for the process_contours function
process_contours(image_path, pdf_output_folder)

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