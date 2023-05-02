# Bacterial Growth Curves Database
This project is the basis of a database set up for human gut bacterial growth curves and all the information regarding the obtainance of this data. Hence, it has two main functionalities for the user:
* **Populate the database** with new experiments, providing information about the procedure and files with the final data
* **Extract information from the database** by means of a Python Command-Line Program; information will be return both in a README.txt file and in plots, depending on the user choices when running the progam.

## Previous requirements
* [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html): 

### Environment set up
First, you need to set up the environment that contain all the packages that will be used by the program. To do so, run the following commands:
````
cd envs/
conda env create -f environment.yml
````

### Running the program
The program will be run with via Command-Line instructions; it has 4 functionalities that can be investigated with the wide commonly used `--help` command:
