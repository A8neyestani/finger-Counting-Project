# finger-Counting-Project
# Finger Counting using Hand Tracking

This repository contains code to detect hands using a webcam feed and count the number of raised fingers. The hand tracking is powered by the `handTrackingModule`.

## Features

- Real-time hand detection using a webcam feed.
- Count and display the number of raised fingers.
- Displays corresponding images for each finger count.

## Usage

1. Make sure you have OpenCV and other required libraries installed.
2. Run the script to start the webcam feed and hand tracking.

## Code Overview

The main script initializes a webcam feed, uses the `handTrackingModule` to detect hands in the frame, and then processes the detected hand landmarks to determine the number of raised fingers. The corresponding image for the counted fingers is then displayed on the frame.

## Dependencies

- OpenCV
- [handTrackingModule](#) *(https://developers.google.com/mediapipe)*

## Author

**Arman Neyestani**
- **GitHub:** [A8neyestani](https://github.com/A8neyestani)
- **Email:** [A8neyestani@protonmail.com](mailto:A8neyestani@protonmail.com)

## License

This project is open source and available under the [MIT License](LICENSE).

---

If you have any questions or encounter any issues, please open an issue or contact the author.
