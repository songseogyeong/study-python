import datetime

def log_time(original_function):
    formatting = None

    def logging(*args, **kwargs):
        self, other = args
        error_code = kwargs.get('error_code')
        with open('log.txt', 'a', encoding='utf-8') as file:
            result = original_function(*args, **kwargs)
            now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            if error_code is None:
                if self.oper == '/':
                    value, rest = result
                    file.write(f'{self.number} {self.oper} {other} = {value}, {result}\tKST{now}\n')

                else:
                    file.write(f'{self.number} {self.oper} {other} = {result}\tKST{now}\n')

            else:
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                file.write(f'{error_code}\tKST\n')
        # nonlocal formatting
        # formatting = ""
        return result

    return logging