from celery.utils.log import get_task_logger

from celery_worker import app
from conf import settings
from tasks.base import AnsibleTask
from worker.commons import run_ansible

SHELL_SCRIPT = settings['sh_path'] + '/cmdb-agent.sh'

logger = get_task_logger(__name__)


@app.task(base=AnsibleTask)
def start(host):
    cmdstr = SHELL_SCRIPT + ' ' + 'start'
    res = run_ansible(cmdstr, host, become=False, become_user=None)
    return res


@app.task(base=AnsibleTask)
def status(host):
    logger.info('status {} '.format(host))
    cmdstr = SHELL_SCRIPT + ' ' + 'status'
    res = run_ansible(cmdstr, host, become=False, become_user=None)
    return res


@app.task(base=AnsibleTask)
def refresh(host):
    cmdstr = SHELL_SCRIPT + ' ' + 'refresh'
    res = run_ansible(cmdstr, host, become=False, become_user=None)
    return res


@app.task(base=AnsibleTask)
def restart(host):
    cmdstr = SHELL_SCRIPT + ' ' + 'restart'
    res = run_ansible(cmdstr, host, become=False, become_user=None)
    return res


@app.task(base=AnsibleTask)
def stop(host):
    cmdstr = SHELL_SCRIPT + ' ' + 'stop'
    res = run_ansible(cmdstr, host, become=False, become_user=None)
    return res
