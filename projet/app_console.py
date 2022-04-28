from container import Container

container = Container()
anna = container.anna()

text = input('What are you looking for? ')
results = anna.search(text)
print(results)