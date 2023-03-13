#!/usr/bin/env python

import sys
import subprocess
import os
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Input file path
file_in = sys.argv[1]
# Output file path
file_out = sys.argv[2]
# Silence timestamps
silence_file = sys.argv[3]

# Ease in duration between cuts
try:
    ease = float(sys.argv[4])
except IndexError:
    ease = 0.0

minimum_duration = 1.0

def main():
    # start of next clip
    last = 0

    with open(silence_file, "r", errors='replace') as in_handle:
        timestamps = [tuple(map(float, line.strip().split())) for line in in_handle.readlines()]

    video = VideoFileClip(file_in)
    full_duration = video.duration
    clips = []
    for i, (end, duration) in enumerate(timestamps):
        to = end - duration

        start = last
        clip_duration = to - start
        # Clips less than one seconds don't seem to work
        print("Clip Duration: {} seconds".format(clip_duration))

        if clip_duration < minimum_duration:
            continue

        if full_duration - to < minimum_duration:
            continue

        if start > ease:
            start -= ease

        print("Clip {} (Start: {}, End: {})".format(i, start, to))
        clip = video.subclip(start, to)
        clips.append(clip)
        last = end

    if full_duration - last > minimum_duration:
        print("Clip {} (Start: {}, End: {})".format(len(timestamps), last, 'EOF'))
        clips.append(video.subclip(last-ease))

    processed_video = concatenate_videoclips(clips)
    processed_video.write_videofile(
        file_out,
        fps=30,
        preset='ultrafast',
        codec='libx265'
    )

    video.close()

main()
