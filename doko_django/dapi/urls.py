
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register(r'topics', topic.TopicViewSet, base_name='topics')
# router.register(r'difficulties', topic.DifficultyViewSet)
# router.register(r'tags', topic.TagViewSet)
# router.register(r'tests', test.TestViewSet, base_name='tests')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^test/', views.get_users),
    url(r'^auth/', views.auth),

]


