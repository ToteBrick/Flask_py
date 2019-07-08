#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

goods = Blueprint('goods', __name__)

from . import views