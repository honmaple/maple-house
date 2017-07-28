#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-12 14:16:15 (CST)
# Last Update:星期四 2017-7-20 12:6:0 (CST)
#          By:
# Description:
# **************************************************************************
from tornado.web import RequestHandler, authenticated
from house.models import User, House
from house.utils import BaseHandler


class RegisterHandler(BaseHandler):
    def get(self):
        self.render2('register.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = User(username=username)
        user.set_password(password)
        user.save()
        self.redirect('/login')


class LoginHandler(BaseHandler):
    def get(self):
        print(self.session['username'])
        print(self.session['aaaa'])
        # self.session.clear()
        self.render2('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = User.select().where(User.username == username).first()
        if user and user.check_password(password):
            self.session['username'] = username
            self.session['is_authenticated'] = True
            self.redirect(self.get_argument('next', '/'))
        else:
            self.redirect('/')


class LogoutHandler(BaseHandler):
    @authenticated
    def get(self):
        if self.get_argument("logout", None):
            self.clear_cookie("username")
        self.redirect("/")


class HouseHandler(BaseHandler):
    def get(self):
        users = User.select()
        houses = House.select()
        self.render2('index.html', houses=houses, users=users)
        # self.write('hello world!')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = User.create(username=username, password=password)
        user.save()
        self.redirect('/')
        # self.write('hello {}'.format(username))


class BlockUserHandler(BaseHandler):
    def post(self, pk):
        self.write('ss {}'.format(pk))

    def get(self, pk):
        self.write('ss {}'.format(pk))


class BlockHouseHandler(BaseHandler):
    def post(self, pk):
        pass

    def get(self, pk):
        self.write('ss {}'.format(pk))
