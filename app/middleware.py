from functools import wraps

class MyCacheMiddleware(object):
    def __init__(self):
        self._cache = {}
    def process_request(self, request):
        uri = request.build_absolute_uri()
        if uri in self._cache: # return cached response
            print('Return response to "{}" from cache'.format(uri))
            return self._cache[uri]

        return None # not in cache
    def process_response(self, request, response):
        can_use_cache = not hasattr(request, '_no_cache')
        if not can_use_cache:
            return response

        uri = request.build_absolute_uri()
        self._cache[uri] = response # put response into cache

        return response

def never_cache(view_func):
    @wraps(view_func)
    def wrapped_view_func(request, *args, **kwargs):
        request._no_cache = True
        response = view_func(request, *args, **kwargs)
        response['Cache-Control'] = 'max-age=0'
        return response
    return wrapped_view_func
