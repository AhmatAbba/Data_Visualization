from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! This is my first Django app deployed on Vercel, Render, and Supabase.")
