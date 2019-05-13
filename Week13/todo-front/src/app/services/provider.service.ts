import { Injectable } from '@angular/core';
import {Task, TaskList} from '../models/task';
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
    return this.get(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
  getTasksById(id: number): Promise<TaskList[]> {
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`, {});
  }
}
