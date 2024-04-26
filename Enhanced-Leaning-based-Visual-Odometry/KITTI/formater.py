from PIL import Image
import os

# Directory where your JPG images are stored
image_directory = '/home/yifeng/Desktop/DeepVO/DeepVO-pytorch/KITTI/images/30'
# Directory where you want to save the PNG images
output_directory = '/home/yifeng/Desktop/DeepVO/DeepVO-pytorch/KITTI/images/30/formetted'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the image directory
for filename in os.listdir(image_directory):
    if filename.endswith('.jpg'):
        # Construct the full file path
        img_path = os.path.join(image_directory, filename)
        # Open the image
        with Image.open(img_path) as img:
            # Replace the file extension
            png_filename = filename[:-4] + '.png'
            # Construct the output file path
            output_path = os.path.join(output_directory, png_filename)
            # Save the image in PNG format
            img.save(output_path, 'PNG')

        print(f'Converted {filename} to {png_filename}')

print('Conversion complete.')
