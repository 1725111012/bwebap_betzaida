import web
import math

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
            numero_1=0.0
            numero_2=0.0
            resultado=0.0
            return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
            formulario = web.input()
            operacion = formulario.get('operacion')
            if operacion == "limpiar":
                return render.calculadora(0.0, 0.0, 0.0)
            
            numero_1 = float(formulario['numero_1'])
            numero_2 = float(formulario['numero_2'])
            resultado = 0.0
            
            if operacion == "sumar":
                resultado = numero_1 + numero_2
            elif operacion == "restar":

                resultado = numero_1 - numero_2
            elif operacion == "multiplicar":
                resultado = numero_1 * numero_2

            elif operacion == "dividir":
                if numero_2 != 0:
                    resultado = numero_1 / numero_2
                else:
                    resultado = "Error: Div entre 0"

            elif operacion == "potencia":
                resultado = numero_1 ** numero_2
            
            elif operacion == "raiz":
                if numero_1 >= 0:
                    resultado = math.sqrt(numero_1)
                else:
                    resultado = "Error: Raíz negativa"
            
            elif operacion == "modulo":
                resultado = numero_1 % numero_2

            print (f"Tipo de dato de numero_1 : {type(numero_1)}")
            print (f"Tipo de dato de numero_2 : {type(numero_2)}")

            return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
    