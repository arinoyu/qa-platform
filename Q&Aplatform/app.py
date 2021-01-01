from appdir import app

# if __name__ == '__main__':
#     app.config['SERVER_NAME'] = 'www.arino.top'
#     app.run('0.0.0.0', port=443, debug=True,
#             ssl_context=('ssl/4620052_www.arino.top.pem', 'ssl/4620052_www.arino.top.key'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
