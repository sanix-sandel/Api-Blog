from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')), #for login/logout
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),#Registration
]
#There are also endpoints for password reset:
#http://127.0.0.1:8000/api/v1/rest-auth/password/reset
#
#And for password reset confirmed:
#http://127.0.0.1:8000/api/v1/rest-auth/password/reset/confirm