from django.urls import path
from django.conf.urls import url
from .views import home, projects, useractions, comments

urlpatterns = [
    #path('', home.index, name='home'),
    path('home', home.index, name='home'),
    path('about', home.about, name='about'),
    path('project', projects.index, name='project_list'),
    path('project/add', projects.create, name='add_project'),
    url(r'^project/(?P<project_id>\d+)/$', projects.view, name='view_project'),
    url(r'^project/(?P<project_id>\d+)/report$', useractions.reportAproject, name='report_project'),
    url(r'^project/(?P<project_id>\d+)/comment$', useractions.comment, name='comment_project'),
    url(r'^project/(?P<project_id>\d+)/(?P<comment_id>\d+)/report$', useractions.reportAcomment, name='report_comment'),
    url(r'^project/(?P<project_id>\d+)/donation$', useractions.makeDonation, name='make-donation'),
    path(r'^project/(?P<project_id>\d+)/comment$', useractions.comment, name='comments_detail'),
    # path('comment/<project_id>/<comment_id>/update', useractions.editComment, name='comment_edit'),
    path('project/comment/update', useractions.editComment, name='comment_edit'),
    # path('<slug:project_id>/', comments.comments_detail, name='comments_detail'),
]
