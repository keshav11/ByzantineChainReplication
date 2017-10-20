class Object:
    def __init__(self):
        self.state = {}

    def put(self, key, value):
        print('In put:', key, value)
        self.state[key] = value
        return 'OK'

    def get(self, key):
        print('In get:', key)
        try:
            print('GET for key ', key, 'returning val ', self.state[key])
            return self.state[key]
        except KeyError:
            print('error: key does not exist:', key)
            return ''

    def slice(self, key, slice):
        print('In slice:', key, slice)
        if key not in self.state.keys():
            return 'fail'
        current_val = self.state[key]
        slice_params = slice.split(':')
        start = int(slice_params[0])
        end = int(slice_params[1])
        step = 1
        if len(slice_params) == 3:
            step = int(slice_params[2])
        try:
            rval = current_val[start:end:step]
            if rval == '':
                return 'fail'
            self.state[key] = rval
            print('Updated key ', key, ' val to ', rval, ' after slicing')
            return 'OK'
        except Exception as e:
            print('Exception while slicing: ', e)
            return 'fail'

    def append(self, key, value): # TODO
        print('In append:', key, value)
        if key not in self.state.keys():
            return 'fail'
        self.state[key] += value
        return 'OK'

    def print_obj(self):
        print('printing object after request evaluation...')
        for key in self.state:
            print(key, '->', self.state[key])

    def evaluate_request(self, request):
        print('In evaluate_request:', request)
        request = request.strip()
        if request.startswith('get'):
            processed_request = request.strip()[4:-1]
            return_val = self.get(processed_request.strip().strip('\''))
        elif request.startswith('put'):
            key_val = request.strip()[4:-1].strip().split(',')
            return_val = self.put(key_val[0].strip().strip('\''),
                            key_val[1].strip().strip('\''))
        elif request.startswith('append'):
            key_val = request.strip()[7:-1].strip().split(',')
            return_val = self.append(key_val[0].strip().strip('\''),
                               key_val[1].strip().strip('\''))
        elif request.startswith('slice'):
            key_val = request.strip()[6:-1].strip().split(',')
            return_val = self.slice(key_val[0].strip().strip('\''),
                              key_val[1].strip().strip('\''))

        self.print_obj()
        return return_val

def main():
    # Testing Object
    o = Object()
    print(o.evaluate_request('put(\'fruit\',\'apple\')'))
    print(o.evaluate_request('get(\'fruit\')'))
    o.evaluate_request('slice(\'fruit\',\'apple\')')
    o.evaluate_request('append(\'fruit\',\'apple\')')


if __name__ == "__main__":
    main()