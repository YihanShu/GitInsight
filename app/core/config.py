import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # 不再写死 repo
    REPO_PATH = None