from django.contrib import admin
from django.urls import include, path
from drf_info_endpoint.views import info
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from version import __version__

admin.site.site_header = f"ums {__version__}"
admin.site.site_title = "ums"
admin.site.index_title = "ums"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("info/", info),
    path("health/", include("health_check.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
