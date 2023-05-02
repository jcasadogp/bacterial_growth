# Bacterial Growth Curves Database
This project is the basis of a database set up for human gut bacterial growth curves and all the information regarding the obtainance of this data. Hence, it has two main functionalities for the user:
* **Populate the database** with new experiments, providing information about the procedure and files with the final data
* **Extract information from the database** by means of a Python Command-Line Program; information will be return both in a README.txt file and in plots, depending on the user choices when running the progam.

------
Be aware of the hierarchy between studies, biological replicates and perturbations!
------

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
#### (1) Create Information File (`createInfoFile`)
This is the first step needed for populating the database. The positional argument `createInfoFile` will be followed by optional arguments with which the user will indicate the amount of studies (`--num_studies`, `-s`. 0 or 1), biological replicates (`--num_biological_replicates`, `-br`. 0 up to N), perturbations (`--num_perturbations`, `-p`. 0 up to N) that will be introuced in the database. In case of 0, you can omit the optional argument.
If you want to add, i.e., a new perturbation into an existing biological (and thus, the study already exists too), just use the `--num_perturbations`or `-p`; the program will ask you for the remaining information.
Some command examples are listed below:
```
python3 main.py createInfoFile --num_studies 1 --num_biological_replicates 1 --num_perturbations 1
python3 main.py createInfoFile --num_studies 1 --num_biological_replicates 1
python3 main.py createInfoFile --num_biological_replicates 1 --num_perturbations 1
python3 main.py createInfoFile --num_perturbations 2
```
The program will then generate a YML file and ave it in your local computer. You will need to fill in this file with the information you want to place into the DB and pass it, in the next step, to the program.

#### (2) Populate the Database (`populateDB`)
This is the second and last step needed for populating the database. The positional argument `populateDB`will be follow by one single argument, `--info_file`, where you will indicate the path of the YML file you filled in previously.
Some command examples are listed below:
```
python3 main.py populateDB --info_file /yml_files/study_information.yml
python3 main.py populateDB --info_file /yml_files/perturbation_information.yml
```
#### (3) Get information from the database (`getResultsFile`)
This command will extract information from the database and place in in the user's local directory.
First, this argument can be followed by two optional arguments, `--bacteria` and `--metabolites`:
* `--bacteria` receives a comma separated list of bacteria species. The program will return all the studies that have been done with that (combination of) bacteria(s). For example:
`python3 main.py getResultsFile --bacteria Bacteroides thetaiotaomicron`
* `--metabolites`. This command can be kept empty, meaning that all the studies in which metabolites were measured will be returned, or be followed by a comma separated list of metabolites. The program will return all the studies that have been done with that (combination of) metabolites(s). For example:
`python3 main.py getResultsFile --metabolites Glucose, Fructose`

This two optional arguments can be passed together:
`python3 main.py getResultsFile --metabolites Glucose --bacteria Bacteroides thetaiotaomicron`

#### (4) Plot Information from the Database (`plot`)
This option will retrieve plots of the information indicated by the user. When this command is run, the user will receive the following message with several plotting options and will wait for the user input:
```
Choose the plotting option:
	1: Plot one technical replicate.
	2: Plot mean and deviation from several replicates from the same perturbation/biological replicate.
	3: Plot mean and deviation from several replicates from one biological replicate (with all its perturbations).
Option: __
```
Once the user has picked up one option, the program will display tables with the existing studies, biological replicates and perturbations for the user to choose what to plot.

- Option 1:
<img src="https://user-images.githubusercontent.com/80517901/235652313-b20ce96a-824c-4289-be76-6c38a58e0dc2.png" width="48">
- Option 2:
<img src="https://user-images.githubusercontent.com/80517901/235652359-5bec7390-58ba-48d3-9e51-16c72cc33502.png" width="48">
- Option 3:
<img src="https://user-images.githubusercontent.com/80517901/235652402-eaa5c2c6-c3c5-4b6a-aac7-30f036611652.png" width="48">

