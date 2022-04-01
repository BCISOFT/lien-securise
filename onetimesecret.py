from app import app, db
from app.models import OTS
from datetime import datetime
from crontab import CronTab
import time


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'OTS': OTS}


