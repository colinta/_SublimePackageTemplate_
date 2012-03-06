from strange_case.strange_case_config import CONFIG
from strange_case.configurators import titlecase


def project_title(CONFIG):
    assert CONFIG.get('project', None), "'project' is required"

    if 'Project' not in CONFIG:
        CONFIG['Project'] = titlecase(CONFIG['project'])

CONFIG['config_hook'] = project_title
CONFIG['len'] = len
