import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error

def load_and_summarize(filepath):
  '''loads a csv and prints its head and info.'''
  print(f" --- Loading {filepath.split('/')[-1]} ---")
  df=pd.read_csv(filepath)
  print("First 5 rows:")
  print(df.head())
  print("\nData Info:")
  df.info()
  return df

def scale_dataframe(df):
  scaler=MinMaxScaler()
  scaled_data = scaler.fit_transform(df)
  return pd.DataFrame(scaled_data, columns=df.columns)

def split_data(df, target_column):
  X=df.drop(columns=[target_column])
  y=df[target_column]
  X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
  return X_train, X_test,y_train,y_test

def evaluate_classifier(y_true, y_pred, model_name="Model"):
  accuracy = accuracy_score(y_true, y_pred)
  print(f"Accuracy for {model_name}: {accuracy:.4f}")

def evaluate_regressor(y_true, y_pred, model_name="Model"):
  mse=mean_squared_error(y_true, y_pred)
  print(f"MSE for {model_name}: {mse:.4f}")
