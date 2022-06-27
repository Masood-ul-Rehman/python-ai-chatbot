
import json


class Search_process:
    def __int__(self, rep):
        self.resp = rep.capitalize()
        with open('intents.json') as file:
            data = json.load(file)


# a = 0
# for key, values in data.items():
#     print("Process started with " + self.resp)
#     size = len(values)
#     while a <= size:
#         print("Process " + str(a))
#         if self.resp in values[a]["patterns"]:
#             print("Found at " + str(a))
#             self.responce = random.choice(values[a]["responses"])
#             a = size
#         a = a + 1
