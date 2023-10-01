from PIL import Image


def resize_image(source, destination, size):
    try:
        # Open the image file
        image = Image.open(source)

        # Resize the image
        resized_image = image.resize(size)

        # Save the resized image to the output path
        resized_image.save(destination)
        print(f"Image resized and saved to {destination}")

    except Exception as e:
        print(f"An error occurred: {e}")

input_path = "1.png"
output_path = "resized.jpg"
size = (500, 500)
resize_image(input_path, output_path, size)
