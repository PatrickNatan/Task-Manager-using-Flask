def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

if __name__ == "__main__":
    test_soma()
    print("Todos os testes passaram!")