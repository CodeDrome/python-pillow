from PIL import Image

import colors_histogram


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| Pillow Histogram |")
    print("--------------------")

    filename = "photo.jpg"

    try:

        image = Image.open(filename)

        histograms = colors_histogram.create_histograms(image)

        if image.mode == "RGB":

            histograms["red"].save("histogram_red.png", "PNG")
            histograms["green"].save("histogram_green.png", "PNG")
            histograms["blue"].save("histogram_blue.png", "PNG")

        elif image.mode == "L":

            histograms["greyscale"].save("histogram_greyscale.png", "PNG")

        image.close()

        print("histograms saved")

    except IOError as e:

        print(e)

    except ValueError as e:

        print(e)


if __name__ == "__main__":

    main()
