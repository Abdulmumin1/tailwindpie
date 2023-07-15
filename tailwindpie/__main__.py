__version__ = '0.1.0'
__author__ = 'abdulmumin abdulkarim'

import argparse
from .main import CreateEnv

App = CreateEnv()


def create():
    App.create_package_dot_json()

    App.install_packages()
    App.activate_tailwind()
    App.create_input_css()
    App.add_content_template_to_tailwind()
    App.add_node_and_stuff_to_gitignore()
    App.print_next_step()


def build():
    App.build_tailwind()


def parge():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Example argparse with multiple commands")

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # Command for function1
    parser_function1 = subparsers.add_parser(
        "config", help="Configure tailwind")
    parser_function1.set_defaults(func=create)

    # Command for function2
    parser_function2 = subparsers.add_parser("build", help="Build CSS")
    parser_function2.set_defaults(func=build)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command:
        args.func()
    else:
        # Show help if no command is provided
        parser.print_help()


if __name__ == '__main__':
    parge()
