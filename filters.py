from PIL import Image, ImageEnhance, ImageFilter

def gray_scale(image):
    return image.convert("L")

def invert_colors(image):
    return Image.eval(image, lambda x: 255 - x)

def enhance_contrast(image, factor=1.5):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=5))

def sharpen(image):
    return image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

def edge_detection(image):
    return image.filter(ImageFilter.FIND_EDGES)

def rotate(image, angle=90):
    return image.rotate(angle)

def resize(image, size):
    return image.resize(size)
