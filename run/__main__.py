from source.WorkWithProject import WorkWithProject

def main():
    rootFolderProjectPath = input("Ingresar ruta del proyecto: ")
    currentProject = WorkWithProject(rootFolderProjectPath)
    currentProject.work()
    
if __name__ == "__main__":
    main()