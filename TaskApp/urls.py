from django.urls import path
from .views import (login_page, login_user,
                    get_tasks, main_page,
                    add_task, delete_task,
                    complete_task,clear_all_tasks
                    )

urlpatterns = [
    path('login_page', login_page, name="login_page"),
    path('main_page', main_page, name="main_page"),
    path('login_user', login_user, name="login_user"),
    path('getTasks', get_tasks, name="get_tasks"),
    path('addTask', add_task, name="add_task"),
    path('deleteTask/<int:pk>', delete_task, name="delete_task"),
    path('completeTask/<int:pk>', complete_task, name="complete_task"),
    path('clearAllTasks', clear_all_tasks, name="clear_all_tasks")

]
