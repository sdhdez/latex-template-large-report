# -*- coding: utf-8 -*-
from pygments.lexers.shell import BashSessionLexer
from pygments.token import Name, Keyword

class MyConsoleLexer(BashSessionLexer):
    EXTRA_KEYWORDS = set(('pip', 'git', 'clone', 'python', 'install'))

    def get_tokens_unprocessed(self, text):
        for index, token, value in BashSessionLexer.get_tokens_unprocessed(self, text):
            print(index, token, value)
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value
