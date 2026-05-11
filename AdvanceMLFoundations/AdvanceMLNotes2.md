# 🚀 Day 34 - EDA Mastery - Exploratory Data Analysis

Raw messy data
↓
Understand data
↓
Find missing values
↓
Detect outliers
↓
Check correlations
↓
Visualize distributions
↓
Then build model

Topics
✅ df.info()
✅ df.describe()
✅ df.isnull().sum()
✅ duplicate detection
✅ value counts
✅ target distribution
✅ correlation matrix

Visuals:
✅ histograms
✅ boxplots
✅ scatter plots
✅ heatmaps

Libraries:
✅ matplotlib
✅ seaborn

1. What is EDA?
   EDA = Exploratory Data Analysis. Before training any model, ask: “What story is this data telling me?”
   Example:
   If a customer churn dataset has:
   70% customers who stay
   30% customers who leave
   That immediately tells you: Class imbalance exists. That changes:
   model choice
   evaluation metric
   preprocessing
   That’s why EDA matters.

Data Scientist Mindset. Instead of:
❌ “Let’s train RandomForest.”
Think:
✅ What is the target?
✅ Is data clean?
✅ Are some columns useless?
✅ Are there missing values?
✅ Is the target balanced?
✅ Are features skewed?
✅ Any leakage?
✅ Any strong correlations?
✅ Any outliers?

2. Dataset Structure
   1. First thing: df.shape
      Example output: (10000, 15) Meaning, 10,000 rows, 15 columns
      Ask:
      enough data?
      too many features?
      tiny dataset?
   2. Check columns: df.columns => ['age', 'salary', 'gender', 'city', 'churn']
      Now identify:
      Numerical: age, salary
      Categorical: gender, city
      Target: churn
   3. Check types: df.info()
      age int64
      salary float64
      gender object
      This tells:
      what preprocessing needed
      encoding requirements
      possible data issues
      If age is object: "25", "30" which is Bad data type. Need conversion.

3. Missing Values
   Real-world data is messy.
   Check - df.isnull().sum()

   Interpretation:
   <5% → usually manageable
   5–30% → careful handling
   50% → maybe drop column

   Use
   Numerical: median, mean. Use median if skewed.
   Categorical: mode
   Advanced: KNN imputation, Iterative imputation

   Why median over mean? Because mean gets affected by outliers.

   Example:
   age 0
   salary 120
   city 45
   Meaning: salary missing in 120 rows Some models fail: Logistic Regression, SVM, Linear Regression. Even tree models can behave poorly.

4. Duplicate Rows
   Check df.duplicated().sum()
   Duplicates can:
   bias learning
   inflate accuracy
   create leakage

   Remove using: df.drop_duplicates(inplace=True)

5. Descriptive Statistics
   df.describe()
   Gives: mean, std, min, max, quartiles
   Eg: salary mean = 50,000
   salary max = 2,000,000
   Huge difference. Possible outliers.

6. Understand Target Variable
   1. Classification target:
      df['target'].value_counts()
      Eg:
      No 900
      Yes 100
      Class imbalance. Model can predict all "No" and still get: 90% accuracy.

      Visualize:
      sns.countplot(x='target', data=df)
      plt.show()

      Interpret:
      balanced?
      imbalanced?

   2. Regression target:
      df['price'].describe()
      Visualize:
      sns.histplot(df['price'], kde=True)
      Ask:
      normally distributed?
      skewed?
      extreme values?

7. Univariate Analysis
   Study ONE feature at a time.
   1. Numerical: sns.histplot(df['age'], kde=True)
      Interpret:
      normal?
      skewed?
      multimodal?
      Example: Two peaks? Could indicate two customer groups.
   2. Boxplot: sns.boxplot(x=df['salary'])
      Shows:
      median
      quartiles
      outliers
   3. Categorical: sns.countplot(x='gender', data=df) Shows distribution.

8. Outliers
   Outliers = unusually extreme values.
   Example: Salary
   30000
   45000
   50000
   52000
   9999999

   in this 9999999 = suspicious.
   They distort:
   mean
   regression line
   distance-based models
   scaling

   Detect using IQR:
   Q1 = df['salary'].quantile(0.25)
   Q3 = df['salary'].quantile(0.75)
   IQR = Q3 - Q1
   lower = Q1 - 1.5 _ IQR
   upper = Q3 + 1.5 _ IQR
   Find outliers: outliers = df[(df['salary'] < lower) | (df['salary'] > upper)]
   But think critically: Not all outliers are bad.
   Example: Luxury house prices. High values may be valid.
   Should we always remove outliers? No. Only if they are errors or harmful noise.

9. Skewness
   Skew = asymmetry in distribution.
   df['salary'].skew()
   Interpret:
   near 0 → symmetric
   1 → highly right skewed
   <-1 → left skewed
   Right skew example:
   Most salaries: 30k–70k
   Few: 500k+
   Models like:
   Linear Regression
   Logistic Regression
   often benefit from better distributions.
   Fix: np.log1p(df['salary'])

10. Correlation
    how features relate to each other.
    df.corr()
    Visualize: sns.heatmap(df.corr(), annot=True)
    Interpret:
    1 → perfect positive (Bigger house → higher price)
    -1 → perfect negative (Older house → cheaper)
    0 → no correlation (Weak relationship)
    High correlation between features = multicollinearity. Can cause instability in models like Linear Regression. Consider dropping one of the correlated features.
    Why important? for eg area_sqft, area_sqmeters Same information. Bad for linear models.

11. Bivariate Analysis
    Relationship between TWO variables.
    1. Classification target:
       sns.boxplot(x='churn', y='salary', data=df)
       Question: Do churners have lower salary?
    2. Categorical vs target:
       sns.countplot(x='gender', hue='churn', data=df)
       Question: Does gender affect churn?
    3. Regression:
       sns.scatterplot(x='area', y='price', data=df)
       Question: Linear relation?

12. Feature Leakage
    Eg: Predict customer churn.
    Features are:
    subscription_end_date
    refund_processed
    churn
    Refund happens AFTER churn. This creates leakage. Model learns from future info. Inflates performance. Always check feature timelines.
    Always ask: “Would I know this at prediction time?”

13. Categorical Cardinality
    check df['city'].nunique()
    Eg: 2500 unique cities - One-hot encoding explosion.
    Solutions:
    frequency encoding
    target encoding
    grouping rare labels

14. Data Quality Checks
    Watch for: Impossible values.
    Eg:
    Age: -5, 250
    Salary: -10000
    Dates: future birth dates
    These are data issues.

# Real EDA Workflow

df.head()
df.shape
df.info()
df.describe()

df.isnull().sum()
df.duplicated().sum()

target analysis
numerical distributions
categorical distributions

outliers
skewness
correlation

bivariate analysis
data quality checks
leakage checks

Heteroscedasticity: Increasing spread
As income increases the spread becomes wider.
means For low income prices tightly grouped
For high income prices widely spread
This can hurt linear regression assumptions. Random Forest handles this better.
