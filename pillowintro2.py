import PIL
from PIL import Image
from PIL import ImageEnhance


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Pillow 2      |")
    print("-----------------\n")

    openfilepath = "photo.jpg"

    show_image_info(openfilepath)

    # The desaturate function is the wrong way to change an image
    # to black and white and is included here with show_image_info
    # to demonstrate that it leaves the image with a mode of RGB
    # desaturate(openfilepath, "photo_desaturated.jpg")
    # show_image_info("photo_desaturated.jpg")

    # This is the correct way to convert an image to B&W.
    # Calling show_image_info will show a mode of L
    # mode_L(openfilepath, "photo_mode_L.jpg")
    # show_image_info("photo_mode_L.jpg")

    # contrast("photo_mode_L.jpg", "photo_mode_L_contrast.jpg", 1.5)

    # bands_brightness(openfilepath, "photo_bands_brightness.jpg", 1.2, 1.0, 1.0)

    # quality_demo(openfilepath)


def show_image_info(openfilepath: str) -> None:

    """
    Open an image and show a few attributes
    """

    try:

        image = Image.open(openfilepath)

        print("filename:           {}".format(image.filename))
        print("size:               {}".format(image.size))
        print("width:              {}".format(image.width))
        print("height:             {}".format(image.height))
        print("format:             {}".format(image.format))
        print("format description: {}".format(image.format_description))
        print("mode:               {}\n".format(image.mode))

    except IOError as ioe:

        print(ioe)


def desaturate(openfilepath: str, savefilepath: str) -> None:

    """
    Convert an image to black and white the wrong way.
    This method still leaves the image with a colour
    depth of 24 bit RGB.
    The correct method is to use convert("L")
    """

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Color(image)

        image = enhancer.enhance(0.0)

        image.save(savefilepath)

        print("Image desaturated")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def mode_L(openfilepath: str, savefilepath: str) -> None:

    """
    The correct way to convert an image to black and white.
    Do not use ImageEnhance.Color to reduce saturation to 0
    as that leaves the colour depth at 24 bit.
    """

    try:

        image = Image.open(openfilepath)

        image = image.convert("L")

        image.save(savefilepath)

        print("Mode changed to L")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def contrast(openfilepath: str, savefilepath: str, amount: float) -> None:

    """
    A general-purpose function to change the contrast
    by the specified amount and save the image.
    """

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Contrast(image)

        image = enhancer.enhance(amount)

        image.save(savefilepath)

        print("Contrast changed")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def bands_brightness(openfilepath: str, savefilepath: str, r: float, g: float, b: float) -> None:

    """
    Split the image into colour channels (bands).
    Change the brightness of each by the specified amount (1 = no change).
    Merge the channels and save the image.
    """

    try:

        image = Image.open(openfilepath)

        # image.split() returns a tuple so we need to convert
        # it to a list so we can overwrite the bands.
        bands = list(image.split())

        enhancer = ImageEnhance.Brightness(bands[0])
        bands[0] = enhancer.enhance(r)

        enhancer = ImageEnhance.Brightness(bands[1])
        bands[1] = enhancer.enhance(g)

        enhancer = ImageEnhance.Brightness(bands[2])
        bands[2] = enhancer.enhance(b)

        image = PIL.Image.merge("RGB", bands)

        image.save(savefilepath)

        print("Band brightnesses changed")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def quality_demo(openfilepath: str) -> None:

    """
    Save the specified image at several different quality levels
    for demonstration purposes.
    Quality can be any value between 1 (awful) to 100 (best).
    Anything < 50 is unlikely to be acceptable.
    """

    try:

        image = Image.open(openfilepath)

        for q in range(25, 101, 25):

            filename = f"quality {q}.jpg"

            image.save(filename, quality=q)

            print(f"Image saved at quality {q}")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


if __name__ == "__main__":

    main()
