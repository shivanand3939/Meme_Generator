"""Get the quote and the body"""


class QuoteModel():

    def __init__(self, body, author):
        self.body = body
        self.author = author


    def get_body(self):
        return self.body


    def get_author(self):
        return self.author

    def __repr__(self):
        return '"{}" - {}'.format(self.body, self.author)
