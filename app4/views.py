from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from .forms import AnnForm
from .models import Announcement, Rubric


def indexView(request):
    context = {}
    form = AnnForm(request.POST or None)
    friends = Announcement.objects.all()
    rubrics = Rubric.objects.all()
    context['form'] = form
    context['friends'] = friends
    context['rubrics'] = rubrics
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("category")
            print(temp)
    # form = FriendForm()
    # friends = Friend.objects.all()
    return render(request, "app4/index.html", context)


def postAnn(request):
    if request.is_ajax and request.method == "POST":
        form = AnnForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            response_dict = {"instance": ser_instance, "rubric_name": str(form.cleaned_data["rubric"])}
            return JsonResponse(response_dict, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)


def checkTitle(request):
    if request.is_ajax and request.method == "GET":
        nick_name = request.GET.get("nick_name", None)
        if Announcement.objects.filter(nick_name = nick_name).exists():
            return JsonResponse({"valid":False}, status=200)
        else:
            return JsonResponse({"valid":True}, status=200)

    return JsonResponse({}, status=400)


def by_rubric(request, rubric_id):
    friends = Announcement.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'friends': friends, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'app4/by_rubric.html ', context)


class AnnDeleteView(DeleteView):
    template_name = 'app4/delete.html'
    model = Announcement
    success_url = reverse_lazy('index')


class AnnUpdateView(UpdateView):
    template_name = 'app4/update.html'
    success_url = reverse_lazy('index')
    model = Announcement
    fields = ('nick_name', 'description', 'price', 'rubric')
    template_name_suffix = '_update_form'

