This method assumes you have python3 installed.
Deployment to Streamlit Cloud coming soon...

Open a terminal and move to the desired folder.

Clone the repository with git clone git@github.com:achoroj3/Predicting_Heart_Disease.git

Create a python environment, then activate the environment. 
installscript.sh creates a python environment, runs the environment, and downloads streamlit. This prevents streamlit from merging with your global package manager.

This run this script with:
chmod +x installscript.sh && ./installsctipt.sh

Once that completes, run the command streamlit run app.py

Navigate to the website provided.

Turn off the environment with "deactivate"