from container import Container

container = Container()
controller = container.controller()

text = input('What are you looking for? ')
results = controller.search(text)
print(results)