from rest_framework.serializers import ValidationError


class HabitValidator:
    """Validator привычек."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value["duration"] > 120:
            raise ValidationError(
                "Время выполнения привычки не может превышать 120 секунд."
            )

        if value["periodicity"] > 7:
            raise ValidationError(
                "Периодичность выполнения привычки не может быть реже чем один раз в неделю."
            )

        if value["related_habit"] and value["award"]:
            raise ValidationError(
                "Нельзя выбирать связанную привычку и вознаграждение одновременно."
            )

        if value["related_habit"]:
            if not value["related_habit"].sign_pleasant_habit:
                raise ValidationError(
                    "В связанные привычки можно выбрать только привычки с признаком приятной привычки."
                )

        if value["sign_pleasant_habit"]:
            if value["award"] or value["related_habit"]:
                raise ValidationError(
                    "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
                )
