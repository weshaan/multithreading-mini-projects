from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    grayscale_image = image.convert('L')
    grayscale_image.save(output_image_path)

# Example usage
input_image_path = 'input_image.jpg'
output_image_path = 'output_grayscale_image.jpg'
convert_to_grayscale(input_image_path, output_image_path)
