import os
from jinja2 import Environment, FileSystemLoader
# TODO: Should this be created in OOP as TemplateCreator class?

# TODO: Where to put this?
TEMPLATE_ENV = Environment(
    autoescape=False,
    # location of the templates
    loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')),
    trim_blocks=False)


def render_template(template_filename, filename, context):

    # files will be generated in the dir where scrip was called
    o_f_path = os.path.join(os.getcwd(), filename)

    # TODO: When called many times how to bubble up the error that some files was skipped, without stopping the script?
    assert not os.path.isfile(o_f_path), f"File { filename } already exist"

    try:
        with open(o_f_path, 'w') as f:
            # VIP line
            output = TEMPLATE_ENV.get_template(template_filename).render(context)
            f.write(output)
    except:
        # TODO: How to clean up when failed?
        os.remove(o_f_path)
        raise


if __name__ == '__main__':
    template_to_use = 'json_robot_template'
    o_file = 'gdf_amazon.py'
    robot_metadata = {
        'project_name': 'gdf_big_fish',
        'robot_name': 'gdf_amazon',
        'url': 'https://www.amazon.com/'
    }
    render_template(template_to_use, o_file, robot_metadata)
