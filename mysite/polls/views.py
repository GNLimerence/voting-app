from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.forms import formset_factory
# Create your views here.
def index (request):
    h = Question.objects.all()
    context = {"Ques": h}
    return render(request, "polls/index.html", context)
def detailview (request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "polls/detail_question.html", {"qs": q})
def vote (request, question_id):
    q = Question.objects.get (pk = question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get (pk = dulieu)
    except:
        HttpResponse("loi khong co choice")
    c.vote = c.vote  + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})
def result(request, question_id):
    res = Question.objects.get(pk = question_id)
    context = {"ques":res}
    return render(request, "polls/result2.html", context)


from django.forms import formset_factory

# ...

from django.shortcuts import render, redirect
from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice


def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=str(i)) for i in
                        range(4)]  # Change 3 to the desired number of choices

        if question_form.is_valid() and all([form.is_valid() for form in choice_forms]):
            question = question_form.save()

            for form in choice_forms:
                choice_text = form.cleaned_data['choice_text']
                if choice_text:
                    choice = Choice(question=question, choice_text=choice_text, vote=0)
                    choice.save()

            return redirect('polls:index')
    else:
        question_form = QuestionForm()
        choice_forms = [ChoiceForm(prefix=str(i)) for i in range(4)]  # Change 3 to the desired number of choices

    return render(request, 'polls/add_question.html', {'question_form': question_form, 'choice_forms': choice_forms})











