from rembg import remove
from PIL import Image
input_path = 'adham.jpg'
output_path = 'removed.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
