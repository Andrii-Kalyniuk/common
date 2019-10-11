import pytest

from homework import Cat, Cheetah, House


@pytest.mark.parametrize("age, food, result", [
    (6, "fodder", 60),
    (6, "apple", 55),
    (6, "milk", 52),
    (6, "another_food", 50)
])
def test_cat_eat(age, food, result):
    cat = Cat(age)
    cat.eat(food)
    assert cat.get_saturation_level() == result


@pytest.mark.parametrize("age, food, result", [
    (6, "gazelle", 80),
    (6, "rabbit", 65),
    (6, "another_food", 50)
])
def test_cheetah_eat(age, food, result):
    cheetah = Cheetah(age)
    cheetah.eat(food)
    assert cheetah.get_saturation_level() == result


@pytest.mark.parametrize("age, result", [
    (1, 12),
    (7, 12),
    (9, 9),
    (10, 9),
    (12, 6)
])
def test_set_cat_average_speed(age, result):
    cat = Cat(age)
    assert cat.get_average_speed() == result


@pytest.mark.parametrize("age, result", [
    (1, 90),
    (5, 90),
    (12, 75),
    (15, 75),
    (19, 40)
])
def test_set_cheetah_average_speed(age, result):
    cheetah = Cheetah(age)
    assert cheetah.get_average_speed() == result


@pytest.mark.parametrize("age, hours, result", [
    (1, 1, 48),
    (7, 4, 45),
    (9, 10, 35),
    (10, 20, 25),
    (6, 100, "Your cat is died :(")
])
def test_cat_run(age, hours, result):
    cat = Cat(age)
    cat.run(hours)
    assert cat.get_saturation_level() == result


@pytest.mark.parametrize("age, hours, result", [
    (1, 1, 35),
    (7, 4, "Your cat is died :("),
    (16, 1, 45)
])
def test_cat_run(age, hours, result):
    cheetah = Cheetah(age)
    cheetah.run(hours)
    assert cheetah.get_saturation_level() == result


class TestHouse:

    @classmethod
    def setup_class(cls):
        cls.house = House()
        cls.house.create_wall(10, 2.5)
        cls.house.create_wall(10, 2.5)
        cls.house.create_wall(14, 2.5)
        cls.house.create_wall(14, 2.5)
        cls.house.create_roof(10, 6, "single-pitch")
        cls.house.create_door(1, 2)
        cls.house.create_window(3, 1)

    def test_get_walls_square(self):
        walls_square = self.house.get_walls_square()
        expected_res = 120  # 10 * 2.5 + 14 * 2.5 + 14 * 2.5 + 10 * 2.5

        assert walls_square == expected_res

    def test_zero_wall(self):
        with pytest.raises(ValueError):
            zero_house = House()
            zero_house.create_wall(0, 0)

    def test_get_count_of_walls(self):
        walls_count = self.house.get_count_of_walls()
        expected_res = 4

        assert walls_count == expected_res

    def test_create_extra_wall(self):
        with pytest.raises(ValueError):
            self.house.create_wall(10, 20)

    def test_get_count_of_windows(self):
        windows_count = self.house.get_count_of_windows()
        expected_res = 1

        assert windows_count == expected_res

    @pytest.mark.parametrize("material, result, update_value, updated_result", [
        ("wood", 20, 20, 40),
        ("metal", 6, 6, 12)
    ])
    def test_count_door_price(self, material, result, update_value, updated_result):
        actual_res = self.house.get_door_price(material)
        assert actual_res == result

        if material == "wood":
            self.house.update_wood_price(update_value)
        if material == "metal":
            self.house.update_metal_price(update_value)

        actual_res = self.house.get_door_price(material)
        assert actual_res == updated_result

    def test_get_roof_square(self):
        actual_res = self.house.get_roof_square()
        expected_res = 60
        assert actual_res == expected_res

        house_with_other_roof = House()
        house_with_other_roof.create_roof(10, 6, "gable")
        actual_res = house_with_other_roof.get_roof_square()
        expected_res = 120
        assert actual_res == expected_res

    def test_get_windows_square(self):
        actual_res = self.house.get_windows_square()
        expected_res = 3

        assert actual_res == expected_res

    def test_get_door_square(self):
        actual_res = self.house.get_door_square()
        expected_res = 2

        assert actual_res == expected_res

    def test_get_number_of_rolls_of_wallpapers(self):
        actual_res = self.house.get_number_of_rolls_of_wallpapers(0.53, 10)
        expected_res = 22

        assert actual_res == expected_res

    def test_zero_length_wallpaper(self):
        with pytest.raises(ValueError):
            self.house.get_number_of_rolls_of_wallpapers(0, 0)

    def test_get_room_square(self):
        actual_res = self.house.get_room_square()
        expected_res = 115

        assert actual_res == expected_res
