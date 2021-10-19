from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

TITLE = "Cars API"
DESCRIPTION = "API to add vehicles and raings"
schema_view = get_schema_view(title=TITLE)

urlpatterns = [
    url(r"^", include("api.urls")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^schema/$", schema_view),
    url(r"^docs/", include_docs_urls(title=TITLE, description=DESCRIPTION)),
    path("admin/", admin.site.urls),
     path('schema', get_schema_view(
         title=TITLE,
         description=DESCRIPTION,
         version="1.0.0"
     ), name='openapi-schema'),
]