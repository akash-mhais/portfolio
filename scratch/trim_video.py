import os
from moviepy import VideoFileClip

# Paths
input_file = r"CartesianRobot\hero_demo.mp4"
output_file = r"CartesianRobot\hero_demo_final.mp4"

def trim_video():
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return

    print(f"Loading {input_file}...")
    with VideoFileClip(input_file) as clip:
        # Check duration
        print(f"Original Duration: {clip.duration:.2f}s")
        if clip.duration <= 3:
            print("Error: Video is shorter than 3 seconds.")
            return

        # Trim from 3s to end
        print("Trimming first 3 seconds...")
        final_clip = clip.subclipped(3, clip.duration)
        
        # Write output - using 'libx264' for broad compatibility
        print(f"Saving to {output_file}...")
        final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print("Done!")

if __name__ == "__main__":
    trim_video()
