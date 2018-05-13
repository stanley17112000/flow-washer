from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
import time
import random
import subprocess
import re
from threading import Thread
# Create your views here.

id_cnt = 1;
task_list = {}
todo_list = [ '/home/stanley/udnserver/phantomjs', '/home/stanley/udnserver/test.js' , '' ]

def index( request ):
    view_data = {'my_ip':'127.0.0.1'}
    return render(request, 'index.html', view_data )

def checkPassword( request ):
    pwd = request.GET.get('password', '')
    if  pwd == 'nopassword':
        request.session.set_expiry(300)
        request.session['secret'] = 'asjldkfjlsdfjinksdn2131hjlkj'
        return HttpResponse( "Yes" );
    else:
        return HttpResponse( "No" );

def deleteTask(request):
    global task_list
    id = request.GET.get('id', '')
    del task_list[int(id)]
    return HttpResponse( 'Success' )

def addTask(request):
    global id_cnt
    global task_list
    url = request.GET.get('url', '')
    count = request.GET.get( 'count' , '' );
    if len( url ) > 0 and re.search( '[1-9]+[0-9]*', count ): 
        task_list[id_cnt] =  { 'id':id_cnt, 'url':url, 'now':0, 'target':int(count)} ;
        thread = Thread( target = background_process, args = (id_cnt,) )
        thread.start()
        id_cnt += 1;
        return HttpResponse( 'Success' )
    else:
        return HttpResponse( 'Failed' )

def console( request ):
    view_data = {'my_ip':'127.0.0.1'}
    
    if 'secret' in request.session and request.session['secret'] == 'asjldkfjlsdfjinksdn2131hjlkj':
        toShow = list( task_list.values() )
        return render(request, 'console.html', {'task_list':toShow} )
    else:
        return render( request, 'index.html', view_data )
def background_process( id ):
    global todo_list 
    run = True
    while run:
        run = False
        if id in task_list:
            task = task_list[id]
            if task['now'] < task['target']:
                task['now'] += 1
                new_task_list = list( todo_list )
                new_task_list[2] = task['url']
                subprocess.Popen( new_task_list )
                print ( {'task {} finished {}'.format( id, task['now'] )} )
                run = True
        sleepTime = random.randrange( 5, 100 )
        print( 'wait {} sec'.format( sleepTime ) )
        time.sleep( sleepTime )
        



