from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.urls import path, re_path, include

from ativnos.profiles.views import UserProfileView

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        'about/',
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        'user/<int:pk>', UserProfileView.as_view(), name="profile"
    ),
    path(
        'users/',
        include("ativnos.users.urls", namespace="users"),
    ),
    path('accounts/', include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path(
        'profiles/',
        include("ativnos.profiles.urls", namespace="profiles"),
    ),
    path(
        'tags/',
        include("ativnos.tags.urls", namespace="tags"),
    ),
    path(
        'tasks/',
        include("ativnos.tasks.urls", namespace="tasks"),
    )
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(
            '400/$',
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        re_path(
            '403/$',
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        re_path(
            '404/$',
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        re_path('500/$', default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [re_path('__debug__', include(debug_toolbar.urls))] + urlpatterns
