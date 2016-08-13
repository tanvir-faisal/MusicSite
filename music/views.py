#from django.http import Http404
from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from .models import Album, Song
#from django.template import loader

# Create your views here.
'''
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'         # cause, detail has "/music/712/"  format(for an individual album)
        html += '<a href= "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')    #when template loader is used
    context = {
        'all_albums': all_albums,
    }
    #return HttpResponse(template.render(context, request))     #when template loader is used
    return render(request, 'music/index.html', context)           #HttpResponse is here in render

'''
def detail(request, album_id):
    #return HttpResponse('<h2> Details of the album id: '+ str(album_id) + '</h2>')
    try:
        album= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('There is no album!')

    return render(request, 'music/detail.html', { 'album' : album})\
'''


def detail(request, album_id):
    #return HttpResponse('<h2> Details of the album id: '+ str(album_id) + '</h2>')
    album=get_object_or_404(Album, pk=album_id)                             #shortcut for try-except block
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError, SongDoesNotExist ):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select any song!!",
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
