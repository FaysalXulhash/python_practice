class Phone:
    def call(self):
        print('I can call')

    def message(self):
        print('I can message')


class Samsung(Phone):

    def photo(self):
        print('I cant take photo')


a = Samsung()
a.call()
a.message()
a.photo()

