from django.shortcuts import render


class Person:
    def __init__(self, name, lastname, hobbies):
        self.name = name
        self.lastname = lastname
        self.hobbies = hobbies

    def hobbies_count(self) -> int:
        return len(self.hobbies)

    def foo(self, a):
        return a


def hello_view(request):
    p = Person('Dmitriy', 'Putin', ['h1', 'h2', 'h3'])

    return render(request, 'todolist/hello.html', context={
        'name': 'Vova',
        'color': 'red',
        'data': [i for i in range(11)],
        'info': p,
    })


def profile_view(request):
    return render(request, 'todolist/profile.html', context={
        'people': [
            {
                'name': 'Vova',
                'info': 'The best developer, 20 years old'
            },
            {
                'name': 'Dima',
                'info': 'The best developer, 20 years old'
            },
            {
                'name': 'Petya',
                'info': 'The best developer, 20 years old'
            },
        ]
    })
