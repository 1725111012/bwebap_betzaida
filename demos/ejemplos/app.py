import web

web.config.debug = False

urls = (
    "/count", "count",
    "/reset", "reset",
)

app = web.application(urls, locals())

# Store session data in folder 'sessions' under the same directory as your app.
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"count": 0})

class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return "Reset"

if __name__ == "__main__":
    app.run()