import os

def listfiles(path):
    print(path)
    try:
        if os.path.isdir(path):
            for filename in os.listdir(path):
                childPath = os.path.join(path, filename)
                listfiles(childPath)
    except PermissionError as e:
        print(f"PermissionError: {e}")

if __name__ == '__main__':
    listfiles('../')
