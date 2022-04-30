# Timetable Scheduler
----------------------------------------------------------------------------------------------------------------------------
### An intelligent timetable generator that generates University timetable using `Genetic Algorithm`.

#### Dependencies:
 1. python 3.6 or above
 2. Django 2.0 or above

#### Run on your local machine by:
* `git clone https://github.com/PROxZIMA/TimetableScheduler.git/`
* `cd TimetableScheduler`
* `python manage.py runserver`
* then go to port `http://127.0.0.1:8000/` to run the local server

#### About the project:
Project uses genetic algorithm to satisfy the constraints related to Timetable scheduling. The program satisfies the following constraints:-

| Hard Constraints                                  | Soft Constraints                                     |
| --------------------------------------------------|:----------------------------------------------------:|
| Unique class timing                               | classes are alloted according to section requirements|
| Course.students <= room.seating capacity          | All courses are according to their department        |
| Two classes dont have same room                   | Even distribution of course in a section per week    |
| Class timing for each teacher is unique           |
| Teachers are allocated to their course accordingly|

## Screenshots

[![1](./assets/img/1.png)](#)
[![2](./assets/img/2.png)](#)
[![3](./assets/img/3.png)](#)
[![4](./assets/img/4.png)](#)
[![5](./assets/img/5.png)](#)
[![6](./assets/img/6.png)](#)
[![7](./assets/img/7.png)](#)
[![8](./assets/img/8.png)](#)

