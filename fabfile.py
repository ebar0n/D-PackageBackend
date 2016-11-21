import os

from fabric.api import cd, env, local, settings

LOCAL = any(['deploy_dev' in task for task in env.tasks])
if LOCAL:
    from fabric.api import local as run
    HOME_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
else:
    from fabric.api import run
    HOME_DIRECTORY = '/root/D-PackageBackend'
    env.user = 'root'
    env.hosts = ['api.d-packagebackend.edwarbaron.me']
    env.password = os.environ.get('SERVER_PASSWORD', None)
    if not env.password:
        env.key_filename = '~/.ssh/id_rsa.pub'

BRANCH = os.environ.get('TRAVIS_BRANCH', 'master')
DOCKER_LOGIN = 'ebar0n'
DOCKER_PASSWORD = 'python6#GuJq'


def pull(branch='master'):
    """
    Pull repostory by branch

    Args:
        branch: Name branch

    Example:
        $ fab pull:branch='master'
    """
    with cd(HOME_DIRECTORY):
        run('git fetch --all')
        run('git pull origin {}'.format(branch))
        run('git checkout {}'.format(branch))


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
    run('docker login -u {} -p {}'.format(DOCKER_LOGIN, DOCKER_PASSWORD))
    with cd(HOME_DIRECTORY):
        run('docker-compose {} build'.format(yml))
        run('docker-compose {} pull'.format(yml))


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


def deploy_production(branch='master'):
    """
    Deploy project by branch

    Args:
        branch: Name branch

    Example:
        $ fab nginx:branch='master'
    """
    local('docker login -u {} -p {}'.format(DOCKER_LOGIN, DOCKER_PASSWORD))
    with cd(HOME_DIRECTORY):
        local('docker build -t ebar0n/d-packagebackend:dev -f Dockerfile-Development .')
        local('docker push ebar0n/d-packagebackend:dev')
        local('docker build -t ebar0n/d-packagebackend:pro -f Dockerfile-Production .')
        local('docker push ebar0n/d-packagebackend:pro')
        local('docker tag ebar0n/d-packagebackend:pro ebar0n/d-packagebackend:latest'.format(BRANCH))
        local('docker push ebar0n/d-packagebackend:latest')
    deploy(branch=branch, yml='-f docker-compose-production.yml')


def test():
    """
    Test by branch

    Example:
        $ fab test
    """
    with cd(HOME_DIRECTORY):
        local('docker-compose run --rm -e TEST=true api py.test')


def ci_test():
    """
    Test by branch

    Example:
        $ fab ci_test
    """
    local('docker login -u {} -p {}'.format(DOCKER_LOGIN, DOCKER_PASSWORD))
    local('docker pull python:3.5')
    local('docker pull ebar0n/d-packagebackend:dev')
    with settings(warn_only=True):
        _exec = local('docker pull ebar0n/d-packagebackend:{}'.format(BRANCH))
        if _exec.return_code == 1:
            local('docker tag ebar0n/d-packagebackend:dev ebar0n/d-packagebackend:{}'.format(BRANCH))

    local('docker images')
    with cd(HOME_DIRECTORY):
        local('docker build -t ebar0n/d-packagebackend:{} -f Dockerfile-Development .'.format(BRANCH))
        local('docker push ebar0n/d-packagebackend:{}'.format(BRANCH))
        local('docker tag ebar0n/d-packagebackend:{} ebar0n/d-packagebackend:dev'.format(BRANCH))

    with cd(HOME_DIRECTORY):
        local('docker-compose run --rm -e TEST=true api py.test')


def enable_swap():
    """ to enable swap on a server. JIC."""
    run('dd if=/dev/zero of=/swapfile bs=1024 count=1024k')
    run('mkswap /swapfile')
    run('swapon /swapfile')
    run('swapon -s')
    run('echo 10 | sudo tee /proc/sys/vm/swappiness')
    run(('if grep -Fxq "/swapfile       none    swap    sw      0       0 " /etc/fstab > /dev/null;'
         'then echo ya tiene la linea; else echo "/swapfile       none    swap    sw      0       0 "'
         ' >> /etc/fstab; fi'))
    run('echo vm.swappiness = 10 | sudo tee -a /etc/sysctl.conf')
    run('chown root:root /swapfile')
    run('chmod 0600 /swapfile')
