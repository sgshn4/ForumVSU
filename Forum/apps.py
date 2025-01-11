import os

from django.apps import AppConfig


class Config(AppConfig):
    name = 'Forum'
    path = os.path.join(os.path.dirname(__file__), 'Forum')