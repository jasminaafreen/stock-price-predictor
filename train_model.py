from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from utils import load_data

# Load data
df = load_data()

X = df[['Prev_Close']]
y = df['Close']

# Split (no shuffle for time series)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved!")
