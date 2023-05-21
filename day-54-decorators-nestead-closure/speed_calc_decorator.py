import time

# ===================== decorator =====================
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


def speed_calc_decorator_v2(function):
    """
    Decoradores sempre precisam retornar uma função, por isso, por boa pratica se usa wrapper function e se retorna ela,
    caso tenha uma logica antes e/ou depois da chamada da função original, ai poem toda logica la dentro "empacotado" (wrapped)
    além que com a wrapper function é possivel usar as variaveis especiais como __name__
    essa é uma versão sem função aninhada (nested function) porém é mais "feio" e não fica tão limpo quanto a outra versão
    """
    start_time = time.time()
    function()
    end_time = time.time()
    print(f"run speed: {end_time - start_time}s")

    return function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


# ===================== closure =====================
# a function that can remember and access variables that are not in scope anymore
# usado em casos de funções sincronas e/ou assicronas, quando depende do estado de outra função para executar uma
# determinada logica, igual em circuitos digitais

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure = outer_function(10)
result = closure(5)
print(result)  # Output: 15
