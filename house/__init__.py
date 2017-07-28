#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-10 13:34:43 (CST)
# Last Update:星期二 2017-7-18 17:44:18 (CST)
#          By:
# Description:
# **************************************************************************
from tornado.web import Application
from house.urls import handlers
import os


def create_app():
    template_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Application(
        handlers=handlers,
        template_path=template_path,
        static_path=static_path,
        debug=True,
        cookie_secret='asdadasdadasdasdasda')
    return app
