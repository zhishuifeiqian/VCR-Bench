import os
import math
import ffmpeg
import json
from tqdm import tqdm
import argparse

def extract_frames(video_path, output_folder, num_frames=32):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Input video file not found: {video_path}")

    probe = ffmpeg.probe(video_path)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')

    try:
        total_frames = int(video_info['nb_frames'])
    except KeyError:
        duration = float(video_info['duration'])
        avg_frame_rate = eval(video_info['avg_frame_rate'])
        total_frames = int(duration * avg_frame_rate)

    if total_frames < num_frames:
        print(f"Warning: Video {video_path} only has {total_frames} frames, which is less than requested {num_frames} frames.")
        num_frames = total_frames

    duration = float(video_info['duration'])
    fps = float(video_info['r_frame_rate'].split('/')[0]) / float(video_info['r_frame_rate'].split('/')[1])

    frame_indices = [math.floor(i * total_frames / num_frames) for i in range(num_frames)]
    timestamps = [round(frame_index / fps, 1) for frame_index in frame_indices]

    os.makedirs(output_folder, exist_ok=True)

    frames = []
    for i, timestamp in enumerate(timestamps):
        frame_name = f'frame_{i + 1:03d}.jpg'
        output_path = output_folder + '/' + frame_name
        try:
            (
                ffmpeg
                .input(video_path, ss=timestamp)
                .output(output_path, vframes=1, format='image2', vcodec='mjpeg')
                .run(quiet=True, overwrite_output=True)
            )

            frames.append(output_path)
        except ffmpeg.Error as e:
            print(f"Failed to extract frame: {e}")
            continue  

    return timestamps, frames


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract frames from videos listed in a JSON file')
    parser.add_argument('--input_json', required=True, help='Path to input JSON file')
    parser.add_argument('--output_json', required=True, help='Path to output JSON file')
    parser.add_argument('--num_frames', type=int, default=64, help='Number of frames to extract per video')
    args = parser.parse_args()

    data = json.load(open(args.input_json, "r", encoding="utf-8"))

    for line in tqdm(data):
        video_path = line["video_path"]  
        
        output_relative_path = line["video_path"].replace("video", "frames_" + str(args.num_frames), 1)
        output_folder = os.path.dirname(output_relative_path) + '/' + os.path.splitext(os.path.basename(output_relative_path))[0]

        try:
            timestamps, frames = extract_frames(video_path, output_folder, args.num_frames)
            line["timestamps"] = timestamps
            line["frames"] = frames
        except Exception as e:
            print(f"Error processing video {video_path}: {e}")

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Processing completed!")