import web 

urls = (
    '/', 'controllers.index.Index',
    '/contactos', 'controllers.contactos.Contactos'
)

app = web.application(urls, globals())
render = web.template.render('views')

if __name__ == "_main_":
    app.run()
    