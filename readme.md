# Meme Generator

Meme generator app is a simple command line and web app
That takes commanline argument and web-form input from 
users and generate random memes. 

## Description - Overview

This application has two modules

* MemeEngine

MemeEngine has one class that's responsible for meme generation and export
MemeEngine.py can be initialized by taking the file export path argument. 
It make_meme method that's responsible for taking, path, text, author as an argument
This class needs python pillow library to be able to manipulate images and texts. 
- Load an image
- resize the image
- caption the image 
- export the image
- return the path of the generated meme

* QuoteEngine

QuoteEngine has 7 classes

* - IngestorInterface 
The IngestorInterface class is an abstract class that get's realized by all the ingestor 
sub classes.
* - Ingestor
The Ingestor class realizes IngestorInterface class and deligates parsing task to 
other Ingestor classes based on the file extension give. 
* - TXTIngestor
The TXTIngestor class parses .txt files and create QuoteModel objects

* - CSVIngestor
The CSVIngestor class parses .csv files and create QuoteModel objects
This class needs pandas library installed before use

* - DocxIngestor
The DocxIngestor class parses .docx files and create QuoteModel objects
This class needs python-docx installed before use

* - PDFIngestor
The PDFIngestor class parses .pdf files and create QuoteModel objects
This calss needs pdftoword binary installed on the machines before use.
On mac - binary installation can be achieved by using brew

* - QuoteModel
QuoteMode class is responsible for the creation on quote objects.
quotes objects have a title and an author attribute, and and 
a represenation method. 


```python
s = "Python syntax highlighting"
print s
python3 meme.py

```

#
## Getting Started

### Dependencies
You will need install these libraris and applicaitons
#### Libraries
* pandas
* pythond-docx
* requests
### Applications
* pdftotext

## detial of the dependancies can be found in requirements.txt file.

### Installing
This application is written on python version 3.8, and tested on os: macOs Big Sur ver 11.04

1. Install all the libraries 
```python
pip3 install requirements.txt
```
2. Install the pdftotext application -you will need to install brew on mac.

### Executing program
The program can be executed from command line as below:

1. Exampel usage with args:

```python
python3 meme.py './_data/photos/dog/xander_1.jpg' 'xander is the best cat in Mars' 'James bond'
```

2. Exampel usage with args:

```python
python3 meme.py
```

Example usage with flask:

Use the following commands to start 
once flask is installed using pip3 install flaks 

run the below command to start the webpage 
```python
export FLASK_APP==app.py
export FLASK_ENV=development
export run
```


## Author:
Daniel Teshager  
[@danielteshager](https://twitter.com/danteshager)
