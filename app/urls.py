from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from app.views import (
    TaskListViews,
    TaskDetailViews,
    TaskCreationViews,
    TaskUpdateViews,
    TaskDeleteViews,
    complete_undo,
)

urlpatterns = [
    path("", TaskListViews.as_view(), name="task-list"),
    path("creation/", TaskCreationViews.as_view(), name="task-creation"),
    path("<int:pk>", TaskDetailViews.as_view(), name="task-detail"),
    path("<int:pk>/update", TaskUpdateViews.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteViews.as_view(), name="task-delete"),
    path("<int:pk>/complete_undo", complete_undo, name="task-complete-undo")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "todo_list"
