## General Information

`vs code : Git Bash`
### Login into raspberrypi
```bash
MICROSOFT@DESKTOP-225HS7V MINGW64 ~
$ ssh pi@raspberrypi.local
pi@raspberrypi.local's password: 
Linux raspberrypi 6.12.47+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.47-1+rpt1 (2025-09-16) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Nov 15 22:31:23 2025 from 192.168.1.6
```
``` bash
hostname -I : to get ip adress
```
```
pwd: 09-09-2024
```

- For camera module `raspi-still` is not working `libcamera-still`.
- The video format must be : Video.h264.

## **Setting Up Env Installing picamera and opencv Libraries**

For venv 
``` bash
sudo apt-get install python3-pip python3-virtualenv
mkdir project
cd project
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
```
Required library download
```python
sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
```
If you're using a PiCamera run:
```
pip install "picamera[array]"
```
Users of PiCamera may also have to enable Camera Support:
```
sudo raspi-config
Inferface Options
Legacy Camera Support -- Enable
```

4:15 Install OpenCV
```
pip install opencv-contrib-python
--Takes a long time
```

5:25 Testing
```python
import cv2
cv2.__version__
```

### Installing OpenCV

```bash
sudo apt install python3-opencv
```

## **Picamera Code that is Running in the Terminal**

[Capturing the Image](/src/initial_testing/capture_image.py)

[This can be used for rotating the image 45 and Save it](/src/initial_testing/rotate_and_save)

`important`  
[Switching on the camera and viewing it | window is comming](/src/initial_testing/reading_camera.py)


## Error

**Q. Error import fd 20 Faliure**

In the context of using libcamera on a Raspberry Pi, the libcamera command-line tool has several flags to control its behavior. Specifically:

`-n (or --no-headers)`  
This flag is used with the libcamera-hello or similar commands to suppress the printing of headers that would normally be included in the output. When you use this option, the program will not print header information such as camera details, which might be useful for debugging or if you want a cleaner output.

`-r (or --raw)`  
The -r flag is used to specify that the output should be in raw format. When you use this option, libcamera will output raw image data rather than a processed or compressed format. This is particularly useful if you want to capture images in their raw form for further processing or analysis.

`-o (or --output)`  
The -o flag specifies the output file where the captured image or video will be saved. You need to provide a filename or path after the -o flag. For example:


- working good with this code: 

`for image :`

```bash
libcamera-still -n -o test.jpg 
```

`for Video :`
```bash
libcamera-vid -n -o test.h264
```
### Installing picamera in the Venv
``` bash
Using cached python-prctl-1.8.1.tar.gz (28 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [1 lines of output]
      You need to install libcap development headers to build this module
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.
```
`Solution`  
Step 1:
```bash
sudo apt-get install libcap-dev
```
Step 2:
```
pip install picamera2
```
## Installing VScode 
```
sudo apt install code
```

## Working On
1. Picamera is present in the external library but not in the Venv
1. face_recognition is present in the venv andnot present expernally
