# Writer-Identifier
A project that uses ML to identify Writers from their hand writing using IAM dataset

# Dataset
if you download the IAM dataset 'data/formsA-D.tgz', download also 'data/xml.tgz' and do the following

1- create a folder called "new data"

2- put them in the same folder after extraction

3- put the 'create DataSet.py' code with them

4- run this code and it will create a dataset folder that contains the writers and inside each writer folder his/her images

"please, classfy each test.png to the correct writer by your self as the classified ones by the script need to be slightly modified"

# Libraries needed to be run
we've done our project using Jupyter notebook. if you haven't it, you can copy these few cells into a python file and run it.

1- python

2- Python packages as numpy,..., etc

3- openCV

4- SKimage

5- SKLearn

# Dataset shape
it takes this hirerachy

 Markup : • \data
            – \01
              ∗ \1
                 · 1.png
                 · 2.png
              ∗ \2
                 · 1.png
                 · 2.png
              ∗ \3
                 · 1.png
                 · 2.png
              ∗ test.png
            – \02
              ∗ \1
                 · 1.png
                 · 2.png
              ∗ \2
                 · 1.png
                 · 2.png
              ∗ \3
                 · 1.png
                 · 2.png
                 ∗ test.png
       
       
 # How to run the project
 • Preconditions
 
 1- open the .ipynb in a new kernel and restart kernel before running it if you work with before.
 
 2- delete any reults.txt or time.txt files before running.
 
 • open final.ipynb file, run the cells, and it'll ask you to enter the path to the dataset. write the path and it'll create new time and results files and then, it'll print the results on them by the end of the code.
