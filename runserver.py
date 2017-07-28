#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: runserver.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-07-12 14:14:18 (CST)
# Last Update:星期四 2017-7-20 10:2:7 (CST)
#          By:
# Description:
# **************************************************************************
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from house import create_app
from house.globals import db
from house.models import User, House, BlockHouse, BlockUser

define("port", default=8000, help="run on the given port", type=int)
define('cmd', default='runserver', metavar='runserver|syncdb')
app = create_app()


def syncdb():
    db.connect()
    db.create_tables([User, House, BlockHouse, BlockUser])


def runserver():
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    options.parse_command_line()
    if options.cmd == 'syncdb':
        syncdb()
    else:
        runserver()
