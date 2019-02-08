import csv
import os

from create_template import render_template


def template_from_csv(csv_path):
    """Generate files for all robot listed in csv. All parameter taken from csv"""
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), csv_path)
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)

        # check mandatory fields
        assert (('template_filename' in headers)
                & ('robot_name' in headers)
                & ('project_name' in headers)), 'Wrong CSV structure!'

        for r in reader:
            metadata = dict(zip(headers, r))

            if not os.path.exists(metadata['project_name']):
                os.makedirs(metadata['project_name'])

            # TODO: Don't know on what level extension should be passed
            metadata['robot_name'] = metadata['robot_name'] + '.py'

            # VIP line
            render_template(metadata['template_filename'],
                            os.path.join(metadata['project_name'], metadata['robot_name']),
                            metadata)


if __name__ == '__main__':
    template_from_csv('input.csv')
