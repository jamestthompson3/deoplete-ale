import re
import os
from os.path import exists

from deoplete.source.base import Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'ale'
        self.mark = '[ALE]'
        self.description = 'Complete for ALE'

    def gather_candidates(self, context):
        # case = context['smartcase'] or context['camelcase']
        # ignorecase = context['ignorecase']
        # if case and re.search(r'[A-Z]', context['complete_str']):
        #     ignorecase = True
        # if ignorecase:
        #     complete_str_0 = (context['complete_str'][0].lower()
        #                         if len(context['complete_str']) > 0 else '')
        #     complete_str_1 = (context['complete_str'][1].lower()
        #                         if len(context['complete_str']) > 1 else '')
        #     prefixes = list({
        #         complete_str_0 + complete_str_1,
        #         complete_str_0 + complete_str_1.upper(),
        #         complete_str_0.upper() + complete_str_1,
        #         complete_str_0.upper() + complete_str_1.upper(),
        #         })
        # else:
        #     prefixes = [context['complete_str']]
        return self.vim('ale#completion#GetCompletions()')
