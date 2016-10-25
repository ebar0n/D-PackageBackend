import os

from fabric.api import cd, env, hosts, local

LOCAL = any(['deploy_dev' in task for task in env.tasks])
if LOCAL:
    from fabric.api import local as run
    HOME_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
else:
    from fabric.api import run
    HOME_DIRECTORY = '/root/D-PackageBackend'
    env.user = 'root'
    env.password = os.environ.get('PASSWORD', None)
    if not env.password:
        env.key_filename = '~/.ssh/id_rsa.pub'


def pull(branch='master'):
    """
    Pull repostory by branch

    Args:
        branch: Name branch

    Example:
        $ fab pull:branch='master'
    """
    with cd(HOME_DIRECTORY):
        run('git checkout .')
        run('git fetch --all')
        run('git checkout {}'.format(branch))
        run('git pull origin {}'.format(branch))


def build(branch='master', yml=''):
    """
    Build by branch

    Args:
        branch: Name branch
        container: Name container
        yml: File docker-compose.yml

    Example:
        $ fab build:branch='master'
    """
    if not LOCAL:
        pull(branch=branch)
    with cd(HOME_DIRECTORY):
        run('docker-compose {} build'.format(yml))


def load(branch='master', yml=''):
    """
    Load by branch

    Args:
        branch: Name branch
        yml: File docker-compose.yml

    Example:
        $ fab load

        Perform deployment
        $ fab load:branch='master',yml=''
    """
    build(branch=branch, yml=yml)
    with cd(HOME_DIRECTORY):
        commands = [
            'api python manage.py migrate --noinput',
            'api python manage.py collectstatic --noinput',
            'api python manage.py compilemessages',
        ]
        run('docker-compose up -d postgres')
        for command in commands:
            run('docker-compose run --rm {}'.format(command))


def deploy(branch='master', yml=''):
    """
    Deploy by branch

    Args:
        branch: Name branch
        yml: File docker-compose.yml

    Example:
        $ fab deploy

        Perform deployment
        $ fab deploy:branch='master',yml=''
    """
    with cd(HOME_DIRECTORY):
        run('docker-compose {} down'.format(yml))
    load(branch=branch, yml=yml)
    with cd(HOME_DIRECTORY):
        run('docker-compose {} up -d'.format(yml))


def deploy_dev():
    """
    Deploy project

    Example:
        $ fab deploy_dev
    """
    deploy()


@hosts('voluntario180.com')
def deploy_production(branch='master'):
    """
    Deploy project by branch

    Args:
        branch: Name branch

    Example:
        $ fab nginx:branch='master'
    """
    deploy(branch=branch, yml='-f docker-compose-production.yml')


def test():
    """
    Test by branch

    Example:
        $ fab test
    """
    with cd(HOME_DIRECTORY):
        local('docker-compose run --rm -e TEST=true api py.test')
