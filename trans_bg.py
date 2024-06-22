from PIL import Image
from config import IMAGE_PATH  # Import paths if needed

def change_background(image_path, background_color):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    data = image.getdata()
    
    new_data = []
    for item in data:
        if item[3] == 0:  # If pixel is transparent
            new_data.append(background_color + (255,))  # Change to the background color
        else:
            new_data.append(item)
    
    image.putdata(new_data)
    return image

def save_image_with_new_background(image, output_path):
    image.save(output_path)
