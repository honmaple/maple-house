#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: globals.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-12 14:25:34 (CST)
# Last Update:星期三 2017-7-12 14:34:34 (CST)
#          By:
# Description:
# **************************************************************************
from peewee import SqliteDatabase, Model

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db
