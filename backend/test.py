import os
import shutil


def copy_and_remap_path_texture(
    file_paths, old_folder_path, keep_texture=False, erase_texure=False
):
    dest_folder = "{}\\maps\\old\\".format(old_folder_path)
    if (
        not os.path.exists("{}\\maps\\old".format(old_folder_path))
        and erase_texure is True
    ):
        os.makedirs("{}\\maps\\old\\".format(old_folder_path))
    for file_path, value in file_paths.iteritems():

        if value["output_exist"] and keep_texture is True:
            logger.debug(
                "You choose to keep existing map copy of {} abort".format(
                    value["output_path"]
                )
            )
        elif erase_texure is True:
            logger.debug(
                "You choose to erase existing map we backup: {} in old folder".format(
                    file_path
                )
            )
            shutil.copy(value["output_path"], dest_folder)
            logger.debug("Copying: {}".format(file_path))
            logger.debug("To: {}".format(value["output_path"]))
            shutil.copyfile(file_path, value["output_path"])
        else:
            logger.debug("Copying: {}".format(file_path))
            logger.debug("To: {}".format(value["output_path"]))
            shutil.copyfile(file_path, value["output_path"])

        # We remap the import file node we the new maps
        for file_node in value["file_nodes"]:
            texture_utils.remap_file_node(file_node, value["output_path"])
