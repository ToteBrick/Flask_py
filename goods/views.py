#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import goods

@goods.route('/goods')
def goods():
    return 'goods'