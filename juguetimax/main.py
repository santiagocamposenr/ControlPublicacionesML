import subprocess

def main():
    subprocess.run(['python', 'GenerarIDs.py'], cwd='./Todas')
    subprocess.run(['python', 'update_sheets_classification.py'], cwd='./Todas')
    subprocess.run(['rm', '-r', '__pycache__'], cwd='./Todas')


if __name__ == '__main__':
    main()