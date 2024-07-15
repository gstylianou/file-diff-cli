class FileReader:
    """read file class"""

    def __init__(self, path):
        self.path = path

    def read(self):
        """read a file"""
        try:
            with open(self.path) as hello_file:
                hello_file_content = hello_file.readlines()
                return hello_file_content
        except Exception as e:
            print("failed to open file with error", e)
            return []
