import re

global PROJECT_DIRECTORY
global LOCAL_DIRECTORY

global EXPERIMENT_ANALYSIS_FILE
global MEDIA_ANALYSIS_FILE
global HEADERS_FILE
global EXPERIMENTS_LIST
global MEDIA_LIST

global od_regex
global counts_regex
global qpcr_regex
global rnaseq_regex

global abundance_options

# This directory MUST BE the one where the core is in the server
PROJECT_DIRECTORY = '/Users/julia/bacterialGrowth_thesis/'
LOCAL_DIRECTORY = '/Users/julia/Desktop/local_thesis_files/'
# Bash files needed to run the code
EXPERIMENT_ANALYSIS_FILE = 'src/bash_scripts/Lab_files_analysis2.sh'
MEDIA_ANALYSIS_FILE = 'src/bash_scripts/media_file_analysis.sh'
MODIFY_YML_FILE = 'src/bash_scripts/modify_yml_files.sh'

# Files generated by the bash needed in the code
HEADERS_FILE = 'IntermediateFiles/lab_headers.txt'
EXPERIMENTS_LIST = 'IntermediateFiles/listOfFiles.list'
MEDIA_LIST = 'IntermediateFiles/listOfMedia.list'

# File types
file_types = ['abundanceFile', 'metabolitesFile', 'phFile']

# Abundance options
abundance_options = ['od', 'counts', 'qpcr', 'rnaseq']

# Regex options
abundance_regex = re.compile(r'.*time.* | .*liquid.* | .*active.* | .*OD.*', flags=re.I | re.X)
# abundance_regex = re.compile(r'time | liquid | active | OD', flags=re.I | re.X)
ph_regex = re.compile(r'.*time.* | .*ph.*', flags=re.I | re.X)
od_regex = re.compile(r'.*time.* | .*OD.*', flags=re.I | re.X)
counts_regex = re.compile(r'.*time.* | .*count.*', flags=re.I | re.X)
qpcr_regex = re.compile(r'.*time.* | .*qpcr.*', flags=re.I | re.X)
rnaseq_regex = re.compile(r'.*time.* | .*rna.*', flags=re.I | re.X)

exp_metadata_fields = ['plateId', 'plateColumn', 'plateRow', 'initialPh', 'initialTemperature', 'inoculumConcentration', 'inoculumVolume', 'carbonSource', 'antibiotic']
pert_metadata_fields = ['property', 'newValue', 'startTime', 'endTime']

