## Домашнее задание к уроку 19

В этом задании мы учимся работать с авторизацией пользователей и контролем доступа.

Для реализации проекта к базовой версии из условия задания были добавлены модель и схема сериализации пользователя, вьюшки авторизации и добавления нового пользователя.

___
Для проверки проекта можно создать своих пользователей через метод POST или воспользоваться следующими учетными данными
### Admin:

{
	"username": "olga",
	"password": "P@ssw0rd"
}

**refresh_token:** eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJwYXNzd29yZCI6Ilx1MDAxYlx1MDAwNlx1MDAxOVx1YzE2OVpcdTAwMWV0Slx1MDUwMEJcdTAwMDNbXHUwMDAzalx1MDAxOVxyQVx1MDAwZlx1MDAwMVx1MDAxMyIsImlkIjozLCJ1c2VybmFtZSI6Im9sZ2EiLCJleHAiOjE2NjUwNTM3MDMuMzU2MTQ3fQ.J0WzV9tZCbFf9MJjQlaqCbVBExQgHc0ffl4pwuG06Ug

### User:

{
	"username": "julia",
	"password": "hard_4"
}

**refresh_token:** eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imp1bGlhIiwiaWQiOjQsInJvbGUiOiJ1c2VyIiwicGFzc3dvcmQiOiI3Zlx1MDA3Zlx1MDA3ZjRcdTAwMDVcdTAwMThcdTAwMTVcYi1cdTAwMGIgc21sXHUwMDE1LVx1MDAxYSBVXHUwNzdjIiwiZXhwIjoxNjY1MDU0MjEwLjkwODYwOH0.yoryIS9sVX8qf-mCV-yvbnawAeHdB7uzDc0IwC_2k0I