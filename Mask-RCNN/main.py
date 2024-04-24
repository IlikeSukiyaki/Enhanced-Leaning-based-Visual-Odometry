import os
import cv2
import numpy as np
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained Mask R-CNN model
model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

def process_and_color_mask_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image_tensor = F.to_tensor(image).unsqueeze(0)
    image_np = np.array(image)

    with torch.no_grad():
        prediction = model(image_tensor)

    # Get the predicted classes; COCO class ID for traffic light is 10
    pred_classes = prediction[0]['labels'].cpu().numpy()
    
    combined_mask = np.zeros((image_np.shape[0], image_np.shape[1]), dtype=np.bool_)
    for element, score, pred_class in zip(prediction[0]["masks"], prediction[0]["scores"], pred_classes):
        if score > 0.3 and pred_class != 10:  # Filter out traffic light class
            mask = element.squeeze().cpu().numpy()
            combined_mask = np.logical_or(combined_mask, mask > 0.5)
    
    image_np[combined_mask] = [0, 255, 0]  # RGB for green
    return image_np

def process_and_save_mask_images(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over all image files in the input directory
    for image_file in os.listdir(input_folder):
        # Construct the full file path
        image_path = os.path.join(input_folder, image_file)
        # Check if it's a file and has a .png extension
        if os.path.isfile(image_path) and image_path.lower().endswith('.png'):
            try:
                # Process the image to create a masked image
                colored_mask_image = process_and_color_mask_image(image_path)
                
                # Save the masked image to the output folder
                output_path = os.path.join(output_folder, image_file)
                Image.fromarray(colored_mask_image).save(output_path)
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

# Example usage
input_folder = '04'  # Update this path to your input image folder
output_folder = '/home/yifeng/Desktop/Mask-RCNN/output_folder'  # Update this path to your output folder
process_and_save_mask_images(input_folder, output_folder)

# Note: The actual display of the images using plt.show() is not necessary if you're processing batches of images.
# It is used only for visual confirmation and should be commented out when processing large datasets.
