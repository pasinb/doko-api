
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseVs)
router.register(r'sections', views.SectionVs)
router.register(r'questions', views.QuestionVs)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^test/', views.get_users),
    url(r'^auth/', views.auth),

]


