# Data Science Salary Estimator: Project Overview

Developed a predictive tool that estimates Data Science salaries based on job descriptions, location, company attributes, and technical skill requirements, designed to help job seekers make informed salary negotiations.

- Built a full end-to-end machine learning pipeline to predict average salaries with a Mean Absolute Error (MAE) of approximately $12.8K.
- Scraped and cleaned job postings from Glassdoor using Python and Selenium.
- Engineered features from job descriptions, quantifying the importance of tools and technologies such as Python, Excel, AWS, Spark, and TensorFlow.
- Implemented model optimization using GridSearchCV across Linear Regression, Lasso Regression, and Random Forest Regressor, achieving the best overall performance.
- Deployed a production-ready Flask API for real-time salary predictions.

## Code and Resources

**Python Version:** 3.13  
**Required Packages:** pandas, numpy, scikit-learn, matplotlib, seaborn, selenium, flask, json, pickle  

**To install dependencies:**  
```bash
pip install -r requirements.txt
```

**Pipeline run order:**

```bash
python data_cleaning.py     # glassdoor_jobs.csv    -> salary_data_cleaned.csv
jupyter notebook data_eda.ipynb        # salary_data_cleaned.csv -> eda_data.csv
jupyter notebook model_training.ipynb  # eda_data.csv -> FlaskAPI/models/model_file.p
```

**References:**  
- Scraper GitHub Repository: [https://github.com/arapfaik/scraping-glassdoor-selenium](https://github.com/arapfaik/scraping-glassdoor-selenium)  
- Scraper Tutorial: [Selenium Glassdoor Scraper Article](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)  
- Flask Deployment Tutorial: [Productionize ML Models with Flask and Heroku](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)

## Web Scraping

Modified and extended a Glassdoor scraping script to gather job postings for Data Science-related roles.  
Each record included the following attributes:

- Job Title  
- Salary Estimate  
- Job Description  
- Rating  
- Company  
- Location  
- Company Headquarters  
- Company Size  
- Company Founded Date  
- Type of Ownership  
- Industry  
- Sector  
- Revenue  
- Competitors  

### Scope and limitations

The modelling in this repo runs on `glassdoor_jobs.csv`, a snapshot captured in
April 2024. That snapshot is the project's data source and is committed here so
every downstream step is reproducible.

`Glassdoor_Scraper.py` is retained as the collection code, but it is **card-level
only**: it reads the fields visible on a search-results card (title, company,
rating, location, salary, snippet, date posted, job link) and does not open each
posting's detail page. It therefore does not reproduce the richer fields the
model uses, such as Industry, Sector, Revenue, Company Size, and Founded date,
and its output columns do not match what `data_cleaning.py` expects.

Recovering those fields means visiting every posting individually, which is slow
and runs into Glassdoor's bot detection. Since Glassdoor's markup changes
frequently, keeping a detail-page scraper working is ongoing maintenance with no
benefit to the modelling work, so the captured dataset is used instead. Treat the
scraper as a reference implementation rather than a working ingestion step.

## Data Cleaning

After collecting the raw data, extensive preprocessing was performed to prepare the dataset for modeling.  
The following changes and new variables were created:

- Extracted numeric values from text-based salary estimates.  
- Added flags for hourly pay and employer-provided salary information.  
- Removed rows lacking salary data.  
- Parsed company rating from text.  
- Extracted state information from job location.  
- Created a binary indicator for whether the job is located at the company's headquarters.  
- Converted the year founded into company age.  
- Created binary indicators for the presence of technical skills:  
  - Python  
  - R  
  - Excel  
  - AWS  
  - Spark  
  - SQL  
- Simplified job titles into broader categories and added a seniority-level feature.  
- Computed a description length variable to measure the verbosity of job postings.

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to visualize salary trends, feature distributions, and relationships among categorical variables.  

Key findings included:  
- Salary variation across different states and company ratings.  
- Visualization of the most common keywords using a word cloud. 
- Clear evidence that technical skills and company-level factors significantly influence salary levels.
  
![wordcloud](wordcloud.png)

## Model Building

### Data Preparation
- Converted categorical variables into dummy variables using `pd.get_dummies()`.  
- Split the dataset into training (80%) and testing (20%) subsets.

### Models Evaluated
Three regression models were tested using **Mean Absolute Error (MAE)** as the evaluation metric, selected for its interpretability and robustness against outliers.

1. **Multiple Linear Regression**: established a baseline for comparison.  
2. **Lasso Regression**: applied regularization to handle sparse categorical data.  
3. **Random Forest Regressor**: chosen for its ability to capture nonlinear relationships and feature interactions.

## Model Evaluation

| Model                 | MAE (Mean Absolute Error) |
| --------------------- | ------------------------- |
| **Random Forest**     | **12.80**                 |
| **Linear Regression** | 18.84                     |
| **Lasso Regression**  | 19.65                     |

The Random Forest model demonstrated the best performance, achieving the lowest prediction error on both training and validation sets.

## Model Deployment

Developed a Flask-based REST API to serve the trained model for real-time salary predictions.

- The API accepts job listing information as JSON input.  
- Input data is automatically formatted to match the model's training feature structure.  
- Returns a salary prediction in JSON format.

### Running it locally

```bash
cd FlaskAPI
pip install -r requirements.txt
python app.py
```

Then, from a second shell:

```bash
cd FlaskAPI
python sample_request.py
```

Expected output, using the sample vector in `data_input.py`:

```
{'response': 92.91111111111111}
```

The endpoint is POST-only and expects exactly 169 features, matching the column
list stored alongside the model in `models/model_file.p`. A request with the
wrong number of features returns HTTP 400 naming the mismatch.

