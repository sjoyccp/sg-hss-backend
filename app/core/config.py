import os

BASE_DIR = os.getcwd()
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'sg_hss.db')}"
SECRET_KEY = "segredo"
