from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404  # HttpResponseRedirect,
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import postform
from .models import post
# from django.views.generic import View, TemplateView


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404("you are not login")
    form = postform(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect(reverse('posts:list'))
    else:
        messages.error(request, "not Created !  try again")
    context = {
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(post, id=id)
    context = {
        'v1': instance.title,
        'instance': instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = post.objects.all().order_by("-timestamp")
    page = request.GET.get('page')
    context = {
        'qqq': queryset,
        'v1': 'List',
    }
    return render(request, "base.html", context)


# class post_list(TemplateView):
#     template_name = 'base.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(** kwargs)
#         context['vi'] = 'List'
#         return context


def post_update(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=id)
    form = postform(
        request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Update")
        return redirect(reverse('posts:list'))
    else:
        messages.error(request, "Not Update !  try again")
    return render(request, "post_form.html", {'form': form})


def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, id=id)
    instance.delete()
    return redirect("posts:list")

    # /posts/id/=>


# {% url "postss:detaill" id=obj.id %}
