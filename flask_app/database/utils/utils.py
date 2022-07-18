def format_model(cls: object, attrs: list) -> dict:
    return {str(attr):cls.__getattribute__(attr) for attr in attrs}