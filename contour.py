from PIL import Image, ImageFilter
from config import CONTOUR_IMAGE_FILE

def generate_contour(image_path):
    image = Image.open(image_path)  # Open the image
    alpha = image.split()[-1]  # Get the alpha channel

    # Create an image to hold the alpha channel with a transparent background
    contour_image = Image.new('L', image.size, 0)
    contour_image.paste(alpha, mask=alpha)  # Paste the alpha channel

    # Detect edges in the alpha channel
    edges = contour_image.filter(ImageFilter.FIND_EDGES)

    # Convert edges to black lines on a transparent background
    final_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    final_image.paste(Image.new('RGBA', image.size, (0, 0, 0, 255)), mask=edges)
    # Invert the image
    final_image = Image.composite(final_image, Image.new('RGBA', image.size, (255, 255, 255, 255)), edges)

    # Save the contour image
    final_image.save(CONTOUR_IMAGE_FILE)