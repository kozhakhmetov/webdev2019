import DateTimeFormat = Intl.DateTimeFormat;

export interface Task {
  name: string;
  id: number;
}

export interface TaskList {
  name: string;
  created_at: string;
  due_on: string;
  status: string;
  task_list: string;
}
