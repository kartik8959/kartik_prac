from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('institute/',include('institutes.urls')),
    # path('account/',include('django.contrib.auth.urls'))

]
