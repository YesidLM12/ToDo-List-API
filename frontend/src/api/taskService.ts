import { getAuthHeader } from "../helpers/getAuthHeader";
import type { Task } from "../types/task";

const API_URL = import.meta.env.VITE_API_URL;

export const getTasks = async (): Promise<Task[]> => {
  try {
    const response = await fetch(`${API_URL}/task/`, {
      headers: {
        "Content-type": "application/json",
        ...(getAuthHeader() ?? {}),
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(
        "Fetch failed:",
        response.status,
        response.statusText,
        errorText
      );
      throw new Error(`Error fetching tasks: ${response.status}`);
    }

    return await response.json();
  } catch (err) {
    console.error(err);
    throw err;
  }
};

export const createTask = async (task: Omit<Task, "id">): Promise<Task> => {
  try {
    const res = await fetch(`${API_URL}/task`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(getAuthHeader() ?? {}),
      },
      body: JSON.stringify(task),
    });

    if (!res.ok) throw new Error("Error creating task");

    return await res.json();
  } catch (err) {
    console.error(err);
    throw err;
  }
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
