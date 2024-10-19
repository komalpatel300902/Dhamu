from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera for still image capture
picam2.configure(picam2.create_still_configuration())

# Start the camera
picam2.start()

# Wait for a few seconds to allow the camera to stabilize
time.sleep(2)

# Capture an image
picam2.capture_file("image.jpg")

print("Image captured and saved as image.jpg")

# Stop the camera
picam2.stop()