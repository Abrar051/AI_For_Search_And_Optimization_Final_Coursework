class SimulatedAnnealing:
    def __init__(self, cities: np.ndarray, initial_temp: float = 10000,
                 cooling_rate: float = 0.995, min_temp: float = 0.1):

        self.cities = cities
        self.n_cities = len(cities)
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.best_tour = None
        self.best_distance = float('inf')
        self.history = []

    def get_initial_solution(self) -> List[int]:
        tour = list(range(self.n_cities))
        random.shuffle(tour)
        return tour

    def get_neighbor(self, tour: List[int]) -> List[int]:
        new_tour = tour.copy()
        i, j = sorted(random.sample(range(self.n_cities), 2))
        new_tour[i:j + 1] = reversed(new_tour[i:j + 1])
        return new_tour

    def acceptance_probability(self, current_dist: float, new_dist: float,
                               temp: float) -> float:
        if new_dist < current_dist:
            return 1.0
        return np.exp((current_dist - new_dist) / temp)



