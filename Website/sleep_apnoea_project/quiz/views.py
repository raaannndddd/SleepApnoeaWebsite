from django.shortcuts import render, redirect
import random
import time
from datetime import datetime

def landing(request):
    return render(request, 'quiz/landing.html')

def quiz_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'quiz':
            # process form...
            score = random.randint(30, 95)
            request.session['score'] = score

        elif form_type == 'audio':
            # process audio...
            score = random.randint(30, 95)
            request.session['score'] = score

        # track how many times user has taken quiz
        count = request.session.get('loading_count', 0)
        request.session['loading_count'] = count + 1

        return redirect('loading')

    return render(request, 'quiz/quiz.html')

def result_view(request):
    score = request.session.get('score', None)

    if score is None:
        return redirect('quiz')  

    return render(request, 'quiz/result.html', {'percent': score})

def about_page(request):
    return render(request, 'quiz/about.html')

def contact_page(request):
    return render(request, 'quiz/contact.html')

def loading(request):
    delay = random.randint(3, 7)
    return render(request, 'quiz/loading.html', {'delay': delay})

def choose_input_method(request):
    if request.method == 'POST':
        method = request.POST.get('method')
        if method == 'quiz':
            return redirect('quiz')
        elif method == 'audio':
            return redirect('upload')
    return render(request, 'quiz/choice.html')


def upload_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            # Optionally save/process the audio file here

            # Dummy prediction result (replace with actual model logic later)
            score = random.randint(30, 95)
            request.session['score'] = score

            # Track how many times user has uploaded audio
            count = request.session.get('loading_count', 0)
            request.session['loading_count'] = count + 1

            return redirect('loading')  # Redirect to loading page first

    return render(request, 'quiz/upload.html', {'now': datetime.now()})