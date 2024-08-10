import cv2
import os

def extract_frames(video_file):
    cap = cv2.VideoCapture(video_file)

    frame_rate = 2
    frame_count = 0

    video_name = os.path.splitext(os.path.basename(video_file))[0]

    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Only extract frames at the desired frame rate
        if frame_count % int(cap.get(5) / frame_rate) == 0:
            output_file = f"{output_directory}/{frame_count}.jpg"
            cv2.imwrite(output_file, frame)
            print(f"Frame {frame_count} has been extracted and saved as {output_file}")

    cap.release()
    cv2.destroyAllWindows()


# use cli for input video file

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract frames from a video file")
    parser.add_argument("video_file", help="Path to the video file")
    args = parser.parse_args()

    extract_frames(args.video_file)
