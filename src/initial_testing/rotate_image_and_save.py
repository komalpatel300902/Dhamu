from picamera2 import Picamera2
from PIL import Image

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

picam2.start()
image_array = picam2.capture_array()  # Get image as a NumPy array
picam2.stop()

# Convert NumPy array to PIL Image
image_pil = Image.fromarray(image_array)

# Apply some Pillow processing (e.g., rotating the image)
rotated_image = image_pil.rotate(45)

# Save or display the processed image
rotated_image.save("rotated_image.jpg")
rotated_image.show()