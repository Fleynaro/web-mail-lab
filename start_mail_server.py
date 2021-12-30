import sys
sys.path.append('./mail')

from server import app, run

if __name__ == '__main__':
    run()

__all__ = ['app', 'run']