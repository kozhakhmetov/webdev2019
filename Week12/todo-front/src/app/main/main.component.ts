import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {TaskList, Task} from '../models/task';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public loading = false;
  public listOfTaskList: Task[] = [];
  public tasks: TaskList[] = [];
  public name: any = '';
  public logged = false;
  public login = '';
  public password = '';
  public tok = '';


  constructor(private provider: ProviderService) { }

  ngOnInit() {

    const token = localStorage.getItem('token');
    this.tok = token;
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.provider.getAllTaskLists().then(res => {
        this.listOfTaskList = res;
        setTimeout(() => {
          this.loading = true;
        }, 2000);
      });
    }
  }
  getTasks(task: Task) {
    this.provider.getTasksById(task.id).then(res => {
      this.tasks = res;
    });
  }

  deleteTask(c: Task) {
    this.provider.deleteTask(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getAllTaskLists().then(r => {
        this.listOfTaskList = r;
      });
    });
  }

  updateTask(c: Task) {
    this.provider.updateTask(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  createTask() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.listOfTaskList.push(res);
        this.name = '';
      });
    }
  }
  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);

        this.logged = true;

        this.provider.getAllTaskLists().then(r => {
          this.listOfTaskList = r;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });

      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged = false;
    });
  }

}
