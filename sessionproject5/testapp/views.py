from django.shortcuts import render


# Create your views here.
def page_count_view(request):
    print(request.COOKIES)
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    return render(request, 'testapp/pagecount.html', {'count': count})

    """
        print(request.COOKIES)
        count = int(request.COOKIES.get('count', 0))
        count += 1
        request.COOKIES['count'] = count
        response = render(request, 'testapp/pagecount.html', {'count': count})
        response.set_cookie('count', count)
        return response
    """