# add parent directory to path
import sys
import pathlib
parent_dir = pathlib.Path().resolve()
sys.path.append(str(parent_dir))

from server import app, run


if __name__ == '__main__':
    run()

__all__ = ['app', 'run']