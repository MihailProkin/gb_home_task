import os

folder_struct = {
    'my_project': [{
        'settings': [{'bar': [], 'foo': []}],
        'mainapp': [],
        'adminapp': [],
        'authapp': []
    }]
}


def project_started(pth, struct):
    for hold_node, ch_node in struct.items():
        test_path = os.path.join(pth, hold_node)

        if not os.path.exists(test_path):
            os.mkdir(test_path)
        if len(ch_node) > 0:
            for node in ch_node:
                project_started(test_path, node)


if __name__ == '__main__':

    project_started(os.getcwd(), struct=folder_struct)
    