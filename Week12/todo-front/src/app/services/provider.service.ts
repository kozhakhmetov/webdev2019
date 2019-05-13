import { Injectable } from '@angular/core';
import {IAuthResponse, Task, TaskList} from '../models/task';
import {MainService} from './main.service';

import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getAllTaskLists(): Promise<Task[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }

  getTaskListById(id: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/task_lists/${id}`, {});
  }

  getTasksById(id: number): Promise<TaskList[]> {
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`, {});
  }

  createTaskList(name: any): Promise<Task> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: name
    });
  }

  updateTask(task: Task) {
    return this.put(`http://localhost:8000/api/task_lists/${task.id}/`, {
      name: task.name
    });
  }

  deleteTask(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }

  auth(login: any, password: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {
    });
  }
}
