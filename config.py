import os
from strange_case.strange_case_config import CONFIG
from strange_case.registry import Registry
from strange_case.extensions.configurator_title_from_name import titlecase


def project_title(CONFIG):
    if CONFIG.get('project', None) is None:
        import sys
        sys.stderr.write("Usage:\n    scase project:name [desc:description]\n\n'project' is required\n")
        sys.exit(1)

    CONFIG['project'] = CONFIG['project'].replace('-', '_')
    CONFIG['Project'] = titlecase(CONFIG['project'])
    CONFIG['ProJect'] = CONFIG['Project'].replace(' ', '')
    CONFIG['deploy_path'] = os.path.abspath(os.path.dirname(__file__) + '/../' + CONFIG['ProJect'])

CONFIG['config_hook'] = project_title
CONFIG['len'] = len
CONFIG['deploy_path'] = 'ignore'

Registry.associate('page', '*.*')
