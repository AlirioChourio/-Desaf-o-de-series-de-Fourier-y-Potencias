# Importar librerías matemáticas
import numpy as np         # Para operaciones numéricas
import pandas as pd        # Para manipulación de datos
import matplotlib.pyplot as plt  # Para visualización de datos
import scipy               # Para funciones científicas
import sympy as sp              # Para matemáticas simbólicas

# Importar frameworks
from flask import Flask, render_template, request  # Para usar Flask
import random

# Crear una instancia de Flask
app = Flask(__name__)

# Lista de preguntas
questions = [
    {
        'id': 'pregunta1',
        'question': '¿Qué es una serie de potencias?',
        'options': {
            'a': 'Una suma finita de términos.',
            'b': 'Una serie que incluye potencias de una variable.',
            'c': 'Un tipo de ecuación diferencial.'
        },
        'correct_answer': 'b'
    },
    {
        'id': 'pregunta2',
        'question': '¿Qué se entiende por radio de convergencia en el contexto de series de potencias?',
        'options': {
            'a': 'El número máximo de términos en la serie.',
            'b': 'El conjunto de valores para los cuales la serie converge.',
            'c': 'La distancia entre el centro de la serie y el primer término.'
        },
        'correct_answer': 'b'
    },
    {
        'id': 'pregunta3',
        'question': '¿Cuál es el papel del punto c en una serie de potencias?',
        'options': {
            'a': 'Es el centro alrededor del cual se desarrolla la serie.',
            'b': 'Es el valor máximo que puede tomar x.',
            'c': 'Es el coeficiente principal de la serie.'
        },
        'correct_answer': 'a'
    },
    {
        'id': 'pregunta4',
        'question': '¿Qué tipo de funciones se pueden representar mediante series de potencias?',
        'options': {
            'a': 'Solo funciones polinómicas.',
            'b': 'Solo funciones periódicas.',
            'c': 'Funciones comunes y nuevas funciones complejas.'
        },
        'correct_answer': 'c'
    },
    {
        'id': 'pregunta5',
        'question': '¿Quién desarrolló la teoría de las series de Fourier?',
        'options': {
            'a': 'Jean-Baptiste Joseph Fourier.',
            'b': 'Isaac Newton.',
            'c': 'Carl Friedrich Gauss.'
        },
        'correct_answer': 'a'
    },
    {
        'id': 'pregunta6',
        'question': '¿Qué se entiende por radio de convergencia en el contexto de series de potencias?',
        'options': {
            'a': 'El número máximo de términos en la serie.',
            'b': 'El conjunto de valores para los cuales la serie converge.',
            'c': 'La distancia entre el centro de la serie y el primer término.'
        },
        'correct_answer': 'b'
    },
    {
        'id': 'pregunta7',
        'question': 'Al calcular el radio de convergencia de la serie Σ (n²x^n) / 3^n, ¿qué resultado obtenemos?',
        'options': {
            'a': '1/3',
            'b': '3',
            'c': '9'
        },
        'correct_answer': 'a'
    },
    {
        'id': 'pregunta8',
        'question': 'En una serie de Fourier para f(x) = x² en el intervalo [-π, π], ¿cuál será el valor del coeficiente a₀?',
        'options': {
            'a': 'π²/3',
            'b': '2π²/3',
            'c': 'π²'
        },
        'correct_answer': 'b'
    },
    {
        'id': 'pregunta9',
        'question': 'Si expandimos ln(1+x) en una serie de Maclaurin, ¿cuál es el tercer término no nulo de la serie?',
        'options': {
            'a': 'x²/2',
            'b': '-x²/2',
            'c': '-x³/3'
        },
        'correct_answer': 'c'
    },
    {
        'id': 'pregunta10',
        'question': 'Al representar una onda cuadrada con una serie de Fourier, ¿qué términos estarán presentes?',
        'options': {
            'a': 'Solo términos seno',
            'b': 'Solo términos coseno',
            'c': 'Solo términos seno de orden impar'
        },
        'correct_answer': 'c'
    },
    {
        'id': 'pregunta11',
        'question': '¿Cuál es la expresión de la serie de potencias para la función f(x) = e^x alrededor de x = 0?',
        'options': {
            'a': 'Σ (x^n) / n!',
            'b': 'Σ (x^n) / n²!',
            'c': 'Σ (x^n) / (n+1)!'
        },
        'correct_answer': 'a'
    },
    {
        'id': 'pregunta12',
        'question': 'Al calcular los coeficientes de Fourier para f(x) = |x| en [-π, π], ¿cuál será el valor de b₁?',
        'options': {
            'a': '0',
            'b': '2/π',
            'c': '-2/π'
        },
        'correct_answer': 'b'
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Recuperar las preguntas seleccionadas de la solicitud anterior
        selected_questions = request.form.getlist('selected_questions')

        # Recibir respuestas del formulario
        respuestas = {question_id: request.form.get(question_id, 'no respondida') for question_id in selected_questions}

        # Verificar respuestas
        resultados = []
        
        # Filtrar las preguntas que se respondieron
        for question_id in selected_questions:
            # Buscar la pregunta correspondiente en la lista original
            pregunta = next((q for q in questions if q['id'] == question_id), None)
            if pregunta:
                respuesta = respuestas[question_id]
                # Verificar si la respuesta es correcta
                if respuesta == 'no respondida':
                    resultados.append(f"Pregunta {pregunta['id']}: Incorrecto (Respuesta correcta: {pregunta['correct_answer']})")
                elif respuesta == pregunta['correct_answer']:
                    resultados.append(f"Pregunta {pregunta['id']}: Correcto")
                else:
                    resultados.append(f"Pregunta {pregunta['id']}: Incorrecto (Respuesta correcta: {pregunta['correct_answer']})")

        # Unir resultados en una cadena
        resultados_str = '<br>'.join(resultados)  # Cambiar a <br> para HTML

        # Seleccionar 3 nuevas preguntas aleatorias para la próxima ronda
        new_selected_questions = random.sample(questions, 3)

        # Renderizar la plantilla con los resultados y nuevas preguntas
        return render_template('index.html', results=resultados_str, questions=new_selected_questions, selected_questions=new_selected_questions)
    else:
        # Seleccionar 3 preguntas aleatorias al inicio
        selected_questions = random.sample(questions, 3)
        return render_template('index.html', questions=selected_questions, results=None, selected_questions=selected_questions)



# SERIES DE POTENCIAS
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