from www.celery import app
from services.hospital.update_pers import UpdatePers
@app.task
def update_pers(user):
    up = UpdatePers(user)
    up.update()
    up.update_pers()
    return 'Update task'
