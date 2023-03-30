DROP DATABASE BacterialGrowth;
CREATE DATABASE BacterialGrowth;
USE BacterialGrowth;

CREATE TABLE IF NOT EXISTS Study (
	studyId INT AUTO_INCREMENT,
    studyDescription TEXT DEFAULT NULL,
    PRIMARY KEY (studyId)
);

CREATE TABLE IF NOT EXISTS Precultivation (
	precultivationId INT AUTO_INCREMENT,
    precultivationDescription TEXT,
    PRIMARY KEY (precultivationId)
);

CREATE TABLE IF NOT EXISTS Reactor (
	reactorId INT AUTO_INCREMENT,
    reactorName TINYTEXT NOT NULL,
    volume FLOAT DEFAULT 0,
    atmosphere FLOAT DEFAULT 0,
    stirring_speed FLOAT DEFAULT 0,
    reactorMode VARCHAR(50) DEFAULT '', #chemostat, batch, fed-batch,
    reactorDescription TEXT,
    PRIMARY KEY (reactorId)
);

CREATE TABLE IF NOT EXISTS Bacteria (
	bacteriaId INT NOT NULL UNIQUE,
    bacteriaGenus VARCHAR(100) DEFAULT '',
	bacteriaSpecies VARCHAR(100),
	bacteriaStrain VARCHAR(100),
    PRIMARY KEY (bacteriaSpecies, bacteriaStrain)
);

CREATE TABLE IF NOT EXISTS Media (
    mediaId INT NOT NULL UNIQUE,
    mediaName VARCHAR(20),
    mediaFile VARCHAR(100),
    PRIMARY KEY (mediaName)
);

CREATE TABLE IF NOT EXISTS Experiment (
	experimentId INT AUTO_INCREMENT,
    studyId INT NOT NULL,
    precultivationId INT,
    reactorId INT NOT NULL,
    plateId INT DEFAULT NULL,
    plateColumn INT DEFAULT NULL,
    plateRow VARCHAR(2) DEFAULT NULL,
    mediaId INT NOT NULL,
    blank BOOLEAN DEFAULT FALSE,
    inoculumConcentration INT DEFAULT 0,
	inoculumVolume INT DEFAULT 0,
    initialPh FLOAT DEFAULT NULL,
    initialTemperature FLOAT DEFAULT NULL,
    carbonSource BOOLEAN DEFAULT FALSE,
    antibiotic VARCHAR(100) DEFAULT NULL,
    experimentDescription TEXT,
    PRIMARY KEY (experimentId),
    FOREIGN KEY (studyId) REFERENCES Study (studyId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (precultivationId) REFERENCES Precultivation (precultivationId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (reactorId) REFERENCES Reactor (reactorId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (mediaId) REFERENCES Media (mediaId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Perturbation (
	perturbationId VARCHAR(15),
    experimentId INT NOT NULL,
    property VARCHAR(20),
    newValue VARCHAR(20),
    startTime INT,
    endTime INT DEFAULT NULL,
    perturbationDescription TEXT,
    PRIMARY KEY (perturbationId),
    FOREIGN KEY (experimentId) REFERENCES Experiment (experimentId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS TechnicalReplicate (
	replicateId VARCHAR(15),
    experimentId INT,
    perturbationId VARCHAR(15) DEFAULT 0,
    abundanceFile VARCHAR(100),
    metabolitesFile VARCHAR(100),
    phFile VARCHAR(100),
    PRIMARY KEY (replicateId),
    FOREIGN KEY (experimentId) REFERENCES Experiment (experimentId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (perturbationId) REFERENCES Perturbation (perturbationId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS BacteriaCommunity (
    bacteriaId INT,
    experimentId INT,
    PRIMARY KEY (bacteriaId, experimentId),
    FOREIGN KEY (bacteriaId) REFERENCES Bacteria (bacteriaId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (experimentId) REFERENCES Experiment (experimentId) ON UPDATE CASCADE ON DELETE CASCADE
);