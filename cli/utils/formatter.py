class Formatter:    
    @staticmethod
    def display(data):
        print()
        print(data["title"])
        print("-" * 40)
        for key, value in data["items"].items():
            print(f"{key}: {value}")
        print()