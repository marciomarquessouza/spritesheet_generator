import argparse
import os
import re
import math
import json
from PIL import Image

# Parse CLI arguments
parser = argparse.ArgumentParser(description="Generate a spritesheet from a set of images.")
parser.add_argument("basename", type=str, help="Base name of the image files (e.g., 'noise' for noise_1.png)")
parser.add_argument("--columns", type=int, default=3, help="Number of columns in the spritesheet (default: 3)")
parser.add_argument("--count", type=int, help="Number of images to include (optional)")

args = parser.parse_args()
basename = args.basename
columns = args.columns
image_pattern = re.compile(rf"{basename}_(\d+)\.png")

# Detect matching files
all_files = os.listdir(".")
matching_files = sorted(
    [f for f in all_files if image_pattern.fullmatch(f)],
    key=lambda x: int(image_pattern.fullmatch(x).group(1))
)

# Use count or all matching files
if args.count:
    frame_names = matching_files[:args.count]
else:
    frame_names = matching_files

if not frame_names:
    raise FileNotFoundError(f"No images found matching pattern: {basename}_<number>.png")

frame_count = len(frame_names)
rows = math.ceil(frame_count / columns)
sheet_filename = f"{basename}_spritesheet.png"
json_filename = f"{basename}_spritesheet.json"

# Load frames
frames = [Image.open(name).convert("RGBA") for name in frame_names]
frame_width, frame_height = frames[0].size

# Create spritesheet
sheet_width = frame_width * columns
sheet_height = frame_height * rows
sheet = Image.new("RGBA", (sheet_width, sheet_height))

# Prepare JSON metadata
data = {
    "frames": {},
    "meta": {
        "image": sheet_filename,
        "size": {"w": sheet_width, "h": sheet_height},
        "scale": "1"
    }
}

# Paste each frame into the sheet and add to JSON
for index, frame in enumerate(frames):
    col = index % columns
    row = index // columns
    x = col * frame_width
    y = row * frame_height
    sheet.paste(frame, (x, y))

    frame_id = f"{basename}_{index}"
    data["frames"][frame_id] = {
        "frame": {"x": x, "y": y, "w": frame_width, "h": frame_height},
        "rotated": False,
        "trimmed": False,
        "spriteSourceSize": {"x": 0, "y": 0, "w": frame_width, "h": frame_height},
        "sourceSize": {"w": frame_width, "h": frame_height}
    }

# Save output files
sheet.save(sheet_filename)
with open(json_filename, "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Generated {sheet_filename} and {json_filename} with {frame_count} frame(s) in {columns}x{rows} layout.")
