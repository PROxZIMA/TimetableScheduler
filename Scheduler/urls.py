from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from SchedulerApp.forms import UserLoginForm
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('SchedulerApp.urls')),
]

handler404 = 'SchedulerApp.views.error_404'
handler500 = 'SchedulerApp.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
