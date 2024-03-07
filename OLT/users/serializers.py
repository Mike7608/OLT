from rest_framework import serializers

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'  # ['id', 'user_id', 'date_pay', 'pay_course', 'pay_lesson', 'pay_summ', 'pay_method']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

