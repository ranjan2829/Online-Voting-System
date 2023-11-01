# Matplotlib and Seaborn
import seaborn as sns

# Data Manipulation with Pandas
df = pd.read_csv('data.csv')
print(df.head())

# Machine Learning with Scikit-Learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# (Assuming X and y are defined)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
