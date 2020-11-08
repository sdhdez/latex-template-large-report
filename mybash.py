# -*- coding: utf-8 -*-
from pygments.lexers.python import BashLexer
from pygments.token import Name, Keyword

class MyBashLexer(BashLexer):
    EXTRA_KEYWORDS = set(('git', 'clone', 'pip', 'python'))
    def get_tokens_unprocessed(self, text):
        for index, token, value in BashLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value