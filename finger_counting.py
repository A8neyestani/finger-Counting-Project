# Import required libraries
import cv2
import os
import handTrackingModule as htm

# Setting the width and height for the webcam feed
wCam, hCam = 640, 480

# Initialize the webcam feed
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Variables to calculate frame rate
CTime = 0
PTime = 0

# Indices of fingertips in the landmarks list provided by the hand tracking model
tipsId = [4, 8, 12, 16, 20]

# Path where the images for each finger count are stored
folderPath = "fingersImage"
mylist = os.listdir(folderPath)

# Load all the images from the specified folder into a list
all_images = []
for name in mylist:
    img = cv2.imread(f"{folderPath}/{name}")
    all_images.append(img)

# Initialize the hand detector
detector = htm.handDetector()

# Start the loop to process webcam frames
while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    # Break the loop if frame isn't available
    if frame is None:
        break

    # Detect hands in the frame
    img = detector.findHands(frame)

    # Get the position of hand landmarks
    lmList = detector.findPosition(img, draw=False)

    # If landmarks are detected, process them to determine the number of raised fingers
    if len(lmList) != 0:
        fingers = []
        
        # Loop through the tips of the fingers to determine if they are raised or not
        for tips in tipsId:
            if tips == 4:  # Thumb has a different check because of its position
                if lmList[tips][1] > lmList[tips-1][1]:
                    fingers.append(0)
                else:
                    fingers.append(1)
            else:  # For other fingers
                if lmList[tips][2] < lmList[tips-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        # Count the total number of raised fingers
        totalfingers = fingers.count(1)

        # Display the corresponding image for the counted fingers
        frame[0:200, 0:200] = all_images[totalfingers-1]

        # Draw a rectangle and display the number of raised fingers on the frame
        cv2.rectangle(frame, (20, 255), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, str(totalfingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 10)
    
    # Display the resulting frame with the hand and finger count
    cv2.imshow("image", frame)

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the webcam and close any OpenCV windows
cv2.destroyAllWindows()
cap.release()
