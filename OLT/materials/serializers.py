from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    count_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'pict', 'description', 'lessons', 'count_lessons')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lessons'] = LessonSerializer(instance.lesson_set.all(), many=True).data
        return data

    def get_count_lessons(self, instance):
        return instance.lesson_set.count()


