from db import db
from sqlalchemy.sql.expression import func
from .models import Team, Developer


def check_team_count(team_details):
    try:
        team_name = team_details['name']
        x = db.session.query(Team).filter_by(name=team_name).all()
        return len(x)
    except Exception as e:
        return -1


def create_team_devs(team_details, dev_details):
    try:
        team_name = team_details['name']
        t = Team(name=team_name)
        db.session.add(t)
        db.session.flush()
        for dev in dev_details:
            dev_name = dev['name']
            dev_pn = dev['phone_number']
            d = Developer(team_id=t.id, name=dev_name, phone_number=dev_pn)
            db.session.add(d)
        db.session.commit()
        return True
    except Exception as e:
        print('exception occurred due to {}'.format(e))
        db.session.rollback()
        return False


def fetch_dev(team_details):
    try:
        team_name = team_details['name']
        team = db.session.query(Team).filter_by(name=team_name).first()
        dev = db.session.query(Developer).filter_by(team_id=team.id).order_by(func.random()).first()
        return dev.phone_number
    except Exception as e:
        print('exception occurred due to {}'.format(e))
        return None
