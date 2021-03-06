#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from unit2 import hw1
from unit2 import hw2
from unit3 import myBlog
from final import myWiki

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

WIKI_PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

app = webapp2.WSGIApplication([
    ('/', MainHandler), 
    ('/unit2/hw1', hw1.Hw1MainHandler),
    ('/unit2/hw2', hw2.Hw2MainHandler), 
    ('/unit2/hw2/welcome', hw2.HelloHandler),

    # My Blog
    ('/myblog', myBlog.MyBlogMainPage),
    ('/myblog/.json', myBlog.MyBlogMainPageJSON),
    ('/myblog/signup', myBlog.SignUpPage),
    ('/myblog/login', myBlog.LoginPage),
    ('/myblog/logout', myBlog.Logout),
    ('/myblog/welcome', myBlog.WelcomePage),
    ('/myblog/newpost', myBlog.NewPostPage),
    ('/myblog/flush', myBlog.FlushAll),
    ('/myblog/(\d+)', myBlog.Permalinks),
    ('/myblog/(\d+).json', myBlog.PermalinksJSON),

    # My Wiki
    ('/mywiki', myWiki.MainPage),
    ('/mywiki/signup', myWiki.SignUpPage),
    ('/mywiki/login', myWiki.LoginPage),
    ('/mywiki/logout', myWiki.Logout),
    ('/mywiki/_edit/'+WIKI_PAGE_RE, myWiki.EditWikiPageHandler),
    ('/mywiki/'+WIKI_PAGE_RE, myWiki.WikiPageHandler)
], debug=True)
