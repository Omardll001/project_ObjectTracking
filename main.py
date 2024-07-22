from utils import read_video, save_video
from trackers import Tracker

def main():
    print("Starting main function...")
    # Read the video
    video_path = 'input_videos/madrid vs city.mp4'
    frames = read_video(video_path)
    print("Video read completed.")

    # Initialize the tracker
    tracker = Tracker('models/best2.pt')

    # Get object tracks
    tracks = tracker.get_object_tracks(frames, 
                                       read_from_stub=False, 
                                       stub_path='stubs/track_stubs.pkl')

    print("Tracks obtained.")
    # Draw the output tracks
    output_video_frames = tracker.draw_annotations(frames, tracks)
    
    # Save the video
    output_video_path = 'output_videos/output_video.avi'
    save_video(output_video_frames, output_video_path)
    print("Video saved.")

if __name__ == "__main__":
    main()
