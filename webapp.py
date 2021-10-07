import flask
import uptime
import redis

app = flask.Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)
r.set("counter", '0')

@app.route("/")
def static_counter():
    counter = r.get("counter")
    html = "<h2>{counter}</h2>"
    return html.format(counter=str(int(counter)))
    

@app.route("/stat")
def stat():
    r.incrby("counter", 1)
    counter = r.get("counter")
    html = "<h2>{counter}</h2>"
    return html.format(counter=str(int(counter)))


@app.route("/about")
def about():
    html = "<h3>Hello, Tatiana!</h3>" \
    "<b>Uptime:</b> {uptime}<br/>"
    return html.format(uptime=str(uptime.uptime()))


   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

