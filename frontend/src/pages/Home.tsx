import { TaskList } from "../components/TaskList";

export const Home = () => {
  return (
    <div className="container">
      <h1>ToDo List</h1>
      <TaskList />
    </div>
  );
};
