import logging
from os import remove

logging.basicConfig(
    format=(
        '%(asctime)s - %(name)s:%(levelname)s - %(filename)s:%(lineno)d'
        '- %(message)s'
    ),
    level=logging.INFO,
)
logger = logging.getLogger('kill')


def kill_server(pid_file):
    try:
        with open(pid_file) as fp:
            pid = int(fp.read())
    except (OSError, ValueError) as err:
        logger.error('%r: cannot get pid - %s', pid_file, err)
        raise

    logger.info('killing %s', pid)
    # TODO: Actual kill

    try:
        remove(pid_file)
    except OSError as err:
        logger.warning('cannot delete %r - %s', pid_file, err)


if __name__ == '__main__':
    kill_server('Ch06/06_04/app.pid')
