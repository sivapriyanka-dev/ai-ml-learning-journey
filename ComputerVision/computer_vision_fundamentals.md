# Day 36 — Computer Vision Fundamentals

1. What is an image mathematically?
   A computer sees an image as numbers.
   Example:
   A grayscale image: Each number = pixel intensity. So grayscale image = 2D matrix
   [[0, 120, 255],
[34, 90, 180],
[255, 10, 60]]
   Each number = pixel intensity
   0 → black
   255 → white
   values between → shades of gray
   Shape: (height, width) => (28, 28) => 28 rows 28 columns

2. RGB Images
   Color images have 3 channels: Red, Green, Blue
   Shape: (height, width, channels) => (224, 224, 3) => Means:
   224 pixels height
   224 pixels width
   3 color channels
   [0,255,0] # green
   [0,0,255] # blue
   [255,255,255] # white
   [0,0,0] # black

3. Pixels
   Pixel = smallest unit of image.
   A 224×224 image has: 224 \* 224 = 50,176 pixels
   Each pixel has values.
   RGB image: 50,176 × 3 values
   That’s what model learns from.

4. Resizing
   Models need fixed image size.
   Example:
   image 1 → 500×700
   image 2 → 200×300
   Cannot directly train. Need: resize all → 128×128
   Common sizes:
   64×64
   128×128
   224×224

5. Normalization
   Pixel values: 0 to 255
   Neural networks train better with: 0 to 1
   Formula: image = image / 255.0
   Example:
   255 → 1.0
   128 → 0.50
   0 → 0

6. Train / Validation / Test Split
   Typical split:
   70% train
   15% validation
   15% test
   Meaning:
   Train: learn patterns
   Validation: tune model
   Test: final evaluation
