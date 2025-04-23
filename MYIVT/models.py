import datetime
import json
import os
import sys
from datetime import timedelta
from enum import Enum
from html import escape
from json import loads
from logging import getLogger
from re import match
from typing import Dict, List, Optional, Set, Union

from django.conf import settings
from django.contrib.auth.models import BaseUserManager, Group, Permission, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.core.validators import MinValueValidator, validate_comma_separated_integer_list
from django.db import connections, models, transaction
from django.db.models import Q
from django.db.models.manager import Manager
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.template import loader
from django.template.defaultfilters import linebreaksbr
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey, TreeManyToManyField
from mptt.models import MPTTModel

class BaseQuerySet(models.query.QuerySet):
    pass

class BaseManager(Manager.from_queryset(BaseQuerySet)):
    def get_queryset(self):
        pass

class BaseModel(models.Model):
    objects = BaseManager()

    class Meta:
        abstract = True

