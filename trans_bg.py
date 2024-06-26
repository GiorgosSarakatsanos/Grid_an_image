from PIL import Image
from config import PNG_NO_ALPHA_FILE


def replace_alpha_with_transparent(image_path, background_color=(255, 255, 255)):
    image = Image.open(image_path).convert('RGBA')
    datas = image.getdata()

    new_data = []  # Create a new list to store the new data
    for item in datas:  # Loop through the data
        # If the pixel matches the background color, make it transparent
        if item[:3] == background_color:
            new_data.append((item[0], item[1], item[2], 0))  # Change alpha to 0
        else:
            new_data.append(item)  # Add the pixel as it is

    # Update the image with the new data
    image.putdata(new_data)
    image.save(image_path.replace('.png', '_transparent.png'))  # Save the modified image with a new name

    image.putdata(new_data) # Put the new data in the image
    image.save(PNG_NO_ALPHA_FILE) # Save the image