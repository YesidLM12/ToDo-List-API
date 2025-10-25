 export type TaskStatus = "pending" | "in-progress" | "completed";

export interface Task {
  id: string;
  description: string;
  status: TaskStatus;
}
