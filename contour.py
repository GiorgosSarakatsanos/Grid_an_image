from PIL import Image, ImageFilter
from config import CONTOUR_IMAGE_FILE, IMAGE_PATH, PNG_OUTPUT_FOLDER

def generate_contour(image_path):
    image = Image.open(image_path) # Open the image
    alpha = image.split()[-1]   # Get the alpha channel
    contour_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    contour_image.paste(alpha, mask=alpha)  # Paste the alpha channel to the contour image
    contour_image = contour_image.filter(ImageFilter.FIND_EDGES)    # Apply the FIND_EDGES filter
    contour_image.save(CONTOUR_IMAGE_FILE)   # Save the contour image