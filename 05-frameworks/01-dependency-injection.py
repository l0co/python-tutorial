#######################################################################################################################
print("there's a lib for dependency injection in Python called 'injector'")
# pip install injector

from injector import Injector, inject, singleton

class Repository:
    def get_data(self):
        return "here's some repo data"

@singleton
class MyService:
    @inject
    def __init__(self, repo: Repository):
        self.repo = repo

    def run(self):
        print(self.repo.get_data())

injector = Injector()  # create container

service = injector.get(MyService)  # get instance
service.run()  # STDOUT: here's some repo data

# quite limitied with no interfaces, though
# would love to test with multiple inheritance, but this will be definitely out of this tutorial scope
