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
        uri = request.build_absolute_uri()
        self._cache[uri] = response # put response into cache

        return response
