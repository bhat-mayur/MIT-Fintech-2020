import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

#==============================================================================
# Data Input
#==============================================================================
filename = 'X_train_small.csv'  #This file should be placed in the Data folder
output_filename = 'training_learning.csv'

#==============================================================================
# Choices
#==============================================================================
test_pct=.9       #Set the percentage of your data to test upon
num_epochs=100      #Set the number of epochs(forward and backward passes)
batch_size=30000    #Set the batch size (Amount of data to consider in an epoch)
random_seed=42      #Set the random seed to initialize your Neural Net
use_kfold=False     #Set as True if you want to create an estimate for accuracy using k folds (otherwise False)
n_folds=5           #Set the number of folds to consider in your k-folds analysis

# =============================================================================
# Model
# =============================================================================

def model_to_evaluate(input_dimensions, output_dimensions):
    # Initialize and build the model you want to test
    # For full documentation see: https://keras.io/
    model = Sequential()
    # Layers documentation here: https://keras.io/layers/core/
    # This model currently focuses on Dense and Dropout Layers
    model.add(Dense(25, input_dim=input_dimensions, activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(output_dimensions, activation='linear'))
    # Losses documentation here: https://keras.io/losses/
    # Optimizer documentation here: https://keras.io/optimizers/
    # Metrics documentation here: https://keras.io/metrics/
    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=["accuracy"])
    return model
