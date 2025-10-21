import type { Task } from "../types/task";

const API_URL = import.meta.env.VITE_API_URL;

const getAuthHeader = (): Record<string, string> | undefined => {
  const token = localStorage.getItem("token");
  return token ? { Authorization: `Bearer ${token}` } : undefined;
};

export const getTasks = async (): Promise<Task[]> => {
  const res = await fetch(`${API_URL}/task`);
  if (!res.ok) throw new Error("Error fetching tasks");
  return res.json();
};

export const createTask = async (task: Omit<Task, "id">): Promise<Task> => {
  const res = await fetch(`${API_URL}/task`, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...(getAuthHeader() ?? {}) },
    body: JSON.stringify(task),
  });

  if (!res.ok) throw new Error("Error creating task");
  return res.json();
};

export const updateTask = async (
  id: string,
  data: Partial<Task>
): Promise<Task> => {
  const res = await fetch(`${API_URL}/task/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json", ...(getAuthHeader() ?? {}) },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Error updating task");
  return res.json();
};

export const deleteTask = async (id: string): Promise<void> => {
  const res = await fetch(`${API_URL}/task/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Error deleting task");
};
