from django.http import HttpResponse


def word_view(request, word):
    return HttpResponse(word)