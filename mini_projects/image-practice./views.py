import csv
import numpy as np
from PIL import Image


""" uses open and DictReader to print out the id numbers from views.csv """
# def main():
#     with open("views.csv", "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row["id"])


""" uses the brightness function to print out the brightnesses of the jpegs using their corresponding ids """
# def main():
    # with open("views.csv", "r") as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         brightness = calculate_brightness(f"{row['id']}.jpeg")
    #         print(round(brightness,2))



""" opens existing file and creates a new csv file in one line, adds a new header, and adds the calculations from the brightness funtion to the corresponding brightness column in new file """

# def main():
#     with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
#         reader = csv.DictReader(views)
#         writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])   # could be done by hand like this: fieldnames = ["id", "english_title", etc.], but  reader stores them as a list for ease of use
#         writer.writeheader()   # adds the info from writer to the actual doc

#         for row in reader:
#             brightness = calculate_brightness(f"{row['id']}.jpeg")
#             writer.writerow(                     # writerow uses dictionaries to organize info
#                 {
#                     "id": row["id"],
#                     "english_title": row["english_title"],
#                     "japanese_title": row["japanese_title"],
#                     "brightness": round(brightness, 2)
#                 }
#             )



""" most concise version: instead of making a new dictionary, a new key is added instead """

def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)




def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L")))/255
    return brightness


main()


