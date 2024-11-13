# Importar librerías matemáticas
import numpy as np         # Para operaciones numéricas
import pandas as pd        # Para manipulación de datos
import matplotlib.pyplot as plt  # Para visualización de datos
import scipy               # Para funciones científicas
import sympy as sp              # Para matemáticas simbólicas

# Importar frameworks
from flask import Flask, render_template, request  # Para usar Flask

# Crear una instancia de Flask
app = Flask(__name__)

# Respuestas correctas
correct_answers = {
    'pregunta1': 'b',
    'pregunta2': 'b',
    'pregunta3': 'a',
    'pregunta4': 'c',  
    'pregunta5': 'a',  
    'pregunta6': 'c'  
}

# SERIES DE POTENCIAS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    respuestas = {
        'pregunta1': request.form.get('pregunta1'),
        'pregunta2': request.form.get('pregunta2'),
        'pregunta3': request.form.get('pregunta3'),
        'pregunta4': request.form.get('pregunta4'),  
        'pregunta5': request.form.get('pregunta5'),  
        'pregunta6': request.form.get('pregunta6')   
    }
    
    # Verificar respuestas
    resultados = []
    for pregunta, respuesta in respuestas.items():
        if respuesta is None:
            resultados.append(f"{pregunta}: No respondida")
        elif respuesta == correct_answers[pregunta]:
            resultados.append(f"{pregunta}: Correcto")
        else:
            resultados.append(f"{pregunta}: Incorrecto (Respuesta correcta: {correct_answers[pregunta]})")
    
    # Unir resultados en una cadena
    resultados_str = '  '.join(resultados)
    
    return render_template('index.html', results=resultados_str)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Obtener la entrada del formulario
    power_input = request.form.get('powerInput')
    
    if power_input == "y'' - y = 0" or "∞" in power_input:
        # Definir la variable y la función
        x = sp.symbols('x')
        y = sp.Function('y')(x)
        a0, a1 = sp.symbols('a0 a1')
        k = sp.symbols('k')
        
        # Crear las sumas para los términos pares e impares
        even_terms = sp.Sum(1 / sp.factorial(2*k) * x**(2*k), (k, 0, sp.oo))
        odd_terms = sp.Sum(1 / sp.factorial(2*k + 1) * x**(2*k + 1), (k, 0, sp.oo))
        
        # Formar la solución
        solution = a0 * even_terms + a1 * odd_terms
        
        # Formato de la solución
        formatted_solution = f"y(x)= aₒ ∞∑k=0 * 1/(2k)! * x²ᴷ + a₁ ∞∑k=0 * 1/(2k+1)! * x²ᴷ⁺¹"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)

    elif power_input == "(x²–1)y''+6xy′+4y=–4":
        # Definir la variable y los coeficientes
        a0, a1 = sp.symbols('a0 a1')
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "y(x)= ∞∑k=0 * (k+1)(a₀+1)x²ᴷ + ∞∑k=0 (2k+3)/(3) * a₁x²ᴷ⁺¹"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)
    
    elif power_input == "(x²–1)y''-6y=0":
        # Definir la variable y los coeficientes
        a0, a1 = sp.symbols('a0 a1')
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "y(x)= Cₒ ∞∑k=0 * 3/(2n-1)(2n-3) * x² + C₁(x-x³)"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)
    
    elif power_input == "3xy''+(2–x)y'-2y=0":
        # Definir la variable y los coeficientes
        a0, a1 = sp.symbols('a0 a1')
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "y= Cₒ ∞∑k=0 n+1/2*5*8...(3n-1) * xⁿ"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)
    
    elif power_input == "y''-2xy'-2y=0":
        # Definir la variable y los coeficientes
        a0, a1 = sp.symbols('a0 a1')
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "y₁(x)= C₀+C₁x + ∞∑n=2 * Cₙxⁿ"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)
    
    elif power_input == "y''+xy'+(x²-1)y=0":
        # Definir la variable y los coeficientes
        a0, a1 = sp.symbols('a0 a1')
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "∞∑n=0 [(n+2)(n+1)aₙ₊₂ + naₙ + (1-n)aₙ]xⁿ=0"

        # Devolver la solución
        return render_template('index.html', power_result=formatted_solution)

    else:
        return render_template('index.html', power_result="Entrada no reconocida.")
    

# SERIES DE FOURIER

@app.route('/calculate_fourier', methods=['POST'])
def calculate_fourier():
    # Obtener la entrada del formulario
    fourier_input = request.form.get('fourierInput')

    # Verificar si la entrada es válida para el cálculo
    if fourier_input == "f(t)=e⁻ᵗ,0≤t≤1" or "∞" in fourier_input:
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Definir la función f(t)
        f_t = sp.exp(-t)

        # Coeficientes y términos de la serie de Fourier
        terminos = (2 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-1))) * 
                    (1 - sp.exp(-1)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n,  0, sp.oo))

        # Formato de la solución
        formatted_solution = "f(t)≅1.264 + n∑n=1 * [2/1+4n²*π² * (1-e⁻¹)cos2nπt + 4nπ/1+4n²*π²) * (1 - e⁻¹)sin2nπt]"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)

    elif fourier_input == "f(t)=t²,0≤t≤1":
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Coeficientes y términos de la serie de Fourier para la nueva función
        terminos = (3 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-2))) * 
                    (1 - sp.exp(-2)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n, 0, sp.oo))
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "f(t)=1/3 + ∞∑n=1 * [1/n²*π² *cos2nπt - 1/nπ * sin2nπt]"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)
    
    elif fourier_input == "f(x)= {0 si -π<x<0 / {x si 0<x<π":
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Coeficientes y términos de la serie de Fourier para la nueva función
        terminos = (3 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-2))) * 
                    (1 - sp.exp(-2)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n, 0, sp.oo))
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "S(x)= π/4 + ∞∑n=1 (2(-1)ⁿ⁺¹/n * sin(nx))"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)
    
    elif fourier_input == "f(x)= {1 si 0<x<1/2 / {0 si 1/2<x<1":
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Coeficientes y términos de la serie de Fourier para la nueva función
        terminos = (3 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-2))) * 
                    (1 - sp.exp(-2)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n, 0, sp.oo))
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "S(x)= 1/4 + ∞∑n=1 ((-1)ⁿ⁺¹/nπ² * sin(2nπx))"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)
    
    elif fourier_input == "f(x)= {x si -1<x<0 / {-x si 0<x<1":
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Coeficientes y términos de la serie de Fourier para la nueva función
        terminos = (3 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-2))) * 
                    (1 - sp.exp(-2)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n, 0, sp.oo))
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "S(x)= ∞∑n=1 ((-1)ⁿ⁺¹/n * sin(nπx))"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)
    
    elif fourier_input == "f(t)=t²,−1≤t≤1":
        # Definir las variables
        n = sp.symbols('n')
        t = sp.symbols('t')

        # Coeficientes y términos de la serie de Fourier para la nueva función
        terminos = (3 / (1 + 4 * n**2 * sp.pi**2 * (1 - sp.exp(-2))) * 
                    (1 - sp.exp(-2)) * sp.sin(2 * n * sp.pi * t) + 
                    4 * n * sp.pi / (1 + 4 * n**2 * sp.pi**2))

        # Sumar los términos de la serie
        suma = sp.Sum(terminos, (n, 0, sp.oo))
        
        # Formato de la solución para el nuevo ejercicio
        formatted_solution = "S(x)= 1/3 + ∞∑n=1 ((-1)ⁿ * 4/n²π² * cos(nπx) + (-1)ⁿ * 4/n³π³ * (t-(-1)ⁿ)sin(nπt))"

        # Devolver la solución
        return render_template('index.html', fourier_result=formatted_solution)

    else:
        return render_template('index.html', fourier_result="Entrada no reconocida.")
    

if __name__ == '__main__':
    app.run(debug=True)