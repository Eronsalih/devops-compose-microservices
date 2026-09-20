import { useEffect, useState } from "react";
import "./App.css";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function App() {
  const [users, setUsers] = useState([]);
  const [tasks, setTasks] = useState([]);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const [taskTitle, setTaskTitle] = useState("");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadData = async () => {
    try {
      setLoading(true);
      setError("");

      const [usersResponse, tasksResponse] = await Promise.all([
        fetch(`${API_URL}/api/users`),
        fetch(`${API_URL}/api/tasks`),
      ]);

      if (!usersResponse.ok || !tasksResponse.ok) {
        throw new Error("Could not load backend data");
      }

      const usersData = await usersResponse.json();
      const tasksData = await tasksResponse.json();

      setUsers(usersData);
      setTasks(tasksData);
    } catch (err) {
      setError("Backend connection failed");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const addUser = async (event) => {
    event.preventDefault();

    if (!name.trim() || !email.trim()) {
      return;
    }

    try {
      const response = await fetch(`${API_URL}/api/users`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          email,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to create user");
      }

      setName("");
      setEmail("");

      await loadData();
    } catch (err) {
      setError("Could not create user");
      console.error(err);
    }
  };

  const addTask = async (event) => {
    event.preventDefault();

    if (!taskTitle.trim()) {
      return;
    }

    try {
      const response = await fetch(`${API_URL}/api/tasks`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: taskTitle,
          completed: false,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to create task");
      }

      setTaskTitle("");

      await loadData();
    } catch (err) {
      setError("Could not create task");
      console.error(err);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <p className="eyebrow">Docker Compose Lab</p>
          <h1>DevOps Microservices Dashboard</h1>
          <p className="subtitle">
            React → API Gateway → FastAPI Microservices
          </p>
        </div>

        <button onClick={loadData}>Refresh</button>
      </header>

      <section className="stats">
        <div className="stat-card">
          <span>Users</span>
          <strong>{users.length}</strong>
        </div>

        <div className="stat-card">
          <span>Tasks</span>
          <strong>{tasks.length}</strong>
        </div>

        <div className="stat-card">
          <span>Services</span>
          <strong>4</strong>
        </div>
      </section>

      {error && <div className="error">{error}</div>}

      {loading ? (
        <div className="loading">Loading services...</div>
      ) : (
        <main className="grid">
          <section className="panel">
            <h2>Users Service</h2>

            <form onSubmit={addUser}>
              <input
                type="text"
                placeholder="Name"
                value={name}
                onChange={(event) => setName(event.target.value)}
              />

              <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />

              <button type="submit">Add User</button>
            </form>

            <div className="list">
              {users.map((user) => (
                <div className="item" key={user.id}>
                  <strong>{user.name}</strong>
                  <span>{user.email}</span>
                </div>
              ))}
            </div>
          </section>

          <section className="panel">
            <h2>Tasks Service</h2>

            <form onSubmit={addTask}>
              <input
                type="text"
                placeholder="New task"
                value={taskTitle}
                onChange={(event) => setTaskTitle(event.target.value)}
              />

              <button type="submit">Add Task</button>
            </form>

            <div className="list">
              {tasks.map((task) => (
                <div className="item task" key={task.id}>
                  <div>
                    <strong>{task.title}</strong>
                    <span>
                      {task.completed ? "Completed" : "Pending"}
                    </span>
                  </div>

                  <span className={`status ${task.completed ? "done" : ""}`}>
                    {task.completed ? "Done" : "Pending"}
                  </span>
                </div>
              ))}
            </div>
          </section>
        </main>
      )}
    </div>
  );
}

export default App;
