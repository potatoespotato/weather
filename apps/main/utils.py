from django.db import ProgrammingError


def get_solo(model):
    try:
        config = model.get_solo()
    except ProgrammingError:
        config = None
    return config
