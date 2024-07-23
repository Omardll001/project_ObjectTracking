import sys
from utils.video_utils import read_video, save_video
from trackers.tracker import Tracker

def main(video_path, output_video_path):
    print("Starting main function...")
    # Read the video
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
    save_video(output_video_frames, output_video_path)
    print("Video saved.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_video_path> <output_video_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
