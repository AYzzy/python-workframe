import playground


class TestListFunction:
    def test_that_function_return_total_of_list(self):
        sample_list = list(range(10, 20))
        assert 10 == playground.get_total(sample_list)
        assert 25 == playground.get_total(list(range(1, 26)))

    def test_that_function_return_sum_of_even_numbers(self):
        sample_list = list(range(10, 20))
        assert 75 == playground.get_sum_of_even_numbers(sample_list)

    def test_that_function_return_sum_of_odd_numbers(self):
        sample_list = list(range(10, 20))
        assert 70 == playground.get_sum_of_odd(sample_list)

    def test_that_function_return_product_of_third_element(self):
        sample_list = list(range(10, 20))
        assert 3240 == playground.get_product_of_third_element(sample_list)

    def test_that_function_return_average(self):
        sample_list = list(range(10, 20))
        assert 14.5 == playground.get_average(sample_list)

    def test_that_function_return_largest_element(self):
        sample_list = list(range(10, 20))
        assert 19 == playground.get_largest_number(sample_list)

    def test_that_function_return_smallest_element(self):
        sample_list = list(range(10, 20))
        assert 10 == playground.get_smallest_number(sample_list)

    def test_that_function_returns_list_of_string(self):
        sample_list = ["hannah", "praise", "vicky", "balikis", "bolaji"]
        assert ['hannah'] == playground.get_string(sample_list)
        sample_list2 = ["hannah", "praise", "miriam", "orisha"]
        assert ['hannah', 'miriam'] == playground.get_string(sample_list2)
