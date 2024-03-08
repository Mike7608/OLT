from rest_framework.serializers import ValidationError


class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # https://www.youtube.com, https://youtu.be

        if 'url_video' in value:
            list_y = ['www.youtube.com/', '/youtu.be/']
            result = False

            for val in list_y:
                if val in value['url_video']:
                    result = True

            if not result:
                raise ValidationError("Недопустимая ссылка")
