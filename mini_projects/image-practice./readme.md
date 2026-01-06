Image Brightness Analyzer

This Python script reads views.csv containing image IDs, calculates the brightness of each corresponding JPEG image, and writes the results to analysis.csv with an added brightness column. Brightness is computed by converting each image to grayscale and averaging pixel values (0–1). Requires numpy and Pillow.

Usage: 

Place your JPEG images and views.csv in the same folder, then run:
python script.py

After running, analysis.csv will contain all original data plus a brightness column.
