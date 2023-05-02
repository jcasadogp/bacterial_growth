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
The user will always interact directly with the `main.py` file via Command-Line instructions; it has 4 functionalities that can be investigated with the wide commonly used `--help` command:
```
python3 main.py --help
```
We will then obtain the 4 possible positional arguments that the code is receiving:
```
createInfoFile      Create the YML that the user will fill in to put data into the database
populateDB          Pass the YML file to create the database
getResultsFile      Pass the YML file to create the database
plot                Plot data that is in the database
```
#### Create Information File (`createInfoFile`)
This is the first step needed for populating the database. The positional argument `createInfoFile` will be followed by optional arguments with which the user will indicate the amount of studies (`--num_studies`, `-s`. 0 or 1), biological replicates (`--num_biological_replicates`, `-br`. 0 up to N), perturbations (`--num_perturbations`, `-p`. 0 up to N) that will be introuced in the database. In case of 0, you can omit the optional argument.
If you want to add, i.e., a new perturbation into an existing biological (and thus, the study already exists too), just use the `--num_perturbations`or `-p`; the program will ask you for the remaining information.
Some command examples are listed below:
```
python3 main.py createInfoFile --num_studies 1 --num_biological_replicates 1 --num_perturbations 1
python3 main.py createInfoFile --num_studies 1 --num_biological_replicates 1
python3 main.py createInfoFile --num_biological_replicates 1 --num_perturbations 1
python3 main.py createInfoFile --num_perturbations 2
```


Be aware of the hierarchy between studies, biological replicates and perturbations!
