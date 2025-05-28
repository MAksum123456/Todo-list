from django.urls import path
from .views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", ToggleTaskView.as_view(), name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),

    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags-delete"),

]

app_name = "tasks"
