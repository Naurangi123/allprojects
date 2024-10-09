# import os

# def handle_upload(f):
#     upload_dir = 'app/static/upload/'
    
#     if not os.path.exists(upload_dir):
#         os.makedirs(upload_dir)
    
#     file_path = os.path.join(upload_dir,f.name)
    
#     with open(upload_dir, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#             print("File Path",destination)
#     return file_path

def handle_upload(f):
    with open('app/static/upload/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)