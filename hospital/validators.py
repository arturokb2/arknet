def validate_file(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.dbf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неверный тип файла')