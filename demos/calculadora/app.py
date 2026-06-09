import web

urls = (
    '/', 'Index',
        '/calculadora', 'Calculadora'
        )
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
            return render.index()
                
class Calculadora:
    def GET(self):
            return render.calculadora()
    
    def POST(self):
            formulario = web.input()
            numero_1 = int(formulario.numero_1)
            numero_2 = int(formulario.numero_2)
            resultado = numero_1 + numero_2 

            return f"Numero 1: {numero_1}, Numero 2: {numero_2}, Resultado: {resultado}"

if __name__ == "__main__":
    app.run()