# from django.http import HttpRequest
# from django.http.response import HttpResponse
# from django.utils.deprecation import GetResponseCallable, MiddlewareMixin

# from django.contrib.sessions.middleware import SessionMiddleware

class CustomMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        print("middleware called")
        return response
        
        