# Photo Sorter by Nicolas Kellum
#
# This simple script moves photos from a directory into their respective
# Year/Month directories which will be created if they do not exist.
# If a file is not an photo (jpg), it will be moved to the Videos folder,
# which is also created if it does not exist.
# The images are sorted by date taken which is found in the image's
# metadata using the exif package.


from exif import Image
import os
import shutil
import sys

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def get_date_taken(img_name):
    with open(img_name, 'rb') as image_file:
        my_image = Image(image_file)
        if(my_image.has_exif):
            return my_image.datetime.split(" ")[0]
        else:
            return 0


def get_year_taken(datetime):
    return datetime.split(":")[0]


def get_month_taken(datetime):
    return datetime.split(":")[1]


def sort_image(filename, dir):
    datetime = get_date_taken(dir + "/" + filename)
    if(datetime == 0):
        return
    year = get_year_taken(datetime)
    month = get_month_taken(datetime)
    month = months[int(month) - 1]
    if(not os.path.isdir(dir + "/" + year)):
        os.mkdir(dir + "/" + year)
    if(not os.path.isdir(dir + "/" + year + "/" + month)):
        os.mkdir(dir + "/" + year + "/" + month)
    shutil.move(dir + "/" + filename, dir + "/" + year + "/" + month)


if(len(sys.argv) == 1):
    print("usage: py sort.py [dir_to_sort]")
    exit()
if(not os.path.isdir(sys.argv[1])):
    print(sys.argv[1] + " does not seem to be a directory.")
    exit()
if(not os.path.isdir(sys.argv[1] + "/Videos")):
    os.mkdir(sys.argv[1] + "/Videos")
print("Sorting images in " + sys.argv[1] + "...")
for filename in os.listdir(sys.argv[1]):
    if filename.endswith(".jpg"):
        sort_image(filename, sys.argv[1])
    else:
        shutil.move(sys.argv[1] + "/" + filename, sys.argv[1] + "/Videos")

print("Done.")
