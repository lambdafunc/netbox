import strawberry
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from strawberry import auto
from users import filtersets
from utilities.querysets import RestrictedQuerySet
from .filters import *

__all__ = (
    'GroupType',
    'UserType',
)


@strawberry.django.type(
    Group,
    fields=['id', 'name'],
    filters=GroupFilter
)
class GroupType:
    @classmethod
    def get_queryset(cls, queryset, info, **kwargs):
        return RestrictedQuerySet(model=Group).restrict(info.context.request.user, 'view')


@strawberry.django.type(
    get_user_model(),
    fields=[
        'id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff',
        'is_active', 'date_joined', 'groups',
    ],
    filters=UserFilter
)
class UserType:
    @classmethod
    def get_queryset(cls, queryset, info, **kwargs):
        return RestrictedQuerySet(model=get_user_model()).restrict(info.context.request.user, 'view')
