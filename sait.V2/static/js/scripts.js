function createTask() {
  fetch('/create_task', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      // Данные для создания задачи