from controllers import AppController
from services import LcsService

service = LcsService()
controller = AppController(service)

text1 = input('Please input text 1: ')
text2 = input('How about text 2: ')
result = controller.compute(text1, text2)
print('Length of the longest common sequence is: ' + str(result))