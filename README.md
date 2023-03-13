# machine_learning_DA_part_1
This repository contains the code for a ML-augmented data assimilation method, demonstrated on the Lorenz96 system. The code is implemented in four classes, each contained in a single .py file in the root directory.

## Processed data
Processed data for generating the figures is contained in the "PublicationFigs" directory. Data is in netcdf, text, and numpy array format. Figures in the paper can be generated using code in the "tables_and_figs.ipynb" notebook.

## Classes and Run Scripts
"EnKF.py" contains methods for implementing the Ensemble Kalman Filter on the Lorenz 96 system. Options for covariance localization and covariance inflation are included. "L96.py" contains methods that specify the Lorenz system and allow for it to be integrated forward in time. "Experiment.py" contains the bulk of the codebase. It has as an attribute an Xarray DataSet object containing time series data of the true evolution of the system, synthetic observations, ensemble forecasts, and ensemble analyses. Its attributes specify the run settings, including localization, inflation, observation error standard deviation, ensemble size, and observation time step. It also contains methods for generating true trajectories and synthetic observations and for performing assimilation of those observations. Lastly, "NeuralNet.py" contains methods for training and using a simple CNN for assimilation. It implements a cyclic padding procedure and has methods for transforming provided input into the size and shape needed by the neural network.

Sensitivity runs are contained in the "Sensitivity" directory and can be generated by running "sensitivity.py". The case number at the top of the file can be changed. "0" corresponds to the base case, with 1-9 the respective sensitivity runs. The results are stored in a pickle file and are too large to include in the git repository.

Augmented sensitivity runs test the augmented method on the different sensitivity settings. They are in the "Augmented" directory. The results presented in paper correspond to the base run. As with the previous sensitivity runs, they can be generated by running "augmented.py" and setting the case number to the appropriate value.

The "Augmented" directory contains a "TrainingData" directory. The pickle file containing the results from the best performing sensitivity run is placed here. The neural network is trained by running "Train.py", which trains a neural network to emulate the EnKF and saves training history data to text files and model weights to an hdf5 file in this directory.

The "Plotting" directory contains the files and code for generating all the results figures in the paper. "postprocess_forecast.py" and "postprocess_shap.py" must be run to generate the data for some plots from the results. They save the relevant data in the "Data" subdirectory. The hdf5 file containing model weights must be placed in the data subdirectory, along with the pickled results from the all obs EnKF base case, the augmented base case, and the sparse base case (the last being generated by the "augmented.py" file).

If all necessary data files are present, the plots and tables in the paper can be generated using the Jupyter notebook "MakeFigs.ipynb".

## Dependencies
* Numpy
* Scipy
* Keras
* Tensorflow
* Xarray
* Pickle
* Tqdm
* Matplotlib