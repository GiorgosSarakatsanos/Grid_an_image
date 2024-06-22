from PIL import Image
import os
from config import IMAGE_PATH, PNG_NO_ALPHA_FILE, PNG_NO_ALPHA_FOLDER

def replace_alpha_with_transparent(image_path, output_path):
    image = Image.open(image_path).convert('RGBA')
    datas = image.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            # Change all white (also shades of whites)
            # pixels to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(PNG_NO_ALPHA_FILE, "PNG")

def process_upload(image_filename):
    image_path = os.path.join()
    output_path = os.path.join(PNG_NO_ALPHA_FOLDER, PNG_NO_ALPHA_FILE)
    replace_alpha_with_transparent(image_path, output_path)
    return output_path