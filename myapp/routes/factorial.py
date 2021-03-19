from myapp import app

<<<<<<< HEAD
@app.route('/factorial/<int:n>')
def factorial(n):

    if n == 1:
        return n
    else:
        return n*factorial(n-1)
=======

def factorial(n):
    if n == 1:
        return n
    else:

        return n * factorial(n - 1)

@app.route('/factorial/<int:n>')
def factorial_handler(n):
    return {"result": factorial(n)}




>>>>>>> e5ae26b3330778bb7515d73650266847f7b2823c
