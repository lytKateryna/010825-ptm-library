"""
Задание 1. список пользователей доступен только администраторам
Эндпоинты:
Требования
Реализовать custom permission, который:
Разрешает доступ только администраторам.
Для всех остальных аутентифицированных пользователей возвращает 403.
Подключить permission к эндпоинтам списка и детализации пользователей.
Для анонимного пользователя возвращать 401.
Задание 2
пользователь может смотреть только свой профиль
Эндпоинты:
Требования
Реализовать permission, который:
Разрешает доступ, если тот, кто делает запрос -- это владелец объекта.
Администратору разрешает доступ к любому объекту пользователя.
Разрешить редактирование только своих данных:
first_name
last_name
phone
Запретить изменение:
role
is_staff
is_superuser
deleted
При нарушении прав возвращать 403 с понятным сообщением.
"""

from rest_framework.permissions import BasePermission


class IsAdminOnly(BasePermission):

    def has_permission(self, request, view):
        #if request.user.role == 'admin':
        #     return True
        # return False
        print(request.user)
        return request.user and request.user.is_authenticated and request.user.role == 'admin'


    def has_object_permission(self, request, view, obj):
        if view.action == 'get_me':
            if request.user and request.user.is_authenticated and request.user.role == 'admin'
                return True
            elif request.user and request.user.is_authenticated and request.user.id == obj.id:
                return True

        return request.user and request.user.is_authenticated and request.user.role == 'admin'
