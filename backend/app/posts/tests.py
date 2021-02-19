from django.test import TestCase
from app.posts.models import Post


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(body="a body here")

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = f"{post.body}"
        self.assertEqual(expected_object_body, "a body here")


# Todo wait for CICD issue to remove harcode entrypoint
def render_hud(path_template, input_file, output_file, save_path, frame):
    """Allow to generate Hud commande to render on farm
    :param path_template: location of base template for HUD
    :type path_template: str
    :param input_file: absolute path to input frames
    :type input_file: str
    :param output_file: absolute path to output frames
    :type output_file: str
    :param save_path: absolute path where we save the template of the asset
    :type save_path: str
    :param frame: frame interval for render
    :type frame: str
    :return: the full commande to execute on farm
    :rtype:str
    """
    return "rez env nuke_bundle nuke -- nuke -t A:\package/int/nuke_bundle/0.5.1/python/nuke_bundle\cli\_entrypoint.py hud --template {} --input_file {} --output_file {} --save_path {} --render_nodes --frames={}".format(
        path_template, input_file, output_file, save_path, frame
    )


commande = render.render_hud(
    posixpath.join(*path_generic_template.split("\\")),
    posixpath.join(*path_input_img.split("\\")),
    posixpath.join(*path_output_img.split("\\")),
)
