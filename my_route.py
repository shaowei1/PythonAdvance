# class Myflask():
#
#     def route(self, rule, **options):
#         def decorator(f):
#             endpoint = options.pop('endpoint', None)
#             # self.add_url_rule(rule, endpoint, f, **options)
#             return f
#
#         return decorator
#
#
# if __name__ == '__main__':
#     app = Myflask()
#
#
#     @app.route('/', methods=['POST', 'POST'], endpoint='?')
#     def index():
#         return 'xxx'
#
#
#     print(index())
#


class MyRoute(object):

    @staticmethod
    def set_args(url=''):
        def set_func(func):
            def wrapper(*args, **kwargs):
                print('Wrapper...')
                func(*args, **kwargs)

            router[url] = wrapper
            return wrapper

        return set_func

    @staticmethod
    @set_args('index.html')
    def index():
        print('index page')

    @staticmethod
    @set_args('login.html')
    def login():
        print('login page')

    def run(self, url):
        print('run is executing')
        func = router[url]
        func()


if __name__ == '__main__':
    router = {}
    a = MyRoute()
    a.run('login.html')
