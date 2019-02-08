import os
import unittest
from filecmp import cmp

from create_template import render_template


class TestRenderTemplate(unittest.TestCase):

    def setUp(self):
        self.template_to_use = 'json_robot_template'
        self.o_file = 'gdf_amazon.py'
        self.robot_metadata = {
            'project_name': 'gdf_big_fish',
            'robot_name': 'gdf_amazon',
            'url': 'https://www.amazon.com/'
        }
        render_template(self.template_to_use, self.o_file, self.robot_metadata)

    def test_output(self):
        self.assertTrue(cmp('./' + self.o_file, './json_robot_desired_output.py'))

    def tearDown(self):
        os.remove('./' + self.o_file)


if __name__ == '__main__':
    unittest.main()
