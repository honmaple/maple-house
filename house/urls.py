#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-12 14:14:50 (CST)
# Last Update:星期二 2017-7-18 15:45:53 (CST)
#          By:
# Description:
# **************************************************************************
from house.views import (HouseHandler, RegisterHandler, LoginHandler,
                         BlockHouseHandler, BlockUserHandler)

__all__ = ['handlers']

handlers = [(r"/", HouseHandler), (r"/register", RegisterHandler),
            (r"/login", LoginHandler),
            (r"/block/house/(?P<pk>[0-9]+)", BlockHouseHandler),
            (r"/block/user/(?P<pk>[0-9]+)", BlockUserHandler)]
