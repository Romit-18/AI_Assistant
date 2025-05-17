import cv2

def open_camera():
    try:
        # Open the default camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception("Unable to access the camera.")
        
        print("Camera opened successfully. Press 'q' to exit.")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
            cv2.imshow("Camera", frame)
            
            # Exit the camera view with 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occurred: {e}")

