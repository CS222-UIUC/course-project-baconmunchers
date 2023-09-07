import unittest
from .build_database import get_sections_from_class

#WARNING: They still seem to be updating the course explorer. If a test case fails, make sure that it is not because the course explorer page has changed!

class TestStringMethods(unittest.TestCase):

    def test_cs_222(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/CS/222'),
            [
                ['CS', '222', '71617', '01:00PM', '01:50PM', 'W', 'Electrical & Computer Eng Bldg', '1002'],
            ]
        )

    def test_macs_100(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/MACS/100'),
            [
                ['MACS', '100', '63465', '09:00AM', '09:50AM', 'R', 'Gregory Hall', '329'],
                ['MACS', '100', '63466', '10:00AM', '10:50AM', 'R', 'Gregory Hall', '313'],
                ['MACS', '100', '63467', '11:00AM', '11:50AM', 'R', 'Gregory Hall', '327'],
                ['MACS', '100', '63472', '01:00PM', '01:50PM', 'R', 'Gregory Hall', '313'],
                ['MACS', '100', '63473', '02:00PM', '02:50PM', 'R', 'Gregory Hall', '313'],
                ['MACS', '100', '63474', '03:00PM', '03:50PM', 'R', 'Gregory Hall', '313'],
                ['MACS', '100', '63835', '10:00AM', '10:50AM', 'F', 'Gregory Hall', '327'],
                ['MACS', '100', '63836', '11:00AM', '11:50AM', 'F', 'Gregory Hall', '327'],
                ['MACS', '100', '63837', '12:00PM', '12:50PM', 'F', 'Gregory Hall', '327'],
            ]
        )

    def test_chem_101(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/CHEM/101'),
            [
                ['CHEM', '101', '59948', '09:00AM', '09:50AM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59948', '08:00AM', '09:50AM', 'M', 'Noyes Laboratory', '204'],

                ['CHEM', '101', '59951', '12:00PM', '12:50PM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59951', '10:00AM', '11:50AM', 'M', 'Noyes Laboratory', '204'],

                ['CHEM', '101', '59953', '08:00AM', '08:50AM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59953', '12:00PM', '01:50PM', 'M', 'Noyes Laboratory', '204'],

                ['CHEM', '101', '59954', '10:00AM', '10:50AM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59954', '02:00PM', '03:50PM', 'M', 'Noyes Laboratory', '203'],

                ['CHEM', '101', '59955', '02:00PM', '02:50PM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59955', '02:00PM', '03:50PM', 'M', 'Noyes Laboratory', '204'],

                ['CHEM', '101', '59956', '01:00PM', '01:50PM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59956', '04:00PM', '05:50PM', 'M', 'Noyes Laboratory', '204'],

                ['CHEM', '101', '59957', '11:00AM', '11:50AM', 'F', 'Noyes Laboratory', '304'],
                ['CHEM', '101', '59957', '04:00PM', '05:50PM', 'M', 'Noyes Laboratory', '203'],

                ['CHEM', '101', '59958', '01:00PM', '01:50PM', 'TR', 'Noyes Laboratory', '100'],
            ]
        )

    def test_law_694(self):
        # Tests if "Location Pending" sections are ignored
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/LAW/694'),
            []
        )

    def test_cs_447(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/CS/447'),
            [
                ['CS', '447', '74372', '02:00PM', '03:15PM', 'WF', 'Siebel Center for Comp Sci', '1404'],
                ['CS', '447', '74373', '02:00PM', '03:15PM', 'WF', 'Siebel Center for Comp Sci', '1404']
            ]
        )

    def test_zulu_202(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/ZULU/202'),
            []
        )

    def test_aas_539(self):
        self.assertEqual(
            get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/AAS/539'),
            [
                ['AAS', '539', '65078', '02:00PM', '04:50PM', 'W', 'Davenport Hall', '312'],
            ]
        )


if __name__ == '__main__':
    unittest.main()
