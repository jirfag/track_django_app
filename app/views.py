from django.http import HttpResponse
from datetime import datetime
from .middleware import never_cache

@never_cache
def get_current_time(request):
    now = datetime.now()
    return HttpResponse('<html><body>It is now {}</body></html>'.format(now))
