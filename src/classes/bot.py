

class Memory:
    def __init__(self):
        self.memory = []

    def add(self, name, sentence):
        # clear new line
        sentence = sentence.replace("\n", " ")

        # trim space
        sentence = sentence.strip()

        self.memory.append(f"{name}: {sentence}")

    def get(self):
        return "\n".join(self.memory)


class Bot:
    def __init__(self, name, gateway, memory):
        self.name = name
        self.gateway = gateway
        self.memory = memory

    def listen(self, name: str, sentence: str):
        self.memory.add(name, sentence)

    def speak(self):
        prompt = self.memory.get()
        prompt = f"{prompt}\n {self.name}:"
        response = self.gateway.create_completion(prompt)
        self.memory.add(self.name, response)
        return response

    def export_memory(self):
        return self.memory.get()
