
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.utils.translation import gettext as _
from django.contrib.staticfiles.views import serve

from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/',include('grappelli.urls')),
    path("",include("jobs.urls")),
    url(r'accounts/',include('registration.backends.simple.urls')),
    # path('favicon.ico/', serve, {'path': 'favicon.ico'}),
    path('i18n/',include("django.conf.urls.i18n")),
    path('sentry-debug/', trigger_error),
]

admin.site.site_header = _("北京网络科技招聘管理系统")
