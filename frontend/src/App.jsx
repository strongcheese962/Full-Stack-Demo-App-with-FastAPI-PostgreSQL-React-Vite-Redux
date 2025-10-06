import TaskList from './components/TaskList'
import TaskForm from './components/TaskForm'

function App() {
  return (
    <div>
      <h1>My Task Manager</h1>
      <TaskForm />
      <TaskList />
    </div>
  )
}

export default App
