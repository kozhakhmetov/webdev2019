import DateTimeFormat = Intl.DateTimeFormat;

export interface Task {
  name: string;
  id: number;
}

export interface TaskList {
  name: string;
  created_at: DateTimeFormat;
  due_on: DateTimeFormat;
  status: string;
  task_list: string;
  read_only: false;
}

export interface IAuthResponse {
  token: string;
}
