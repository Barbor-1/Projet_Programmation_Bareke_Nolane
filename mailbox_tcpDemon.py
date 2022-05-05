#MESSAGE DEF : dict


class MailboxTcp(): # no client / server => commands 
    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
    def getMessage(self):
        return self.output_queue.get()
    def send_command(self, command):
        self.input_queue.put(command)
        self.input_queue.join() # wait for demon to finish task
        return self.output_queue.get()
