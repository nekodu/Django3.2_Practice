""" 
To render html pages
"""

from django.http import HttpResponse

HTML_STRING = """
<h1> Hello World</h1>
"""

def home_view():
    """
    Take in a request(Django does that)
    Return html as a response (we do that)
    """
    return HttpResponse(HTML_STRING)
