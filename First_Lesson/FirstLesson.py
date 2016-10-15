# # # # import urllib
# # # # import urllib2
# # # # # # # response = urllib2.urlopen('http://www.baidu.com')
# # # # # # request = urllib2.Request('http://www.baidu.com')
# # # # # # response = urllib2.urlopen(request)
# # # # # # print response.read()
# # # # # 
# # # # # # values = {'username' : '1016903103@qq.com', 'password' : 'XXXX'}
# # # # # # values = {}
# # # # # # values['username'] = '1016903103@qq.com'
# # # # # # values['password'] = 'XXXX'
# # # # # # data = urllib.urlencode(values)
# # # # # # url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# # # # # # request = urllib2.Request(url,data)
# # # # # # response = urllib2.urlopen(request)
# # # # # # print response.read()
# # # # # # 
# # # # # # values = {'username' : '1016903103@qq.com', 'password' : 'XXXX'}
# # # # # # data = urllib.urlencode(values)
# # # # # # url = 'http://passport.csdn.net/account/login'
# # # # # # geturl = url + '?' + data
# # # # # # request = urllib2.Request(geturl)
# # # # # # response = urllib2.urlopen(request)
# # # # # # print geturl
# # # # # # print response.read()
# # # # # 
# # # # # values = {'username' : '1016903103@qq.com', 'password' : 'XXXX'}
# # # # # data = urllib.urlencode(values)
# # # # # url = 'http://passport.csdn.net/account/login'
# # # # # request = urllib2.Request(url, data)
# # # # # response = urllib2.urlopen(request)
# # # # # print response.read()
# # # # 
# # # # 
# # # # # import urllib
# # # # # import urllib2
# # # # url = 'http://www.server.com/login'
# # # # # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# # # # values = {'username' : 'cqc', 'password' : 'XXXX'}
# # # # headers = {'User-Agent' : user_agent, 'Referer' : 'http://ww.zhihu.com/articles'}
# # # # data = urllib.urlencode(values)
# # # # # request = urllib2.Request(url, data, headers)
# # # # # response = urllib2.urlopen(request, timeout = 10)
# # # # # page = response.read()
# # # # # 
# # # # # enable_proxy = True
# # # # # proxy_handler = urllib2.ProxyHandler({'http' : 'http://some_proxy.com:8080'})
# # # # # null_proxy_handler = urllib2.ProxyHandler({})
# # # # # if enable_proxy:
# # # # #     opener = urllib2.build_opener(proxy_handler)
# # # # # else:
# # # # #     opener = urllib2.build_opener(null_proxy_handler)
# # # # # urllib2.install_opener(opener)
# # # # 
# # # # request = urllib2.Request(url, data = data)
# # # # request.get_method = lambda: 'PUT' # or 'DELETE'
# # # # response = urllib2.urlopen(request)
# # # # 
# # # # httpHandler = urllib2.HTTPHandler(debuglevel = 1)
# # # # httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
# # # # opener = urllib2.build_opener(httpHandler, httpsHandler)
# # # # urllib2.install_opener(opener)
# # # # response = urllib2.urlopen(url)
# # # 
# # # import urllib2
# # # request = urllib2.Request('http://www.xxxxxxxxxxxxx.com')
# # # try:
# # #     urllib2.urlopen(request)
# # # except urllib2.URLError, e:
# # #     print e.reason
# # 
# # 
# # # import urllib2
# # # 
# # # req = urllib2.Request('http://blog.csdn.net/cqcre')
# # # try:
# # #     urllib2.urlopen(req)
# # # except urllib2.HTTPError, e:
# # #     print e.code
# # # except urllib2.URLError, e:
# # #     print e.reason
# # # else:
# # #     print 'OK'
# # 
# # import urllib2
# # 
# # req = urllib2.Request('http://blog.csdn.net/cqcre')
# # try:
# #     urllib2.urlopen(req)
# # except urllib2.URLError, e:
# #     if hasattr(e, 'code'):
# #         print e.code
# #     if hasattr(e, 'reason'):
# #         print e.reason
# # else:
# #     print 'OK'
# #     
# #     
# #     
# # import urllib2
# # import cookielib
# # # declare cookie as class cookiejar()
# # cookie = cookielib.CookieJar()
# # # use HTTPCookieProcessor to treat cookie
# # handler = urllib2.HTTPCookieProcessor(cookie)
# # # use the handler to create opener
# # opener = urllib2.build_opener(handler)
# # # use the opener to open the web pages
# # response = opener.open('http://www.baidu.com')
# # for item in cookie:
# #     print 'Name = ' + item.name
# #     print 'Value = ' + item.value
# #   
# 
# import cookielib
# import urllib2
# # file to save cookie
# filename = 'cookie.txt'
# # declare a mozillacookiejar class to save cookie
# cookie = cookielib.MozillaCookieJar(filename)
# 
# handler = urllib2.HTTPCookieProcessor(cookie)
# 
# opener = urllib2.build_opener(handler)
# 
# response = opener.open('http://www.baidu.com')
# 
# cookie.save(ignore_discard = True, ignore_expires = True)
# 
# import urllib, urllib2, cookielib
# # create cookie file and build opener
# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 
# # set all the parameters
# postdata = urllib.urlencode({
#              'username' : 'test',
#              'password' : 'test'
#              })
# loginUrl = 'https://uvwxyz.xyz/logging.php?action=login'
# 
# # get the result
# result = opener.open(loginUrl, postdata)
# 
# #save cookie
# cookie.save(ignore_discard = True, ignore_expires = True)
# # use cookie to obtain pages
# getUrl = 'https://uvwxyz.xyz/thread-256167-1-2.html'
# result = opener.open(getUrl)
# print result.read()

# import re
# 
# pattern = re.compile(r'hello')
# result1 = re.match(pattern, 'hello')
# result2 = re.match(pattern, 'helloo CQC')
# result3 = re.match(pattern, 'helo CQC')
# result4 = re.match(pattern, 'hello CQC')
# 
# if result1:
#     print result1.group()
# else:
#     print '1 failed'
#     
# if result2:
#     print result2.group()
# else:
#     print '2 failed'
# 
# if result3:
#     print result3.group()
# else:
#     print '3 failed'
#     
# if result4:
#     print result4.group()
# else:
#     print '4 failed'

# import re
# 
# m = re.match(r'(/w) (/w)(?P<sign>.*)', 'hello world!')
# 
# print 'string', m.string
# print 're', m.re
# print 'pos', m.pos
# print 'endpos', m.endpos
# print 'lastindex', m.lastindex
# print 'lastgroup', m.lastgroup
# print 'group()', m.group()
# print 'group(1, 2)', m.group(1, 2)
# print 'start(2)', m.start(2)
# # print 'end(2)', m.end(2)
# # print 'span(2)', m.span(2)
# # print "expand(rr'\g \g\g')", m.expand(r'\2 \3\1')
# 
# import re
# 
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#  
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
# print "m.group():", m.group()
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
# 
# import re
# 
# pattern = re.compile(r'world')
# 
# match = re.search(pattern, 'hello world!')
# if match:
#     print match.group()
#     
# 
# import re
# pattern = re.compile(r'\d+')
# print re.split(pattern, 'one11111two2222three3four4')
# for m in re.finditer(pattern, 'one1two2three3four4'):
#     print m.group()

# import re
# 
# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print re.sub(pattern, r'\2 \1', s)
# 
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# 
# print re.sub(pattern, func, s)
# 
# import re
# 
# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# 
# print re.subn(pattern, r'\2 \1', s)
# 
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# 
# print re.subn(pattern, func, s)

import re
s = 'i say, hello world!'
pattern = re.compile(r'\w+')
print pattern.findall(s)
