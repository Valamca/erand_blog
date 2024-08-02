from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

#Importing models and FORMS
from .models import Topic, Answer
from .forms import TopicForm, AnswerForm

# Validations

def check_topic_owner(request, data):
    """
    Make sure if the Topic belongs to the current user
    """
    if data.owner != request.user:
        raise Http404

# Create your views here.
def index(request):
    """
    View for a home page.
    """
    return render(request=request, template_name="blog/index.xhtml")

@login_required
def topics(request):
    """Show all the topics in database"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics":topics}
    return render(request=request, template_name="blog/topics.xhtml",
                context=context)

@login_required
def topic(request, topic_id):
    """Show an individual Topic an its answers"""
    topic = Topic.objects.get(id=topic_id)
    answers = topic.answer_set.order_by("date_added")
    context = {"topic":topic, "answers":answers}

    return render(request=request, template_name="blog/topic.xhtml",
                context=context)

@login_required
def new_topic(request):
    """Creating a new Topic"""

    # Checking if we have a POST or no Request
    if request.method != "POST":
        # If not, we create a empty form
        form = TopicForm()
    else:
        # If we have a POST we create a TopicFORM to process
        form = TopicForm(data=request.POST)
        # validating our form
        if form.is_valid():
            # If valid we save the information
            new_topic = form.save(commit=False)
            # Setting the user
            new_topic.post_user = request.user 
            # Seetign owner
            new_topic.owner = request.user

            # Saving results
            new_topic.save()
            # now we redirect to the TOPICS Page
            return redirect("blog:topics")
        
    # Once we process the data we display the results
    context = {"form":form}
    return render(request=request, template_name="blog/new_topic.xhtml",
                context=context)

@login_required
def new_answer(request, topic_id):
    """Adding a new Answer for a particula Topic."""

    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # IF no data is submitted; Create a blank form
        form = AnswerForm()
    else:
        # If POST; Process data.
        form = AnswerForm(data=request.POST)
        # Validating form
        if form.is_valid():
            #Create a new Answer without saving to database yet
            new_answer = form.save(commit=False)
            # Setting the owner
            new_answer.owner = request.user
            # Setting the user 
            new_answer.answer_user = request.user
            # Setting the Topic for this answer
            new_answer.topic = topic
            # Saving Results
            new_answer.save()
            # Display results
            return redirect("blog:topic", topic_id=topic_id)
    # Creating the display page
    context = {"topic":topic, "form":form}
    return render(request=request, template_name="blog/new_answer.xhtml",
        context=context)

@login_required
def edit_answer(request, answer_id):
    """Edit a blog's answer."""

    answer= Answer.objects.get(id=answer_id)
    topic = answer.topic

    check_topic_owner(request=request, data=answer)
    

    if request.method != "POST":
        # If request is not a POST; Pre fill with current entry
        form = AnswerForm(instance=answer)
    else:
        # If POST; Process data.
        ## Create a Form from the current answer and with the POST method
        form = AnswerForm(instance=answer, data=request.POST)

        if form.is_valid():
            form.save() 
            # After we saved the Answer we redirect to the topic page
            return redirect("blog:topic", topic_id = topic.id)
    context = {"answer":answer, "topic":topic, "form":form}
    return render(request=request, template_name="blog/edit_answer.xhtml",
                context=context)

@login_required
def edit_topic(request, topic_id):
    """Edit a Topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:topics")
    context = {"topic":topic, "form":form}
    return render(request=request, template_name="blog/edit_topic.xhtml",
                context=context)

@login_required
def my_topics(request):
    """ Show all user active Topics"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics":topics}
    return render(request=request, template_name="blog/my_topics.xhtml",
                context=context)

@login_required
def delete_answer(request, answer_id):
    """Deletes the current answer"""
    answer = Answer.objects.get(id=answer_id)
    topic = answer.topic

    check_topic_owner(request=request, data=answer)

    if request.method != 'POST':
        form = AnswerForm(instance=answer)
    else:
        answer.delete()
        return redirect("blog:topic", topic_id = topic.id)
    context = {"answer":answer, "topic":topic, "form":form}
    return render(request=request, template_name="blog/edit_answer.xhtml",
                context=context) 

def delete_topic(request, topic_id):
    """Deletes a Topic"""
    topic = Topic.objects.get(id=topic_id)
    
    check_topic_owner(request=request, data=topic)

    if request.method != "POST":
        form = TopicForm(instance=topic)
    else:
        topic.delete()
        return redirect("blog:my_topics")
    
    context = {"topic":topic, "form":form}
    return render(request=request, template_name="blog/my_topics.xhtml",
                  context=context)