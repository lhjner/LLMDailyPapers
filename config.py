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
KEYWORD_LIST = ["AI-generated content detection","AI-generated image detection", "Synthetic image / media detection","Multimodal detection"]


OPENAI_API_KEYS = os.getenv('OPENAI_API_KEYS', '').split(',')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')
DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL', '')
LANGUAGE = os.getenv('LANGUAGE', 'zh')  # zh | en
