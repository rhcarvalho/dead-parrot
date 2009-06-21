# -*- coding: utf-8 -*-
from __future__ import absolute_import
from yaml import dump, load

from .base import Serializer

class YAMLSerializer(Serializer):
    format = "yaml"
    def __init__(self, obj):
        self.obj = obj

    def serialize(self):
        return dump(self.obj)

    @classmethod
    def deserialize(cls, yaml):
        return load(yaml)