from unittest import TestCase
import Ships


class TestShip(TestCase):
    def test_attack_us_attacks_them_within_range(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 30
        expected_range = 5
        expected_attack_power = 20

        # act
        us_ship = Ships.Ship(exptected_name, expected_x, expected_y,
                             starting_alignment, expected_max_health, expected_range,
                             expected_attack_power)

        them_ship = Ships.Ship(exptected_name, expected_x, expected_y,
                                   Ships.Alignment.Them, expected_max_health, expected_range,
                                   expected_attack_power)

        us_ship.attack(them_ship)

        self.assertEqual(expected_current_health, them_ship.current_health)



    def test_get_type(self):
        with self.assertRaises(NotImplementedError):
            # arrange
            exptected_name = "Some Name"
            expected_x = 10
            expected_y = 20
            expected_alignment = Ships.Alignment.Us
            expected_max_health = 50
            expected_current_health = 50
            expected_range = 5
            expected_attack_power = 20

            # act
            ship = Ships.Ship(exptected_name, expected_x, expected_y,
                              expected_alignment, expected_max_health, expected_range,
                              expected_attack_power)

            # assert
            ship.get_type()

    def test_get_x(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        expected_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          expected_alignment, expected_max_health, expected_range,
                          expected_attack_power)

        # assert
        self.assertEqual(expected_x, ship.get_x())

    def test_get_y(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        expected_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          expected_alignment, expected_max_health, expected_range,
                          expected_attack_power)

        # assert
        self.assertEqual(expected_y, ship.get_y())

    def test_get_alignment(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        expected_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          expected_alignment, expected_max_health, expected_range,
                          expected_attack_power)

        # assert
        self.assertEqual(expected_alignment, ship.get_alignment())

    def test_status(self):
        with self.assertRaises(NotImplementedError):
            # arrange
            exptected_name = "Some Name"
            expected_x = 10
            expected_y = 20
            expected_alignment = Ships.Alignment.Us
            expected_max_health = 50
            expected_current_health = 50
            expected_range = 5
            expected_attack_power = 20

            # act
            ship = Ships.Ship(exptected_name, expected_x, expected_y,
                              expected_alignment, expected_max_health, expected_range,
                              expected_attack_power)

            # assert
            # expect this to fail on get_type()
            ship.status()

    def test_move(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        expected_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 49
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          expected_alignment, expected_max_health, expected_range,
                          expected_attack_power)

        ship.current_health -= 2
        ship.move()

        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_current_health, ship.current_health)

    def test_change_alignment_us_to_them(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Us
        expected_alignment = Ships.Alignment.Them
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)
        ship.change_alignment()

        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_alignment, ship.get_alignment())

    def test_change_alignment_them_to_us(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Them
        expected_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)
        ship.change_alignment()

        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_alignment, ship.get_alignment())

    def test_change_alignment_choatic_doesnt_change(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Chaotic
        expected_alignment = Ships.Alignment.Chaotic
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)
        ship.change_alignment()

        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_alignment, ship.get_alignment())

    def test_assess_damage_doesnt_go_below_0(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 0
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)
        ship.assess_damage(expected_max_health * 2)
        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_current_health, ship.current_health)

    def test_assess_damage_doesnt_go_above_max(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)
        ship.assess_damage(-100)
        # assert
        # expect this to fail on get_type()
        self.assertEqual(expected_current_health, ship.current_health)

    def test__should_attack_us_doesnt_attack_us(self):
        # arrange
        exptected_name = "Some Name"
        expected_x = 10
        expected_y = 20
        starting_alignment = Ships.Alignment.Us
        expected_max_health = 50
        expected_current_health = 50
        expected_range = 5
        expected_attack_power = 20

        # act
        us_ship = Ships.Ship(exptected_name, expected_x, expected_y,
                          starting_alignment, expected_max_health, expected_range,
                          expected_attack_power)

        other_us_ship = Ships.Ship(exptected_name, expected_x, expected_y,
                             starting_alignment, expected_max_health, expected_range,
                             expected_attack_power)

        self.assertFalse(us_ship._should_attack(other_us_ship))
