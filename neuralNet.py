import numpy as np
import pandas as pd
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import train_test_split
#from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import compute_class_weight
from tensorflow import keras
from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Dense, Dropout
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Dropout
# Load the dataset
df = pd.read_csv('masterfile.csv')

# Drop NaN values from relevant columns and convert the 'year' column to integer
df = df.dropna(subset=['rating', 'votes', 'gross(in $)', 'year'])
df['year'] = pd.to_numeric(df['year'], errors='coerce').astype(int)
#print(df.isnull().sum())

# Extract features and labels
X = df[['year', 'rating', 'votes', 'gross(in $)']]
y = df['bechdel']

# Perform one-hot encoding for categorical variables (if needed)
# For simplicity, let's assume you only have numerical features in X

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Standardize/normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert labels to categorical form for training
y_train_categorical = pd.get_dummies(y_train)
y_test_categorical = pd.get_dummies(y_test)

# Calculate class weights based on inverse class frequencies -- did not work
# total_samples = len(y_train)
# class_weight = {
#     0: total_samples / (4 * np.sum(y_train ==0)), 
#     1: total_samples / (2 * np.sum(y_train ==0)), 
#     2: total_samples / (4 * np.sum(y_train ==0)), 
#     3: total_samples / np.sum(y_train == 3)
#     }


# Model architecture
model = keras.models.Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(64, activation='relu'))  
model.add(Dropout(0.4))
model.add(Dense(64, activation='relu'))
model.add(Dense(4, activation='softmax'))

#Specify the learning rate 
custom_optimizer = Adam(learning_rate = 0.005)
# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=custom_optimizer, metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_categorical, epochs=10, batch_size=32, validation_split=0.2)

#Use stratified sampling in train-test split -- didn't help
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test_categorical)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')