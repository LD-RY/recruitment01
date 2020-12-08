from django.urls import path
from jobs import views

urlpatterns = [
    path('joblist/', views.joblist, name="joblist"),
    path('job/<int:job_id>/', views.jobdetail, name="jobdetail"),
    path('resume/add/',views.ResumeCreateView.as_view(),name='resume-add'),
    path('resume/<int:pk>',views.ResumeDetailView.as_view(),name='resume-detail'),
    # 首页自动跳转到职位列表
    path('',views.joblist,name='name'),
    path('create_hr_user/',views.create_hr_user,name='create_hr_user')
]

from django.conf import settings
if settings.DEBUG:
    # 有XSS漏洞的视图页面
    urlpatterns += [path('detail_resume/<int:resume_id>',views.detail_resume,name="detail_resume")]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)