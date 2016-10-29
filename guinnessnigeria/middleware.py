class NoCacheMiddleware(object):
    """Can be put anywhere in middlewares"""

    def process_response(self, request, response):
        response['Cache-Control'] = 'no-cache'
        return response
