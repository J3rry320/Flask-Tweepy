from .main import create_app

app = create_app('dev')


@app.route('/')
def hello():
    return 'Hello From an amazing twitter API.'


if __name__ == '__main__':
    app.run()
