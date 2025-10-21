import { useEffect, useState } from "react";
import type { Task } from "../types/task";
import { TaskList } from "./TaskList";
import { getTasks } from "../api/taskService";

export const Home = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadTasks = async () => {
      try {
        const data = await getTasks();
        setTasks(data);
      } catch (err) {
        setError("Error loading tasks");
      } finally {
        setLoading(false);
      }
    };

    loadTasks();
  }, []);

  if (loading) return <p>Loading tasks...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="container">
      <h1>ToDo List</h1>
      <TaskList tasks={tasks} />
    </div>
  );
};
