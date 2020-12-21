from .handlers import status, create_team, send_alert
from config import GET, POST, PUT, DELETE


API_ENDPOINTS = {
    '/status/': (status, [GET]),
    '/create_team/': (create_team, [POST]),
    '/send_alert/': (send_alert, [POST])

}
