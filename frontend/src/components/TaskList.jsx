import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchTasks, deleteTask } from '../features/tasksSlice'

function TaskList() {
  const dispatch = useDispatch()
  const tasks = useSelector((state) => state.tasks.items)
  const status = useSelector((state) => state.tasks.status)
  const error = useSelector((state) => state.tasks.error)

  // fetch tasks when component first loads
  useEffect(() => {
    if (status === 'idle') {
      dispatch(fetchTasks())
    }
  }, [status, dispatch])

  if (status === 'loading') {
    return <p>Loading tasks...</p>
  }

  if (status === 'failed') {
    return <p>Error: {error}</p>
  }

  return (
    <div>
      <h2>Task List</h2>
      {tasks.length === 0 ? (
        <p>No tasks yet.</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong>: {task.description}
              <button onClick={() => dispatch(deleteTask(task.id))}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default TaskList
