import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'

)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Parametros:
    def GET(self):
        titulo = "Título desde Python"
        descripcion = """Lorem ipsum dolor sit amet, consectetur adipiscing
                    elit. In cursus lacus vel commodo scelerisque. Sed tincidunt orci non porttitor sodales. Phasellus metus sem, pretium eu mattis ac, dapibus ac augue. Suspendisse nec nibh nulla. Maecenas varius et massa condimentum mattis. Nulla at enim urna. Nullam in aliquet sapien. Curabitur varius facilisis neque, eget laoreet massa scelerisque et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pretium a odio vel aliquet. Quisque ullamcorper arcu eu urna pharetra, sed ullamcorper neque bibendum. In quam est, consequat at luctus at, eleifend eu tellus. Suspendisse ultricies nisi vel justo commodo varius. Quisque vitae vestibulum velit."""
        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()