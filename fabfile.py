#!/usr/bin/python3
from fabric.api import run, env, roles, put, local

env.user = 'ubuntu'
env.hosts = ['35.174.204.154', '100.24.236.72']

# def host_type():
#     run('mkdir -p /tmp/fabric')
#     run('echo "Hello, Fabric!" > /tmp/fabric/hello.txt')
#     run('cd /tmp/fabric && ls -l && cat hello.txt')
#     run('rm -rf /tmp/fabric')

#roles in fabric module
env.roledefs = {
    'web': ['ubuntu@35.174.204.154'],
    'web2': ['ubuntu@100.24.236.72']
}

@roles('web')
def task1():
    run('ls -l /tmp')

@roles('web2')
def task2():
    run('ls -l')

def copy():
    put('fabfile.py', '/tmp/fabfile.py')


# local use of fabric
def local_def():
    local('cd ~/AirBnB_clone_v2 && ls -al')
    run('echo "done"')