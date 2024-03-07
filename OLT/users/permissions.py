from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем!"

    #  проверка пользователя на владельца
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class IsModeratorMaterials(BasePermission):
    message = "Вы не являетесь модератором!"

    # проверка пользователя на модератора курсов и уроков
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator_materials').exists():
            return True
        else:
            return False
