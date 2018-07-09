"""mpesapp URL Configuration

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
from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

"""from spotlight.cross_validation import random_train_test_split
from spotlight.datasets.movielens import get_movielens_dataset
from spotlight.evaluation import rmse_score
from spotlight.factorization.explicit import ExplicitFactorizationModel

dataset = get_movielens_dataset(variant='100K')

train, test = random_train_test_split(dataset)

model = ExplicitFactorizationModel(n_iter=1)
model.fit(train)

rmse = rmse_score(model, test)

print(dataset)"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', include('prediction.urls')),
    path('', RedirectView.as_view(url='/prediction/')),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)