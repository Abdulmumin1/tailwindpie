from rich.spinner import Spinner
import argparse
import subprocess
import os
import json
from rich.console import Console
# # Run a simple command and capture the output
# result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
# print(result.stdout)

# # Run a command with arguments
# subprocess.run(['echo', 'Hello, World!'])

# # Run a command and check the return code
# result = subprocess.run(['git', 'status'])
# if result.returncode == 0:
#     print("Git status command executed successfully.")
# else:
#     print("Git status command failed.")

# # Run a command and capture both stdout and stderr
# result = subprocess.run(['ls', 'nonexistent_file'], capture_output=True, text=True)
# print(result.stdout)
# print(result.stderr)


class CreateEnv():
    console = Console()

    def create_env(self):
        print('npm init .......')
        result = subprocess.run(['npm', 'init'])
        # print("Created Venv")

    def install_packages(self):
        self.console.print("\n[bold]npm [green]install[/] tailwindcss[/]")
        # activate_cmd = f'source venv/bin/activate'
        subprocess.run(['npm', 'install', '-D', 'tailwindcss'])

    def activate_tailwind(self):
        self.console.print('\nnpx tailwindcss init', style='bold')
        subprocess.run(['npx', 'tailwindcss', 'init'])

    def create_input_css(self):
        with open('input.css', 'w') as tailwindinput:
            tailwindinput.write(
                "@tailwind base;\n@tailwind components;\n@tailwind utilities;")

    def create_package_dot_json(self):
        self.console.print('Initializing ..\n', style='bold cyan')
        scripts = {
            'scripts': {

                'build_tailwind': "npx tailwindcss -i ./input.css -o YOUR_CSS_FOLDER/tailwind.css --watch"
            }
        }
        with open('package.json', 'w') as packagejson:
            json.dump(scripts, packagejson, indent=2)

    def add_node_and_stuff_to_gitignore(self):

        try:
            self.write_gitignore_stuff('a')
        except:
            self.write_gitignore_stuff('w')

    def write_gitignore_stuff(self, method):
        with open('.gitignore', 'a') as gitignore:
            gitignore.write('\nnode_modules/\npackage.json\npackage-lock.json')

    def build_tailwind(self):
        subprocess.run(['npm', 'run', 'build_tailwind'])

    def add_content_template_to_tailwind(self):
        # Straight from ChatGPT
        filename = 'tailwind.config.js'

        # Read the file content
        with open(filename, 'r') as file:
            file_content = file.readlines()

        # Find the line with 'content: []'
        for i, line in enumerate(file_content):
            if 'content: []' in line:
                # Add the new content to the line
                file_content[i] = line.replace(
                    'content: []', "content: ['./YOUR-HTML-FILES-FOLDER-PATH/**/*.{html,js}']")

        # Write the modified content back to the file
        with open(filename, 'w') as file:
            file.writelines(file_content)

        print(f"\nContent added to '{filename}' successfully.")

    def print_next_step(self):
        self.console.print('\nNext Steps:', style='bold cyan')
        self.console.print(
            '\tEdit [cyan italic]package.json[/], [cyan italic]tailwind.config.js[/]')
        print('\tLink the path to your CSS to HTML!')
# App = CreateEnv()


# def create():
#     App.create_package_dot_json()

#     App.install_packages()
#     App.activate_tailwind()
#     App.create_input_css()
#     App.add_content_template_to_tailwind()
#     App.add_node_and_stuff_to_gitignore()


# def build():
#     App.build_tailwind()


# # Create the parser
# parser = argparse.ArgumentParser(
#     description="Example argparse with multiple commands")

# # Create subparsers for different commands
# subparsers = parser.add_subparsers(title="Commands", dest="command")

# # Command for function1
# parser_function1 = subparsers.add_parser("config", help="Configure tailwind")
# parser_function1.set_defaults(func=create)

# # Command for function2
# parser_function2 = subparsers.add_parser("build", help="Build CSS")
# parser_function2.set_defaults(func=build)

# # Parse the command-line arguments
# args = parser.parse_args()

# # Call the appropriate function based on the command
# if args.command:
#     args.func()
# else:
#     # Show help if no command is provided
#     parser.print_help()


# App = CreateEnv()
# # App.create_env()
# App.create_package_dot_json()
# App.install_packages()
# App.activate_tailwind()
# # App.create_input_css()
# # App.add_node_and_stuff_to_gitignore()
# # App.add_content_template_to_tailwind()
# # App.build_tailwind()
# App.print_next_step()
# App.spinner()
