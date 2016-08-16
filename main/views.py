from django.shortcuts import render, redirect
from main.yours import your_function
from main.models import Query, Mark, CatImage, Version
import random

# Create your views here.

def main(request):
    return render(request, 'main.html', {})

def assess(request):
    if 'text' not in request.POST:
        return redirect('/')

    q = Query.objects.create(text = request.POST['text'], contact = request.POST.get('contact'), version=Version.get_current_version())
    d = {'results': your_function(request.POST['text']), 'src_id': q.id}
    return render(request, 'assess.html', d)

def thank_you(request):
    if 'src_id' not in request.POST:
        return redirect('/')

    res = {}
    for key in request.POST:
        if key.startswith('line_id_'):
            line_no = int(key[8:])
            res[line_no] = res.get(line_no, {})
            res[line_no]['id'] = int(request.POST[key])
        if key.startswith('line_mark_'):
            line_no = int(key[10:])
            res[line_no] = res.get(line_no, {})
            res[line_no]['mark'] = int(request.POST[key])
    q = Query.objects.get(id=int(request.POST['src_id']))
    for key in res:
        if 'id' in res[key] and 'mark' in res[key]:
            q.mark_set.create(line_no = key, line_id = res[key]['id'], line_mark = res[key]['mark'], version=Version.get_current_version())
            
    return render(request, 'thank_you_page.html', {'img': random.choice(CatImage.objects.all())})
