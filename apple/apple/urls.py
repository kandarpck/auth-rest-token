"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter
from backend.views import ActivateUser, CreateUserView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', generic.RedirectView.as_view(url='/auth/api/', permanent=False)),
    url(r'^auth/api/$', get_schema_view()),
    url(r'^auth/api/token/obtain/', obtain_jwt_token),
    url(r'^auth/api/token/refresh/', refresh_jwt_token),
    url(r'^auth/api/token/verify/', verify_jwt_token),
    url('^auth/api/register/$', CreateUserView.as_view()),
    url(
        '^auth/api/activate/(?P<token>.+?)/$',
        ActivateUser.as_view(),
        name='activate-user'
    ),

]
