class Counter:
    def __init__(self):
        self.n = 1
        print("__init__")

    def __enter__(self):
        print("__enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"__exit__:"
              f"\nexc_type={exc_type}\nexc_val={exc_val}\nexc_tb={exc_tb}")


def demo_with():
    with Counter() as c:
        return c


def demo_error_handling():
    print("--> demo error handling: exit is always invoked")
    with Counter() as counter:
        return counter.n + "error"


if __name__ == "__main__":
    demo_with()
    demo_error_handling()
