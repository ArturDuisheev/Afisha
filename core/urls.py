from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('my_app.urls')),
    path('reviews/', include('user_actions.urls')),
    path('account/', include('account.urls'))
]
