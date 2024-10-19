from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

picam2.start()


time.sleep(20)

print("Press 'q' to Quti")

while True:
	frame = picam2.capture_array()
	cv2.imshow("camera view", frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

picam2.stop()
cv2.destroyAllWindows()