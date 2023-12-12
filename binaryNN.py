import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

# Load your dataset
df = pd.read_csv('masterfile_with_encoded_genre.csv')

# Define features and target
X = df[['year', 'rating', 'Biography', 'Drama', 'Music', 'History', 'Romance', 'Comedy', 'Crime', 'Musical', 'Action', 'Thriller', 'Sport', 'Adventure', 'Family', 'War', 'Animation', 'Horror', 'Fantasy', 'Sci-Fi', 'Mystery', 'Western']]
y = (df['bechdel'] == 3).astype(int)  # Convert to binary: 1 if Bechdel score is 3, else 0

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)

# Standardize/normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model architecture
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(64, activation='relu'))  
model.add(Dropout(0.4))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Binary classification with sigmoid activation

# Specify the learning rate 
custom_optimizer = Adam(learning_rate=0.001)

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=custom_optimizer, metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

# Predictions on the test set
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)

# Output confusion matrix and classification report
conf_matrix = confusion_matrix(y_test, y_pred_classes)
classification_rep = classification_report(y_test, y_pred_classes)

print("Confusion Matrix:")
print(conf_matrix)

print("\nClassification Report:")
print(classification_rep)