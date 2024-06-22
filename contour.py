import os
from PIL import Image, ImageFilter
from config import CONTOUR_IMAGE_FILE

def generate_contour(image_path):
    image = Image.open(image_path)
    alpha = image.split()[-1]
    contour_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    contour_image.paste(alpha, mask=alpha)
    contour_image = contour_image.filter(ImageFilter.FIND_EDGES)
    return contour_image

def save_contour_image(contour_image):
    contour_image.save(CONTOUR_IMAGE_FILE)
    return CONTOUR_IMAGE_FILE