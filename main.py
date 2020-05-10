import sys
import ui

from flux import ViewController


def main(*args):
    vc = ViewController()
    vc.view.present()
    print('ok')


if __name__ == '__main__':
    main(sys.argv)
