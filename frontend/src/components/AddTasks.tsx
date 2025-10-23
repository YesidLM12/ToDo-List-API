import { useState } from "react";
import { createTask } from "../api/taskService";
import type { Task } from "../types/task";

interface AddTaskProps {
  onTaskAdded: () => void;
}

export const AddTask = ({ onTaskAdded }: AddTaskProps) => {
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!description.trim()) return;

    try {
      setLoading(true);
      setError(null);

      const newTask: Omit<Task, "id"> = {
        description,
        status: "pending",
      };

      await createTask(newTask);
      setDescription("");
      onTaskAdded();
    } catch (err) {
      setError("Erro at add taks. Try again");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="New Task..."
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button type="submit" disabled={loading}>
        {" "}
        {loading ? "Agregando.." : "Agregar"}
      </button>

      {error && <p>{error}</p>}
    </form>
  );
};
