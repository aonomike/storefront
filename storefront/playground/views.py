from django.shortcuts import render
# Create your views here.


def say_hello(request):
    """Says Hello

    Args:
        request (HTTPReques): http request

    Returns:
        HTTPResponse: HTTP Response
    """
    return render(request, 'hello.html', {'name':'Xi'})