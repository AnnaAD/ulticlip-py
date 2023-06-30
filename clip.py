# from moviepy.config import change_settings
# change_settings({"FFMPEG_BINARY": "/usr/bin/ffmpeg"})

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from datetime import datetime as dt

def split_video(input_file, start_time, end_time, output_file):
    start_format = "%H:%M:%S" if len(start_time.split(":")) == 3 else "%M:%S"
    start = dt.strptime(start_time, start_format)
    end_format = "%H:%M:%S" if len(end_time.split(":")) == 3 else "%M:%S"
    end = dt.strptime(end_time, end_format)
    delta = start - dt.strptime("", "")
    start_seconds = int(delta.total_seconds())
    delta = end - dt.strptime("", "")
    end_seconds = int(delta.total_seconds())
    ffmpeg_extract_subclip(input_file, start_seconds, end_seconds, targetname=output_file)

import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python clip.py <input_file> <timestamps_file> <output_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    timestamps_file = sys.argv[2]
    output_directory = sys.argv[3]

    with open(timestamps_file, "r") as file:
        for index, line in enumerate(file):
            timestamp, clip_name = line.strip().split(": ")
            start_time, end_time = timestamp.split("-")
            output_file = f"output/{clip_name.replace(' ', '-')}-{start_time}-{end_time}.mp4"
            print(start_time)
            print(end_time)
            split_video(input_file, start_time, end_time, output_file)
            print(f"Clip {index+1} saved as {output_file}")