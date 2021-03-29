from django.urls import path

from . import views

app_name = "covid_blog"

urlpatterns = [
	path('', views.index, name='index'),

	path('<int:article_id>/', views.detail, name='details'),

	path('submit-article-form/', views.submit_article_form, name='submit_article'),

	path('success/', views.success, name='success'),

	path('image-upload/', views.upload_image, name='upload_image')
]