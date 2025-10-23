import type { Task } from "../types/task";
import { TaskItem } from "./TaskItem";
import { getTasks } from "../api/taskService";
import { AddTask } from "./AddTasks";
import { useEffect, useState } from "react";

export const TaskList = () => {
  const [tasks, setTasks] = useState<Task[]>([]);

  const fetchTasks = async () => {
    try {
      const data = await getTasks();
      setTasks(data);
    } catch (err) {
      console.error("Error fetching tasks: ", err);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h2>My Tasks</h2>

      <AddTask onTaskAdded={fetchTasks} />

      <ul>
        {tasks.map((task) => (
          <TaskItem key={task.id} task={task} />
        ))}
      </ul>
    </div>
  );
};
