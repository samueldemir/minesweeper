import settings


def height_prct(percentage):
    """

    :param percentage:
    :return:
    """
    return (settings.HEIGHT / 100) * percentage


def width_prct(percentage):
    """

    :param percentage:
    :return:
    """
    return (settings.WIDTH / 100) * percentage
