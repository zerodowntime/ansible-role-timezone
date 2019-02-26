import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command_output(host):
    command = host.command('timedatectl status')
    assert command.stdout.find('Time zone: Europe/Warsaw') > -1
    assert command.rc == 0
