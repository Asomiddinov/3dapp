from flask import Flask, render_template
from winotify import Notification, audio
app = Flask(__name__)
notification = Notification(app_id="New task for you",
                            title="Babai notifies",
                            msg="Oylik otchet tayyorlash",
                            icon="C:/Users/User/Downloads/Telegram Desktop/bab.png",
                            launch="http://192.168.199.11:5000/home/",
                            duration="long")
notification.set_audio(audio.LoopingAlarm9, loop=False)


@app.route("/")
@app.route("/home")
@app.route("/home/")
def index():
    return render_template("index.html")


@app.route("/filter")
@app.route("/filter/")
def filter():
    notification.show()
    return render_template("filter.html", notification=notification)


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(host="192.168.199.11",
            port=5000, debug=True)
