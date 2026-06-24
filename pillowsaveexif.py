from PIL import Image


def main():

    openfilepath = "photo.jpg"

    save_NO_exif(openfilepath, "photo_no_exif.jpg")
    save_WITH_exif(openfilepath, "photo_with_exif.jpg")


def save_NO_exif(openfilepath: str, savefilepath: str) -> None:

    try:

        image = Image.open(openfilepath)
        image_copy = image.copy()
        image_copy.save(savefilepath)

    except IOError as ioe:
        print(ioe)
    except ValueError as ve:
        print(ve)


def save_WITH_exif(openfilepath: str, savefilepath: str) -> None:

    try:

        image = Image.open(openfilepath)
        image_copy = image.copy()

        # if the image has no EXIF the dictionary key 
        # does not exist so we need to check
        if 'exif' in image.info:
            image_copy.save(savefilepath, exif=image.info['exif'])
            # OR
            # exif = image.info['exif']
            # image_copy.save(savefilepath, exif=exif)
        else:
            image_copy.save(savefilepath)

    except IOError as ioe:
        print(ioe)
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":

    main()