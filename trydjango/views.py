""" 
To render html pages
"""
import random
from django.http import HttpResponse



def home_view(request):
    """
    Take in a request(Django does that)
    Return html as a response (we do that)
    """
    number = random.randint(1,99)
    HTML_STRING = f"""
    <h1> Hello User {number}!</h1>
    """
    return HttpResponse(HTML_STRING)
