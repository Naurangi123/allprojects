def handle_upload(f):
    with open('ecommerceapp/static/upload/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)