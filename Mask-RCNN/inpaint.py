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

def process_and_inpaint_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image_tensor = F.to_tensor(image).unsqueeze(0)
    image_np = np.array(image)

    with torch.no_grad():
        prediction = model(image_tensor)
    
    # Combine masks for humans and vehicles into a single mask
    combined_mask = np.zeros((image_np.shape[0], image_np.shape[1]), dtype=np.uint8)
    for element, score in zip(prediction[0]["masks"], prediction[0]["scores"]):
        if score > 0.5:  # Using a threshold to filter detections
            mask = element.mul(255).byte().cpu().numpy()
            mask = mask[0]  # Get the first channel for the grayscale mask
            combined_mask = np.maximum(combined_mask, mask)
    
    # Inpainting
    inpainted_image = cv2.inpaint(image_np, combined_mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    
    return inpainted_image

# Example usage
image_path = '/home/yifeng/Desktop/Mask-RCNN/18/image_3/001230.png'  # Update this path to your KITTI dataset image
inpainted_image = process_and_inpaint_image(image_path)

# Display the inpainted image
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(inpainted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
