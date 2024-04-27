from memory_profiler import profile
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import fetch_openml

@profile
def scikit_learn():
    # Load the Spambase dataset
    spambase = fetch_openml(name='spambase', version=1)

    # Split the data into features and labels
    X = spambase.data
    y = spambase.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Display classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

scikit_learn()