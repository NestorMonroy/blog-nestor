"""nblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from core.views import home_page, IndexView
from django.views.generic import RedirectView, TemplateView
from allauth.urls import urlpatterns
from dj_rest_auth.registration.urls import RegisterView
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView
from .yasg import urlpatterns as doc_urls

# import frontend.urls
# import accounts.urls
# import post.api.urls


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="core/index.html"), name='home'),

    url(r'^signup/$', TemplateView.as_view(template_name="core/signup.html"),
        name='signup'),

    url(r'^email-verification/$',
        TemplateView.as_view(template_name="core/email_verification.html"),
        name='email-verification'),

    url(r'^login/$', TemplateView.as_view(template_name="core/login.html"),
        name='login'),

    url(r'^logout/$', TemplateView.as_view(template_name="core/logout.html"),
        name='logout'),

    url(r'^password-reset/$',
        TemplateView.as_view(template_name="core/password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="core/password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="core/user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="core/password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="core/password_reset_confirm.html"),
        name='password_reset_confirm'),

    # url(r'^rest-auth/', include('dj_rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/',
                                                     permanent=True), name='profile-redirect'),

    url(r'^$', home_page, name='home'),
    path('api/post/', include('post.api.urls')),
    path('api/accounts/', include('accounts.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
