# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')

# The repository to add this issue to
REPO_OWNER = os.getenv('USERNAME')
REPO_NAME = 'LLMDailyPapers'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["soft","robot", ]


OPENAI_API_KEYS = ['', ]
DEEPSEEK_API_KEY = [str(os.getenv('OPENAI_API_KEYS'))]  # DeepSeek API密钥
DEEPSEEK_API_URL = [str(os.getenv('OPENAI_API_URL'))]  # DeepSeek API密钥
LANGUAGE = "zh"  # zh | en
