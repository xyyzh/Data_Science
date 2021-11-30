def get_user(request_handler):
    username = request_handler.get_argument('username')
    pw = request_handler.get_argument('password')

    if username == 'nyc' and pw == 'iheartnyc':
        return 1
    else:
        print("Incorrect username or password.")
        return None

login_url = '/login'
