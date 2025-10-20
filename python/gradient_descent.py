def gradient_descent(f_derivative, start, learning_rate, epochs):

    x = start

    for _ in range(epochs):

        gradient = f_derivative(x)

        x = x - learning_rate * gradient

    return x