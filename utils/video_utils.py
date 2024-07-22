import os
import cv2

def read_video(video_path):
    # Open the video file at the given path
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            # If no frame is returned (end of video), break the loop
            break
        # Append the frame to the list of frames
        frames.append(frame)
    
    # Return the list of frames
    return frames      

def save_video(output_video_frames, output_video_path):  
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Create a VideoWriter object to write the video to the output path
    # The parameters are: output path, codec, frame rate, and frame size
    out = cv2.VideoWriter(output_video_path ,fourcc,24,(output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    
    for frame in output_video_frames:
        # Write each frame to the output video
        out.write(frame)
    
    # Release the VideoWriter object
    out.release()
