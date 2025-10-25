import { useState } from "react";
import type { Task, TaskStatus } from "../types/task";
import { getAuthHeader } from "../helpers/getAuthHeader";

interface TaskItemProps {
  task: Task;
}

export const TaskItem: React.FC<TaskItemProps> = ({ task }) => {
  const [status, setStatus] = useState<TaskStatus>(task.status);

  const updateTaskStatus = async (newStatus: TaskStatus) => {
    try {
      const response = await fetch(`/tasks/${task.id}`, {
        method: "PATCH",
        headers: {
          "Content-type": "application/json",
          ...(getAuthHeader() ?? {}),
        },
        body: JSON.stringify({ status: newStatus }),
      });

      if (!response.ok) throw new Error("Error at update");

      const updateTask = await response.json();
      setStatus(updateTask.status);
    } catch (err) {
      console.error("error", err);
      setStatus(task.status);
    }
  };

  return (
    <li>
      <label>
        <input
          type="checkbox"
          checked={task.status == "completed"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            const newStatus = e.target.checked ? "completed" : "pending";
            setStatus(newStatus);
            updateTaskStatus(newStatus);
          }}
        />
        {task.description}
      </label>
    </li>
  );
};
