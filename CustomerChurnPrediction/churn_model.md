# Churn Model Record

# Logistic Regression vs Random Forest

| Metric    | Logistic Regression | Random Forest (100 trees) |
| --------- | ------------------- | ------------------------- |
| Accuracy  | **80.27%** ✅       | 79.91%                    |
| Precision | 67.9%               | **69.0%** ✅              |
| Recall    | **57.7%** ✅        | 53%                       |

Logistic Regression Still Wins Overall Especially for churn prediction because: Recall matters more

So For this business problem I would currently choose Logistic Regression. Because:
Higher recall
Better overall balance
Easier to explain to business

# with Feature Importance / Coefficients in logistic model found Top Churn Indicators

Positive coefficient - more likely to churn
Negative coefficient - less likely to churn

| Feature                         | Meaning                                 | Coefficient |
| ------------------------------- | --------------------------------------- | ----------- |
| Contract_Month-to-month         | Biggest churn driver 🚨                 | 0.277989    |
| Dependents_No                   | Customers without dependents churn more | 0.264426    |
| Internet Service_Fiber optic    | Fiber users churn more                  | 0.176773    |
| Payment Method_Electronic check | Higher churn risk                       | 0.118132    |
| Online Security_No              | No security → more churn                | 0.110183    |
| Monthly Charges                 | Higher bills → more churn               | 0.099875    |
| Tech Support_No                 | Lack of support → churn                 | 0.098399    |
| Paperless Billing_Yes           | Slightly higher churn                   | 0.088033    |
| Streaming TV_Yes                | Some churn correlation                  | 0.069564    |
| Multiple Lines_Yes              | Some churn correlation                  | 0.058079    |

with this table we can say Customers on monthly plans leave more often.
Customers without dependents are more likely to churn.

With this Project I am able to learn and do
✅ Real dataset project
✅ Data cleaning
✅ Handling missing values
✅ Encoding
✅ Logistic Regression
✅ Random Forest
✅ Confusion Matrix
✅ Precision / Recall
✅ Hyperparameter Tuning
✅ Feature Importance
✅ Business interpretation
