# python-sample
Installing and Running Python
-You can download the python installer for python download page of the official website.

Setting Virtual Environment
-To set up a virtual environment, we first need to install the package virtualenv using pip.
code:
// upgrade pip to its latest version  
python -m pip install --upgrade pip   
  
// install virtualenv  
pip install virtualenv 
end code:
Then, you can simply create your project virtual environment using "virtualenv venv" command where "venv" is the environment name.
code:
// create a new directory 'project-36'  
mkdir project-36  
  
// change currenct directory to 'project-36'  
cd .\project-36  
  
// create a virtual environment named 'venv', feel free to name it anything you like
virtualenv venv
endcode:

Now, it's time to activate the envoronment, check the python version and also list the default packages installed for us.
The (venv) on the left shows that our virtual environment is active.
code:
// activate the virtual environment 
.\venv\Scripts\activate
// check the python version
python --version
// list all packages installed by default
pip list
// deactivate the virtual environment
deactivate
endcode:



