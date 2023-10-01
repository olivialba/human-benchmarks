from benchmarks.ReactionTime import ReactionTime
from benchmarks.AimTrainer import AimTrainer

benchmark_tests = {
    '1': ReactionTime,
    '2': AimTrainer
}

def select_benchmark():
    print()
    print("Benchmarks:")
    for num, test in benchmark_tests.items():
        print(f"{num}. {test.__name__}")
    print()
    bech_num = input("Which Benchmark test do you want to do? ")
    selec_func = benchmark_tests.get(bech_num)
    if selec_func:
        selec_func()
    else:
        print(f"Invalid input: {bech_num}")


if __name__ == "__main__":
    select_benchmark()