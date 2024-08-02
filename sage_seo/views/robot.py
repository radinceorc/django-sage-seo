# views.py
from django.http import HttpResponse
from django.views.generic.base import View

from sage_seo.models import RobotsTxt


class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        try:
            obj = RobotsTxt.objects.first()
            content = obj.content
        except RobotsTxt.DoesNotExist:
            content = "User-agent: *\nDisallow: /"
        return HttpResponse(content, content_type="text/plain")
