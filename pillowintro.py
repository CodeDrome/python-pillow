import math

import PIL
from PIL import Image
from PIL import ImageEnhance


def main():

    print("--------------------------")
    print("| codedrome.com          |")
    print("| Introduction to Pillow |")
    print("--------------------------\n")

    print(f"Pillow version {PIL.__version__}\n")

    openfilepath = "photo.jpg"

    info_and_copy(openfilepath, "photo_copy.jpg")

    # resize(openfilepath, "photo_resized.jpg")

    # thumbnail(openfilepath, "photo_thumbnail.jpg")

    # rotate(openfilepath, "photo_rotated.jpg")

    # crop(openfilepath, "photo_cropped.jpg")

    # set_pixels(openfilepath, "photo_pixels_set.jpg")

    # color(openfilepath, "photo_color_enhanced.jpg")
    # contrast(openfilepath, "photo_contrast_enhanced.jpg")
    # brightness(openfilepath, "photo_brightness_enhanced.jpg")
    # sharpness(openfilepath, "photo_sharpness_enhanced.jpg")

    # add_watermark(openfilepath, "wmcw.png", "photo_watermark.jpg")


def info_and_copy(openfilepath: str, savefilepath: str) -> None:

    '''
    Outputs basic information about the specified 
    image and saves an unedited copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        print("filename:           {}".format(image.filename))
        print("size:               {}".format(image.size))
        print("width:              {}".format(image.width))
        print("height:             {}".format(image.height))
        print("format:             {}".format(image.format))
        print("format description: {}".format(image.format_description))
        print("mode:               {}".format(image.mode))

        image_copy = image.copy()

        image_copy.save(savefilepath)

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def resize(openfilepath: str, savefilepath: str) -> None:

    '''
    Creates and saves a small copy of the image.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        image = image.resize( (100, int(100 * (image.height / image.width))) )

        image.save(savefilepath)

        print("Image resized")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def thumbnail(openfilepath: str, savefilepath: str) -> None:

    '''    
    Creates and saves a thumbnail of the image.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        image.thumbnail((100, 100))

        image.save(savefilepath)

        print("Thumbnail created")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def rotate(openfilepath: str, savefilepath: str) -> None:

    '''
    Rotates image through 270 degrees and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        # without expand=1 the size of the image 
        # will remain the same, cropping any
        # non-square images.
        image = image.rotate(270, expand=1)

        image.save(savefilepath)

        print("Image rotated")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def crop(openfilepath: str, savefilepath: str) -> None:

    '''
    Crops the image and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        # the arguments are the top left and bottom 
        # right of the area to be cropped to
        image = image.crop((500, 200, 1200, 800))

        image.save(savefilepath)

        print("Image cropped")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def set_pixels(openfilepath: str, savefilepath: str) -> None:

    '''
    Sets a number of individual pixels and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        cx = int(image.width / 2)
        cy = int(image.height / 2)

        r = 0
        max_r = math.pi * 2.0
        r_inc = math.pi * 2.0 / 360.0
        radius = min(image.width, image.height) / 16

        while r <= max_r:

            px = int(math.cos(r) * radius) + cx
            py = int(math.sin(r) * radius) + cy

            image.putpixel((px, py), (255,255,255))
            r += r_inc

        image.save(savefilepath)

        print("Image pixels set")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def color(openfilepath: str, savefilepath: str) -> None:

    '''
    Edits the colour and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Color(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image color enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def contrast(openfilepath: str, savefilepath: str) -> None:

    '''
    Edits the contrast and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Contrast(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image contrast enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def brightness(openfilepath: str, savefilepath: str) -> None:

    '''
    Edits the brightness and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Brightness(image)

        image = enhancer.enhance(0.5)

        image.save(savefilepath)

        print("Image brightness enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def sharpness(openfilepath: str, savefilepath: str) -> None:

    '''
    Edits the sharpness and saves as a copy.
    Arguments:
        openfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Sharpness(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image sharpness enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def add_watermark(openfilepath: str, watermarkfilepath: str, savefilepath: str) -> None:

    '''
    Adds a watermark from a file and saves as a copy.
    Arguments:
        openfilepath
        watermarkfilepath
        savefilepath
    Return value:
        none
    '''

    try:

        main_image = Image.open(openfilepath).copy()
        watermark_image = Image.open(watermarkfilepath).copy()

        # calculate position of watermark to leave
        # a bit of space (16px) at the bottom right.
        x = main_image.size[0] - watermark_image.size[0] - 16
        y = main_image.size[1] - watermark_image.size[1] - 16

        main_image.paste(watermark_image, (x, y), watermark_image)

        main_image.save(savefilepath)

        print("Watermark added")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


if __name__ == "__main__":

    main()
