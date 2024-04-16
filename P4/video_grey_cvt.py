import cv2

def convert_video_to_grayscale(input_video_path, output_video_path):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)
    
    # Get the video properties
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=False)
    
    # Read until video is completed
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Write grayscale frame to output video
        out.write(gray_frame)
    
    # Release video objects
    video_capture.release()
    out.release()

# Example usage
input_video_path = 'image6.wmv'
output_video_path = 'output_grayscale_video.wmv'
convert_video_to_grayscale(input_video_path, output_video_path)
