from PIL import Image
import os

script_folder = os.path.dirname(os.path.abspath(__file__))

# Folder containing your images
input_folder = script_folder  # Change this to your folder path
output_folder = script_folder

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to crop image to 4:3 aspect ratio
def crop_to_4_3(img):
    width, height = img.size
    target_ratio = 3 / 4

    current_ratio = width / height

    if current_ratio > target_ratio:
        # Image is wider than 4:3 → crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        right = left + new_width
        top = 0
        bottom = height
    else:
        # Image is taller than 4:3 → crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        bottom = top + new_height
        left = 0
        right = width

    return img.crop((left, top, right, bottom))

# Process all webp files
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            cropped_img = crop_to_4_3(img)
            cropped_img.save(output_path)

print(f"Finished cropping all webp images to 4:3 in '{output_folder}'")
