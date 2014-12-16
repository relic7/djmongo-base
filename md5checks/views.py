from django.shortcuts import render_to_response


def listcontents(request):
    return render_to_response('md5checks/listcontents.html')


def index(request):

    return render_to_response('md5checks/index.html')