#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-12 14:27:31 (CST)
# Last Update:星期四 2017-7-13 9:44:3 (CST)
#          By:
# Description:
# **************************************************************************
from house.globals import BaseModel
from peewee import CharField, IntegerField, ForeignKeyField


class User(BaseModel):
    username = CharField()
    password = CharField()

    def check_password(self, raw_password):
        return self.password == raw_password

    def set_password(self, raw_password):
        self.password = raw_password


class House(BaseModel):
    user = ForeignKeyField(User, related_name='houses')
    place = CharField()
    price = CharField()


class BlockUser(BaseModel):
    block_user = ForeignKeyField(
        User, related_name='block_users', help_text='屏蔽人')
    blocked_user = ForeignKeyField(
        User, related_name='blocked_users', help_text='被屏蔽人')


class BlockHouse(BaseModel):
    block_house_user = ForeignKeyField(
        User, related_name='block_house_users', help_text='屏蔽人')
    blocked_house_user = ForeignKeyField(
        House, related_name='blocked_house_users', help_text='被屏蔽主题')
