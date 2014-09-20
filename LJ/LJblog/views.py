# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import *
from forms import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from django.utils import simplejson
from django.shortcuts import render,render_to_response,RequestContext

@api_view(['GET'])
def post_list(request, format=None):
    def convert_to_json(element):
        data = {'titulo':element.title,
        'text':element.text,}
        return data

    if request.method == 'GET':
        data = Post.objects.filter()
        dic = []
        print data
        for element in data:
            print element
            dic.append(convert_to_json(element))
        print dic
        return Response(dic)
    else:
        dic = {'error':'errors'}
        return Response(dic, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def guardar_post(request, format=None):
    if request.method == 'POST':
        
        text = request.DATA['text']
        title = request.DATA['title']
        #is_published = request.DATA['is_published']

        #guardado = Post(text=text,title=title,is_published=is_published)
        guardado = Post(text=text,title=title)
        print guardado

        valor = guardado.save()
        print 'IPPPPP'
        print valor.pk
        diccionario = {'resultado':'satisfactorio'}

        return Response (diccionario)

    else:
        return Response(Constantes.CONST_ERROR_SERVICE, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def guardar_persona(request, format=None):
    if request.method == 'POST':
        
        nombre = request.DATA['nombres']
        apellidos = request.DATA['apellidos']
        descripcion = request.DATA['descripcion']

        guardado = Person(nombre=nombre,apellidos=apellidos,descripcion=descripcion)
        print guardado

        valor = guardado.save()
        print 'IPPPPP'
        print valor.pk
        diccionario = {'resultado':'satisfactorio'}

        return Response (diccionario)

    else:
        return Response(Constantes.CONST_ERROR_SERVICE, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def persona_list(request, format=None):
    def convert_to_json(element):
        data = {'nombre':element.nombre,
        'apellidos':element.apellidos,
        'descripcion':element.descripcion,}
        return data

    if request.method == 'GET':
        data = Person.objects.filter()
        dic = []
        print data
        for element in data:
            print element
            dic.append(convert_to_json(element))
        print dic
        return Response(dic)
    else:
        dic = {'error':'errors'}
        return Response(dic, status=status.HTTP_400_BAD_REQUEST)



class PostListView(ListView):
    model = Post
    context_object_name = "post_list"

    def get_template_names(self):
        return ["LJblog/list.html"]

    def get_queryset(self):
        posts = Post.objects
        if 'all_posts' not in self.request.GET:
            posts = posts.filter(is_published=True)
        return posts

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_template_names(self):
        return ["LJblog/create.html"]

    def get_success_url(self):
        return reverse('list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "The post has been created.")
        return super(PostCreateView, self).form_valid(form)

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_template_names(self):
        return ["LJblog/detail.html"]

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    context_object_name = "post"

    def get_template_names(self):
        return ["LJblog/update.html"]

    def get_success_url(self):
        return reverse('list')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "The post has been updated.")
        return super(PostUpdateView, self).form_valid(form)

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]

class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('list')

    def get(self, *args, **kwargs):
        """ Skip confirmation page """
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "The post has been removed.")
        return redirect(self.get_success_url())

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]


def quiz_guess(request, fact_id):   
    message = {"fact_type": "", "fact_note": ""}
    if request.is_ajax():
        fact = get_object_or_404(Fact, id=fact_id)
        message['fact_type'] = fact.type
        message['fact_note'] = fact.note
    else:
        message = "You're the lying type, I can just tell."
        json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def goServices(request):
    return render_to_response("LJblog/ajax_in_django.html",context_instance=RequestContext(request))


def goapiGoogle(request):
    return render_to_response("LJblog/example_get.html",context_instance=RequestContext(request))

def goPost(request):
    return render_to_response("LJblog/postData.html",context_instance=RequestContext(request))

def goIndex(request):
    return render_to_response("LJblog/index.html",context_instance=RequestContext(request))

def goHistoria(request):
    return render_to_response("LJblog/historia.html",context_instance=RequestContext(request))

def goGallery(request):
    return render_to_response("LJblog/gallery.html",context_instance=RequestContext(request))