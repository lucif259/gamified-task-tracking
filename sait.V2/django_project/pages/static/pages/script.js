<script src="{% static 'pages/script.js' %}"></script>

document.addEventListener('DOMContentLoaded', function() {
  // Обработка нажатия на кнопку редактирования задачи
  document.querySelectorAll('.edit-task-button').forEach(function(button) {
    button.addEventListener('click', function() {
      var taskId = button.dataset.taskId;
      fetch('/edit_task/' + taskId + '/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        // Отображение формы редактирования задачи на странице
        var taskForm = document.getElementById('task-form');
        taskForm.querySelector('input[name="task_id"]').value = data.task_id;
        taskForm.querySelector('input[name="title"]').value = data.title;
        taskForm.querySelector('textarea[name="description"]').value = data.description;
        taskForm.style.display = 'block';
      })
      .catch(error => {
        console.error(error);
      });
    });
  });

  // Обработка отправки формы редактирования задачи
  document.getElementById('task-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var taskId = event.target.querySelector('input[name="task_id"]').value;
    var title = event.target.querySelector('input[name="title"]').value;
    var description = event.target.querySelector('textarea[name="description"]').value;
    fetch('/edit_task/' + taskId + '/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title,
        description: description
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        // Обновление задачи на странице после успешного редактирования
        var taskRow = document.getElementById('task-' + taskId);
        taskRow.querySelector('.task-title').textContent = title;
        taskRow.querySelector('.task-description').textContent = description;
      }
    })
    .catch(error => {
      console.error(error);
    });
  });
});

document.addEventListener('DOMContentLoaded', function() {
  // Обработка нажатия на кнопку просмотра списка задач
  document.getElementById('view-tasks-button').addEventListener('click', function() {
    // Отправка AJAX-запроса на сервер для получения списка задач
    fetch('/tasks/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      // Отображение списка задач на странице
      var taskList = document.getElementById('task-list');
      taskList.innerHTML = '';
      data.forEach(function(task) {
        var taskItem = document.createElement('li');
        taskItem.innerHTML = '<span class="task-title">' + task.title + '</span> <span class="task-description">' + task.description + '</span>';
        taskList.appendChild(taskItem);
      });
    })
    .catch(error => {
      console.error(error);
    });
  });
});

