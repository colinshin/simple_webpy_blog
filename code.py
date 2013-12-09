#!/usr/bin/env python
#-*- coding: utf-8 -*-

import web
import MySQLdb

from controllers.index import Index
from config.setting import app
from config.url import urls
from controllers.init import init_list
from controllers.init import blog_posts

if __name__ == "__main__":
    init_list()
    app.run()
