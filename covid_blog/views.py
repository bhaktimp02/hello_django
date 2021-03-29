from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Article
from .forms import ImageForm

from django.core.mail import send_mail

def index(request):
	#return HttpResponse("Hello World! ")

	#latest_article_list = Article.objects.all()
	latest_article_list = Article.objects.order_by('-pub_date')

	template = loader.get_template('covid_blog/index.html')
	context = {
		'latest_article_list' : latest_article_list,
	}
	return HttpResponse(template.render(context,request))


def detail(request, article_id):
	
	#detailview = Article.objects.filter(id=article_id).values('details')
	detailview = Article.objects.get(id=article_id)
	#Article.objects.filter(id=1).values('details')

	template = loader.get_template('covid_blog/details.html')
	context = {
		'detailview' : detailview,
	}
	return HttpResponse(template.render(context,request))
	# print("HEERREE", article_id)
	# return HttpResponse("You are looking at article %s" % article_id)


def submit_article_form(request):
	return render(request,'covid_blog/submit_article.html', {})


def success(request):

	print(request.POST)
	try:

		article = Article(title=request.POST['title'], 
				details=request.POST['details'],
				pub_date=request.POST['pubdate'])
		article.save()

		if article.id is not None:
			template = loader.get_template('covid_blog/success.html')
			context = {

				"message" : "Success!",
				"article_id" : article.id
			}
			return HttpResponse(template.render(context, request))
		# else:
		# 	template = loader.get_template('covid_blog/success.html')
		# 	return HttpResponse(template.render({"message":"Error!!!"}, request))
	
	except Exception as error:
		template = loader.get_template('covid_blog/success.html')
		return HttpResponse(template.render({"message":"Error!!!"}, request))


def upload_image(request):

	if request.method == 'POST':
		image_form = ImageForm(request.POST, request.FILES)
		if image_form.is_valid():
			image_form.save()
			context = {
				"form": image_form,
				"img_obj": image_form.instance
			}
		return render(request,'covid_blog/image_upload.html', context)

	else:
		image_form = ImageForm()
		return render(request, 'covid_blog/image_upload.html', {'form': image_form} )


def send_mail_django(request):
	bool_value =  send_mail(
		'Subject here',
		'Here is the message',
		'bhaktimp02@gmail.com',
		['bhaktimp02@gmail.com'],
		fail_silently=False,
		)

	return HttpResponse("Mail success code: ", bool_value)

