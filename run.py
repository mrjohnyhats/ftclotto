from ftclotto import app

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), host='127.0.0.1', port=8000)
