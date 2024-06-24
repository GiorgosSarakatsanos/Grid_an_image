from PIL import Image
from config import PNG_NO_ALPHA_FILE, PNG_NO_ALPHA_FOLDER, IMAGE_PATH


def replace_alpha_with_transparent(image_path):
    image = Image.open(image_path).convert('RGBA')
    datas = image.getdata()

    new_data = [] # Create a new list to store the new data
    for item in datas: # Loop through the data
        if item[0] == 255 and item[1] == 255 and item[2] == 255: # If the pixel is white
            new_data.append((255, 255, 255, 0)) # Add a transparent pixel
        else:
            new_data.append(item) # Add the pixel as it is

    image.putdata(new_data) # Put the new data in the image
    image.save(PNG_NO_ALPHA_FILE) # Save the image