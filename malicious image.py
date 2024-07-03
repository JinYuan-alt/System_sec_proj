from PIL import Image
from PIL.ExifTags import TAGS

img=Image.open(r'me.jpg')
#just for testing
# open the image


# extracting the exif metadata
exifdata = img.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")

    if "<" or ">" in tagname:
        tagname.replace(" ")

