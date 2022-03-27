def create_url_token(ip, session_id, port = None) -> str:
    if port == None:
        return 'http://' + ip + '/token/url?id=' + session_id
    else:
        return 'http://' + ip + ':' + port + '/token/url?id=' + session_id


if __name__ == "__main__":
    print(create_url_token('145.123.45.123', '38j1s89j21js18', "3000"))
    print(create_url_token('145.123.45.123', '38j1s89j21js18'))