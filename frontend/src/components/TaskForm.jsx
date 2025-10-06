import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { addTask } from '../features/tasksSlice'

function TaskForm() {
  const dispatch = useDispatch()
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (title.trim() === '') return

    dispatch(addTask({ title, description }))
    setTitle('')
    setDescription('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Task</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <br />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <br />
      <button type="submit">Add Task</button>
    </form>
  )
}

export default TaskForm
