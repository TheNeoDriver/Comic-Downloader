from PIL import ImageEnhance


RANGE_LIMIT = 127


def get_factor(value):
    value = RANGE_LIMIT if value > RANGE_LIMIT else value
    value = -RANGE_LIMIT if value < -RANGE_LIMIT else value
    factor = (RANGE_LIMIT+1 * (value + RANGE_LIMIT)) / (RANGE_LIMIT+1 * (RANGE_LIMIT - value))
    return factor


def change_contrast(image, value):
    factor = get_factor(value)
    image = ImageEnhance.Contrast(image).enhance(factor)
    return image


def change_brightness(image, value):

    def brightness(c):
        c += value
        return c

    image = image.point(brightness)
    return image


def change_color(image, value):
    factor = get_factor(value)
    image = ImageEnhance.Color(image).enhance(factor)
    return image
