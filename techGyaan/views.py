from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from techGyaan.models import Category,Page
from techGyaan.forms import CategoryForm,PageForm
from techGyaan.webhose_search import run_query

def show_category(request,category_name_slug):
	context_dict={}

	try:
		category=Category.objects.get(slug=category_name_slug)
		pages=Page.objects.filter(category=category).order_by('-views')
		context_dict['pages']=pages
		context_dict['category']=category
	except Category.DoesNotExist:
		context_dict['category']=None
		context_dict['pages']=None
	return render(request,'techGyaan/category.html',context_dict)

def add_category(request):
	form=CategoryForm()

	if request.method=='POST':
		form=CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request,'techGyaan/add_category.html',{'form':form})

def add_page(request,category_name_slug):
	try:
		category=Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category=None

	form=PageForm()
	if request.method=='POST':
		form=PageForm(request.POST)
		if form.is_valid():
			if category:
				page=form.save(commit=False)
				page.category=category
				page.views=0
				page.save()
				return show_category(request,category_name_slug)
		else:
			print(form.errors)
	context_dict={'form':form,'category':category}
	return render(request,'techGyaan/add_page.html',context_dict)
def index(request):
	category_list=Category.objects.order_by('-likes')[:5]
	page_list=Page.objects.order_by('-views')[:5]
	context_dict={'categories':category_list,'pages':page_list}
	return render(request,'techGyaan/index.html',context_dict)

def about(request):
	print(request.user	)
	return render(request,'techGyaan/about.html')

def search(request):
	result_list=[]
	if request.method=='POST':
		query=request.POST['query'].strip()
		if query:
			result_list=run_query(query)				
	return render(request,'techGyaan/search.html',{'result_list':result_list})

def track_url(request):
	page_id=None
	url='/techGyaan/'
	if request.method=='GET':
		if 'page_id' in request.GET:
			page_id=request	.GET['pages_id']

			try:
				page=Page.objects.get(id=page_id)
				page.views=page.views+1
				page.save()
				url=page.url
			except:
				pass
	return redirect(url)