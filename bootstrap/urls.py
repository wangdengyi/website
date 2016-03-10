from django.conf.urls import url,patterns
from bootstrap import views


#add app_name
app_name = 'bootstrap'

#urlpatterns = [

#    url(r'^$', views.Index, name='index'),
#    url(r'^name/$', views.get_name, name='get_name'),
#    url(r'^list/$', views.list, name='list'),   
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#]

urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#    url(r'^list/$', views.list, name='list'),
#    url(r'^login/$', views.login, name='login'),
#    url(r'^regist/$', views.regist, name='regist'),
#    url(r'index/$', views.index, name='index'),
#    url(r'logout/$', views.logout, name='logout'),
#    url(r'^excel/$', views.uploadExcel, name='excel'),
    url(r'^exceltodb/$', views.importdb, name='exceldb'),
    url(r'^sheettodb/$', views.import_sheet, name='sheetdb'),
    url(r'^sheet_safe/$', views.import_safe, name='safe'),
]

'''
from django.conf.urls import patterns, include, url   
  
urlpatterns = patterns('bootstrap.views',  
    url(r'^list/$', 'list', name='list'),  
)  
'''
