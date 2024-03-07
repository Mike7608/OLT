from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем!"

    #  проверка пользователя на владельца
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False


class IsModeratorMaterials(BasePermission):
    message = "Вы не являетесь модератором!"

    # проверка пользователя на модератора курсов и уроков
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator_materials').exists():
            return True
        else:
            return False
