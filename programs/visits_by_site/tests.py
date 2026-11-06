# Each test: (arguments, expected result). Put multiple arguments in a tuple.
TESTS = [
    (["www.a.com", "a.com"], {"a.com": 2}),
    (["www.wikipedia.org"], {"wikipedia.org": 1}),
    ([], {}),
    (["News.com", "news.com"], {"news.com": 2}),
    (["www.web.dev", "web.dev"], {"web.dev": 2}),
    (["blog.site.io"], {"blog.site.io": 1}),
]
