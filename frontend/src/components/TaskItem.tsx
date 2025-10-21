import type { Task } from "../types/task";

interface TaskItemProps {
  task: Task;
}

export const TaskItem: React.FC<TaskItemProps> = ({ task }) => {
  return (
    <li>
      <strong>{task.description}</strong> - {task.status}
    </li>
  );
};
