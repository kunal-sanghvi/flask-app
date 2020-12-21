import requests

from config import NOTIF_URL
from db.ops import create_team_devs, check_team_count, fetch_dev
from flask import jsonify, request
from middleware import basic_auth


def status():
    return jsonify(message='Hello Stranger!')


def return_bad_request(message):
    r = jsonify(message=message)
    r.status_code = 400
    return r


def return_internal_error():
    r = jsonify(message='internal error, please try again in sometime')
    r.status_code = 500
    return r


def valid_team_details(team_details):
    return False if (not isinstance(team_details, dict) or not team_details.get('name', None)) else True


def valid_dev_details(dev_details):
    if not isinstance(dev_details, list) or len(dev_details) == 0:
        return False
    for dev in dev_details:
        if not isinstance(dev, dict) or not dev.get('name', None) or not dev.get('phone_number', None):
            return False
    return True


def valid_alert_details(alert_details):
    if not isinstance(alert_details, dict) or not alert_details.get('name', None) or not alert_details.get('message', None):
        return False
    return True


@basic_auth
def create_team(log):
    print('creating team')
    req_body = request.get_json()
    if not req_body:
        return return_bad_request(message='empty request body not allowed')
    team_details = req_body.get('team', None)
    if not team_details or not valid_team_details(team_details):
        return return_bad_request(message='team details are missing')

    dev_details = req_body.get('developers', None)
    if not dev_details or not valid_dev_details(dev_details):
        return return_bad_request(message='dev details are missing')
    team_count = check_team_count(team_details)
    if team_count < 0:
        return return_internal_error()
    if team_count > 0:
        return return_bad_request(message='team {} already exists'.format(team_details['name']))
    entities_created = create_team_devs(team_details, dev_details)
    if entities_created:
        return jsonify(message='Team created!')
    else:
        return return_bad_request(message='Failed to create entities')


def alert_with_retry(message, phone_num):
    data = {
        'phone_number': phone_num,
        'message': message
    }
    for x in range(2):
        try:
            resp = requests.post(NOTIF_URL, data=data)
            if resp.status_code == 200:
                return True
        except Exception as e:
            pass
    return False


@basic_auth
def send_alert(log):
    print('sending alert')
    req_body = request.get_json()
    if not req_body:
        return return_bad_request(message='empty request body not allowed')
    if not valid_alert_details(req_body):
        return return_bad_request(message='invalid alert details')
    if check_team_count(req_body) == 0:
        return return_bad_request(message='Team {} does not exists'.format(req_body['name']))
    phone_num = fetch_dev(req_body)
    if not phone_num:
        return return_internal_error()
    if not alert_with_retry(req_body['message'], phone_num):
        return return_internal_error()
    return jsonify(message='alerted {}'.format(phone_num))


