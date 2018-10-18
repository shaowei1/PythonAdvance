class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + 'was call'
        print(log_string)
        with open(self.logfile, 'a') as open_file:
            # Now we log to the specified logfile
            open_file.write(log_string, '\n')
        # Now, send a notification
        self.notify()

    def notify(self):
        # logit only logs, no more
        pass

