"""Tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view



schema_view = get_schema_view(openapi.Info(title='Документация по Турам',
                                            description='веб-сайт по поиску тур-путешествий',
                                            default_version='v1'
                                         ), public=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    # path('api/v1/', include('Packets.urls')),
    # path('api/v1/', include('Reviews.urls')),
    # path('api/v1/', include('Payments.urls')),
    path('api/v1/', include('account.urls')),
]
