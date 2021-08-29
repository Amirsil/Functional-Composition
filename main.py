from timer import measure_time
from lazy_generators import divisable_by, infinity_from, power_by, until, get_n_items
from concat import APPLY
if __name__ == "__main__":
    APPLY << print << '\n'.join << list << 'HELLO'
    measure_time(lambda: APPLY << print << list << get_n_items(30) << power_by(2) << infinity_from << 1)
