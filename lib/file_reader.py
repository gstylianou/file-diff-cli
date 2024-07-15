class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as hello_file:
            hello_file_content = hello_file.readlines()
            return hello_file_content
