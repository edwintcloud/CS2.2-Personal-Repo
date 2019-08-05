from timeit import default_timer as timer


def runtime(f):
    def timed(*args, **kwargs):
        start = timer()
        result = f(*args, **kwargs)
        end = timer()
        print(f'{f.__name__}: {((end - start) * 1000):.2f}ms')
        return result

    return timed


@runtime
def naive_solution(seq_A, seq_B):

    # BASE CASE: we have reached the end of sequence A or sequence B
    if len(seq_A) == 0 or len(seq_B) == 0:
        return 0

    # if the last character of sequence a and sequence b match, recur


if __name__ == "__main__":
    naive_solution('a', 'b')
