from PIL import Image

def normalize_image(filename):
    img = Image.open('./' + filename).convert('L').transpose(Image.FLIP_TOP_BOTTOM)
    img.save(filename)