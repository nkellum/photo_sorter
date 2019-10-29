# photo_sorter
This simple script moves photos from a directory into their respective
Year/Month directories which will be created if they do not exist.
If a file is not an photo (jpg), it will be moved to the Videos folder,
which is also created if it does not exist.
The images are sorted by date taken which is found in the image's
metadata using the exif package.

```usage: py photo_sorter.py dir_to_sort```
