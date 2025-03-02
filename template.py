import  os
from pathlib import Path

package_name="Demo" # porjectname

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_trasformation.py",
    f"src/{package_name}/compoments/model_trainer.py"
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utlis/__init__.py",
    "notebook/research.ipynb",
    "notebook/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh"
]
# here will create a directory
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    ''' how exist_ok works: if "directory" already exists,
    os.makedirs() will not raise error , and it will do nothing .
    If "my_directory" doesn't exist,it will create the directory .
    '''
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass 
    else:
        print("file already exists")
# here will use the file handling