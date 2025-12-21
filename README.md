# 🖼️ Spritesheet Generator (Python + Pillow)

This Python script generates a spritesheet and a matching JSON file from a set of images, using a configurable **base filename prefix** via command line.

## 📦 Output

- A `spritesheet.png` combining the input frames
- A `spritesheet.json` with frame metadata

## 🧰 Requirements

- Python 3.6 or higher
- Pillow (Python Imaging Library fork)

Install dependencies:

```bash
pip install pillow
```

## 🚀 Usage

### 1. Prepare your images

Ensure your images follow the pattern:

```
<basename>_01.png
<basename>_02.png
...
<basename>_06.png
```

All images must be the same size and placed in the same directory as the script.

Example:

```
noise_01.png
noise_02.png
...
noise_06.png
```

### 2. Run the script

```bash
python generate_spritesheet.py noise
```

Replace `noise` with your desired base name.

This will generate:

- `noise_spritesheet.png`
- `noise_spritesheet.json`

## 🛠 Changing the Layout or Frame Count

By default, the script assumes:

- 6 frames total
- A layout of `3 columns x 2 rows`

To modify this, open the script and update:

```python
frame_names = [f"{basename}_{str(i).zfill(2)}.png" for i in range(1, 7)]
columns = 3
rows = 2
```

For example, for 9 frames in a 3x3 grid:

```python
frame_names = [f"{basename}_{str(i).zfill(2)}.png" for i in range(1, 10)]
columns = 3
rows = 3
```

## 📁 JSON Output Format

The script generates a JSON file with metadata in this format:

```json
{
  "frames": {
    "noise_0": {
      "frame": { "x": 0, "y": 0, "w": 64, "h": 64 },
      "rotated": false,
      "trimmed": false,
      "spriteSourceSize": { "x": 0, "y": 0, "w": 64, "h": 64 },
      "sourceSize": { "w": 64, "h": 64 }
    }
  },
  "meta": {
    "image": "noise_spritesheet.png",
    "size": { "w": 192, "h": 128 },
    "scale": "1"
  }
}
```
