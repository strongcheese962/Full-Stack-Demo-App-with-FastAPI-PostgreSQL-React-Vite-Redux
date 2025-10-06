import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

// 🔹 1. Async thunks (talk to FastAPI backend)
export const fetchTasks = createAsyncThunk('tasks/fetchTasks', async () => {
  const response = await fetch('http://127.0.0.1:8000/tasks')
  if (!response.ok) {
    throw new Error('Failed to fetch tasks')
  }
  return await response.json()
})


export const addTask = createAsyncThunk('tasks/addTask', async (newTask) => {
  const response = await fetch('http://127.0.0.1:8000/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newTask),
  })
  return await response.json()
})

export const deleteTask = createAsyncThunk('tasks/deleteTask', async (taskId) => {
  await fetch(`http://127.0.0.1:8000/tasks/${taskId}`, { method: 'DELETE' })
  return taskId
})

// 🔹 2. Slice definition
const tasksSlice = createSlice({
  name: 'tasks',
  initialState: {
    items: [],
    status: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    // fetchTasks
    builder.addCase(fetchTasks.pending, (state) => {
      state.status = 'loading'
    })
    builder.addCase(fetchTasks.fulfilled, (state, action) => {
      state.status = 'succeeded'
      state.items = action.payload
    })
    builder.addCase(fetchTasks.rejected, (state, action) => {
      state.status = 'failed'
      state.error = action.error.message
    })

    // addTask
    builder.addCase(addTask.fulfilled, (state, action) => {
      state.items.push(action.payload)
    })

    // deleteTask
    builder.addCase(deleteTask.fulfilled, (state, action) => {
      state.items = state.items.filter(task => task.id !== action.payload)
    })
  },
})

export default tasksSlice.reducer
