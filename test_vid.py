import cv2

def start_video():
    print("start video")
    # Create a video capture object for the camera (0 for default webcam)
    vid_capture = cv2.VideoCapture(0)

    # Define the output filename and codec
    output_filename = 'recorded_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Create a VideoWriter object to save the video
    output = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

    # Record video for 10 seconds
    duration = 15  # Set the desired duration in seconds
    start_time = cv2.getTickCount()

    while True:
        ret, frame = vid_capture.read()
        cv2.imshow('Recording...', frame)
        output.write(frame)

        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time >= duration:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    vid_capture.release()
    output.release()
    cv2.destroyAllWindows()

    print(f"Video saved as {output_filename}")
