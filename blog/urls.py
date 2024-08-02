from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    #Home page
    path("", views.index, name="index"),
    # Page to show all TOPICS
    path("topics/", views.topics, name="topics"),
    # Page to show a specific TOPIC with its answers
    path("topics/<int:topic_id>", views.topic, name="topic"),
    # Page to create a new Topic
    path("new_topic", views.new_topic, name="new_topic"),
    # Page to add a new Answer
    path("new_answer/<int:topic_id>/", views.new_answer, name="new_answer"),
    # Page for edit an answer
    path("edit_answer/<int:answer_id>/", views.edit_answer,name="edit_answer"),
    # Page for edit a topic
    path("edit_topic/<int:topic_id>/", views.edit_topic, name="edit_topic"),
    # Page for all user topics
    path("my_topics/", views.my_topics, name="my_topics"),
    # Delete answer
    path("delete_answer/<int:answer_id>/", views.delete_answer, name="delete_answer"),
    #Delete Topic
    path("delete_topic/<int:topic_id>/", views.delete_topic, name="delete_topic"),
]