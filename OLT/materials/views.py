from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsOwner, IsModeratorMaterials


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        match self.action:
            case 'list':
                permission_classes = [IsAuthenticated]
            case 'create':
                permission_classes = [IsAuthenticated, ~IsModeratorMaterials]
            case 'retrieve':
                permission_classes = [IsAuthenticated, IsModeratorMaterials | IsOwner]
            case 'update':
                permission_classes = [IsAuthenticated, IsModeratorMaterials | IsOwner]
            case 'destroy':
                permission_classes = [IsAuthenticated, IsOwner]
            case _:
                permission_classes = None

        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    # create
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModeratorMaterials]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    #  list
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    # detail
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorMaterials | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    # update
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorMaterials | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    # delete
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

