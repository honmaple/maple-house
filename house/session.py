#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: session.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-18 16:28:36 (CST)
# Last Update:星期四 2017-7-20 14:43:19 (CST)
#          By:
# Description:
# **************************************************************************
from uuid import uuid4
from redis import StrictRedis
from functools import wraps
from datetime import datetime, timedelta
from pytz import timezone


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


def current_time(tz=None):
    if tz is None:
        tz = 'UTC'
    return datetime.now(timezone(tz))


class CoreSession(object):
    def __setitem__(self, key, value):
        '''
        session['username'] = 'hello'
        '''
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def get_or_set(self, key, value):
        if not self.get(key):
            self.set(key, value)
        return self.get(key)


@singleton
class MemorySession(CoreSession):
    def __init__(self):
        '''
        self._client = {'session_id1':{key:value},
                        'session_id2':{key:value}}
        '''
        self._client = {}

    def init(self, session_id, expires_days=30):
        self.session_id = 'session:{}'.format(session_id)
        self.expires_days = expires_days
        if self.session_id not in self._client:
            self._client[self.session_id] = {
                'is_authenticated': False,
                'expire': current_time() + timedelta(days=self.expires_days)
            }
        print(self.session_id)

    def set(self, key, value):
        self._client[self.session_id][key] = value

    def get(self, key):
        return self._client[self.session_id].get(key)

    def pop(self, key):
        return self._client[self.session_id].pop(key, None)

    def remove_expires(self):
        expire_sessions = []
        for key, value in self._client.items():
            if value['expire'] > current_time():
                expire_sessions.append(key)

    def clear(self):
        del self._client[self.session_id]


@singleton
class RedisSession(CoreSession):
    def __init__(self):
        self._client = StrictRedis(
            host='localhost',
            port=6379,
            db=0,
            password='redis',
            decode_responses=True)

    def init(self, session_id, expires_days=30):
        self.session_id = 'session:{}'.format(session_id)
        self.expires_days = expires_days
        if not self._client.exists(self.session_id):
            self._client.hset(self.session_id, 'is_authenticated', 0)
            self._client.expire(self.session_id, self.expires_days * 30 * 3600)

    def set(self, key, value):
        return self._client.hset(self.session_id, key, value)

    def get(self, key):
        return self._client.hget(self.session_id, key)

    def pop(self, key):
        return self._client.hdel(self.session_id, key)

    def clear(self):
        return self._client.delete(self.session_id)


class Session(object):
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.session_id = self.request_handler.get_secure_cookie("session")
        if not self.session_id:
            self.session_id = str(uuid4())
            self.request_handler.set_secure_cookie("session", self.session_id)
        # get cookies is bytes
        if isinstance(self.session_id, bytes):
            self.session_id = self.session_id.decode()
        self._session = RedisSession()
        # self._session = MemorySession()
        self._session.init(self.session_id)
        print(self.session_id)

    def __setitem__(self, key, value):
        self._session[key] = value

    def __getitem__(self, key):
        return self._session[key]

    def clear(self):
        self.request_handler.clear_cookie(self.session_id)
        return self._session.clear()
