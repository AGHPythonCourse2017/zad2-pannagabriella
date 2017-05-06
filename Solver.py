class Solver:
    def __init__(self, function_details):
        self.function_details = function_details
    def solve(self):
        n2_counter = 0
        n_counter = 0
        s_counter = 0

        main_counter = 0
        for x in self.function_details["x"]:
            n2_value = self.function_details["n2_function"](x)
            n_value = self.function_details["n_function"](x)
            s_value = self.function_details["s_function"](x)

            d_n2 = abs(n2_value - self.function_details["n2_y"][main_counter])
            d_n = abs(n_value - self.function_details["n_y"][main_counter])
            d_s = abs(s_value - self.function_details["s_y"][main_counter])