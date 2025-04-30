from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('base/',v.base, name='base'),
    path('index/',v.index, name='index'),
    path('contact/',v.contact, name='contact'),
    path('student/',v.student, name='student'),
    path('stud/',v.stud, name='studentfrm'),
    path('signup/',v.signUp, name='signUp'),
    path('signin/',v.signIn, name='signin'),
    path('list/',v.stlist, name='list'),
    path('item/<int:pk>/delete/', v.delt, name='delete'),
    path('logout/',v.userlogout, name='logout'),
    path('item/<int:pk>/edit/', v.editt, name='edit'),

]