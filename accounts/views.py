from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def register(request):
    """

    :param request:
    :return:
    """

    if request.method == "GET":
        form = CustomUserCreationForm()
    elif request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # make changes to use before saving
            user.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)
