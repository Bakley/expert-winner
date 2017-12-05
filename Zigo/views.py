# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Sender, Receiver, Parcel
from .forms import NewTopicForm

# @login_required
def home(request):
    parcel = Parcel.objects.all()
    context = {'parcel': parcel}
    return render(request, 'dashboard.html', context)

def user(request):
    return(render, 'user.html')

def about(request):
    board = get_object_or_404(Parcel, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Parcel.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'user.html', {'board': board, 'form': form})


def location(request):
    return render(request, 'location.html')


def contact(request):
    return render(request, 'contact.html')