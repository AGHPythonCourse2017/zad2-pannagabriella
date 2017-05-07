import zad2pannagabriella as gaba
def init(x):
    return x

def function(n):
    for i in range(0,n):
        for i in range(0,n):
            pass

def clean(x):
    pass

if __name__ == '__main__':
    generator = gaba.Generator(init, function, clean)

    generator.start(10)
    print(generator.get_function_info())