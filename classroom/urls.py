from django.urls import path
from .views import HomeView, ThankYou, ContactFormView, \
    TeacherCreateView, TeacherListView, \
    TeacherDetailView, TeacherUpdateView, \
    TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thankyou/', ThankYou.as_view(), name='thankyou'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('detail_teacher/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view())
]
