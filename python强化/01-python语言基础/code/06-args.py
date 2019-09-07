def args(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


args(*[1, 2, 3])
args(**{"name": "Jim", "age": 99})


