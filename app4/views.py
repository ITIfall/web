from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from .forms import FriendForm
from .models import Friend, Rubric


def indexView(request):
    context = {}
    form = FriendForm(request.POST or None)
    friends = Friend.objects.all()
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


def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        #print(form.fields["rubric"].choices)
        if form.is_valid():
          #  form.cleaned_data["rubric"]
            print(form.cleaned_data["rubric"])
            instance = form.save()
            print(type(instance))
            #rubric_name = instance["rubric"].name
            # rubric_name = Rubric.objects.get(pk=instance["rubric"])
            # print(rubric_name)
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            response_dict = {"instance": ser_instance, "rubric_name": str(form.cleaned_data["rubric"])}
            print (response_dict)
            return JsonResponse(response_dict, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def checkNickName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if Friend.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status=200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status=200)

    return JsonResponse({}, status=400)


def by_rubric(request, rubric_id):
    friends = Friend.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'friends': friends, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'app4/by_rubric.html ', context)


class FriendDeleteView(DeleteView):
    template_name = 'app4/delete.html'
    model = Friend
    success_url = reverse_lazy('index')


class FriendUpdateView(UpdateView):
    template_name = 'app4/update.html'
    success_url = reverse_lazy('index')
    model = Friend
    fields = ('nick_name', 'description', 'price', 'rubric')
    template_name_suffix = '_update_form'

    # employee = get_object_or_404(pk=kwargs.get('employee_id')
"""
def picFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
"""