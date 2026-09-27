"""Sample input vector for the /predict endpoint.

Generated from row 1 of eda_data.csv, encoded exactly as in model_training.ipynb
(pd.get_dummies(..., drop_first=True)) and ordered to match the 169 columns stored
in FlaskAPI/models/model_file.p.

Actual avg_salary for this row: 87.5 (thousands USD)
Model prediction for this vector: 92.9111

If the model is retrained with a different feature set, regenerate this file.
The column order below is authoritative and must match model_file.p["columns"].
"""

# Column names, in the exact order expected by the model.
columns = [
    'Rating',
    'num_comp',
    'hourly',
    'employer_provided',
    'same_state',
    'age',
    'python_yn',
    'spark',
    'aws',
    'excel',
    'desc_len',
    'Size_1 to 50 employees',
    'Size_10000+ employees',
    'Size_1001 to 5000 employees',
    'Size_201 to 500 employees',
    'Size_5001 to 10000 employees',
    'Size_501 to 1000 employees',
    'Size_51 to 200 employees',
    'Size_Unknown',
    'Type of ownership_College / University',
    'Type of ownership_Company - Private',
    'Type of ownership_Company - Public',
    'Type of ownership_Government',
    'Type of ownership_Hospital',
    'Type of ownership_Nonprofit Organization',
    'Type of ownership_Other Organization',
    'Type of ownership_School / School District',
    'Type of ownership_Subsidiary or Business Segment',
    'Type of ownership_Unknown',
    'Industry_Accounting',
    'Industry_Advertising & Marketing',
    'Industry_Aerospace & Defense',
    'Industry_Architectural & Engineering Services',
    'Industry_Auctions & Galleries',
    'Industry_Banks & Credit Unions',
    'Industry_Beauty & Personal Accessories Stores',
    'Industry_Biotech & Pharmaceuticals',
    'Industry_Brokerage Services',
    'Industry_Colleges & Universities',
    'Industry_Computer Hardware & Software',
    'Industry_Construction',
    'Industry_Consulting',
    'Industry_Consumer Product Rental',
    'Industry_Consumer Products Manufacturing',
    'Industry_Department, Clothing, & Shoe Stores',
    'Industry_Education Training Services',
    'Industry_Energy',
    'Industry_Enterprise Software & Network Solutions',
    'Industry_Farm Support Services',
    'Industry_Federal Agencies',
    'Industry_Financial Analytics & Research',
    'Industry_Financial Transaction Processing',
    'Industry_Food & Beverage Manufacturing',
    'Industry_Gambling',
    'Industry_Gas Stations',
    'Industry_Health Care Products Manufacturing',
    'Industry_Health Care Services & Hospitals',
    'Industry_Health, Beauty, & Fitness',
    'Industry_IT Services',
    'Industry_Industrial Manufacturing',
    'Industry_Insurance Agencies & Brokerages',
    'Industry_Insurance Carriers',
    'Industry_Internet',
    'Industry_Investment Banking & Asset Management',
    'Industry_K-12 Education',
    'Industry_Lending',
    'Industry_Logistics & Supply Chain',
    'Industry_Metals Brokers',
    'Industry_Mining',
    'Industry_Motion Picture Production & Distribution',
    'Industry_Other Retail Stores',
    'Industry_Real Estate',
    'Industry_Religious Organizations',
    'Industry_Research & Development',
    'Industry_Security Services',
    'Industry_Social Assistance',
    'Industry_Sporting Goods Stores',
    'Industry_Staffing & Outsourcing',
    'Industry_Stock Exchanges',
    'Industry_TV Broadcast & Cable Networks',
    'Industry_Telecommunications Manufacturing',
    'Industry_Telecommunications Services',
    'Industry_Transportation Equipment Manufacturing',
    'Industry_Transportation Management',
    'Industry_Travel Agencies',
    'Industry_Trucking',
    'Industry_Video Games',
    'Industry_Wholesale',
    'Sector_Accounting & Legal',
    'Sector_Aerospace & Defense',
    'Sector_Agriculture & Forestry',
    'Sector_Arts, Entertainment & Recreation',
    'Sector_Biotech & Pharmaceuticals',
    'Sector_Business Services',
    'Sector_Construction, Repair & Maintenance',
    'Sector_Consumer Services',
    'Sector_Education',
    'Sector_Finance',
    'Sector_Government',
    'Sector_Health Care',
    'Sector_Information Technology',
    'Sector_Insurance',
    'Sector_Manufacturing',
    'Sector_Media',
    'Sector_Mining & Metals',
    'Sector_Non-Profit',
    'Sector_Oil, Gas, Energy & Utilities',
    'Sector_Real Estate',
    'Sector_Retail',
    'Sector_Telecommunications',
    'Sector_Transportation & Logistics',
    'Sector_Travel & Tourism',
    'Revenue_$1 to $5 million (USD)',
    'Revenue_$10 to $25 million (USD)',
    'Revenue_$10+ billion (USD)',
    'Revenue_$100 to $500 million (USD)',
    'Revenue_$2 to $5 billion (USD)',
    'Revenue_$25 to $50 million (USD)',
    'Revenue_$5 to $10 billion (USD)',
    'Revenue_$5 to $10 million (USD)',
    'Revenue_$50 to $100 million (USD)',
    'Revenue_$500 million to $1 billion (USD)',
    'Revenue_-1',
    'Revenue_Less than $1 million (USD)',
    'Revenue_Unknown / Non-Applicable',
    'job_state_AZ',
    'job_state_CA',
    'job_state_CO',
    'job_state_CT',
    'job_state_DC',
    'job_state_DE',
    'job_state_FL',
    'job_state_GA',
    'job_state_IA',
    'job_state_ID',
    'job_state_IL',
    'job_state_IN',
    'job_state_KS',
    'job_state_KY',
    'job_state_LA',
    'job_state_MA',
    'job_state_MD',
    'job_state_MI',
    'job_state_MN',
    'job_state_MO',
    'job_state_NC',
    'job_state_NE',
    'job_state_NJ',
    'job_state_NM',
    'job_state_NY',
    'job_state_OH',
    'job_state_OR',
    'job_state_PA',
    'job_state_RI',
    'job_state_SC',
    'job_state_TN',
    'job_state_TX',
    'job_state_UT',
    'job_state_VA',
    'job_state_WA',
    'job_state_WI',
    'job_simp_data engineer',
    'job_simp_data scientist',
    'job_simp_director',
    'job_simp_manager',
    'job_simp_mle',
    'job_simp_na',
    'seniority_na',
    'seniority_senior',
]

# Feature values for the sample row, aligned with `columns` above.
data_in = [
    3.4,  # Rating
    0.0,  # num_comp
    0.0,  # hourly
    0.0,  # employer_provided
    0.0,  # same_state
    42.0,  # age
    1.0,  # python_yn
    0.0,  # spark
    0.0,  # aws
    0.0,  # excel
    4783.0,  # desc_len
    0.0,  # Size_1 to 50 employees
    1.0,  # Size_10000+ employees
    0.0,  # Size_1001 to 5000 employees
    0.0,  # Size_201 to 500 employees
    0.0,  # Size_5001 to 10000 employees
    0.0,  # Size_501 to 1000 employees
    0.0,  # Size_51 to 200 employees
    0.0,  # Size_Unknown
    0.0,  # Type of ownership_College / University
    0.0,  # Type of ownership_Company - Private
    0.0,  # Type of ownership_Company - Public
    0.0,  # Type of ownership_Government
    0.0,  # Type of ownership_Hospital
    0.0,  # Type of ownership_Nonprofit Organization
    1.0,  # Type of ownership_Other Organization
    0.0,  # Type of ownership_School / School District
    0.0,  # Type of ownership_Subsidiary or Business Segment
    0.0,  # Type of ownership_Unknown
    0.0,  # Industry_Accounting
    0.0,  # Industry_Advertising & Marketing
    0.0,  # Industry_Aerospace & Defense
    0.0,  # Industry_Architectural & Engineering Services
    0.0,  # Industry_Auctions & Galleries
    0.0,  # Industry_Banks & Credit Unions
    0.0,  # Industry_Beauty & Personal Accessories Stores
    0.0,  # Industry_Biotech & Pharmaceuticals
    0.0,  # Industry_Brokerage Services
    0.0,  # Industry_Colleges & Universities
    0.0,  # Industry_Computer Hardware & Software
    0.0,  # Industry_Construction
    0.0,  # Industry_Consulting
    0.0,  # Industry_Consumer Product Rental
    0.0,  # Industry_Consumer Products Manufacturing
    0.0,  # Industry_Department, Clothing, & Shoe Stores
    0.0,  # Industry_Education Training Services
    0.0,  # Industry_Energy
    0.0,  # Industry_Enterprise Software & Network Solutions
    0.0,  # Industry_Farm Support Services
    0.0,  # Industry_Federal Agencies
    0.0,  # Industry_Financial Analytics & Research
    0.0,  # Industry_Financial Transaction Processing
    0.0,  # Industry_Food & Beverage Manufacturing
    0.0,  # Industry_Gambling
    0.0,  # Industry_Gas Stations
    0.0,  # Industry_Health Care Products Manufacturing
    1.0,  # Industry_Health Care Services & Hospitals
    0.0,  # Industry_Health, Beauty, & Fitness
    0.0,  # Industry_IT Services
    0.0,  # Industry_Industrial Manufacturing
    0.0,  # Industry_Insurance Agencies & Brokerages
    0.0,  # Industry_Insurance Carriers
    0.0,  # Industry_Internet
    0.0,  # Industry_Investment Banking & Asset Management
    0.0,  # Industry_K-12 Education
    0.0,  # Industry_Lending
    0.0,  # Industry_Logistics & Supply Chain
    0.0,  # Industry_Metals Brokers
    0.0,  # Industry_Mining
    0.0,  # Industry_Motion Picture Production & Distribution
    0.0,  # Industry_Other Retail Stores
    0.0,  # Industry_Real Estate
    0.0,  # Industry_Religious Organizations
    0.0,  # Industry_Research & Development
    0.0,  # Industry_Security Services
    0.0,  # Industry_Social Assistance
    0.0,  # Industry_Sporting Goods Stores
    0.0,  # Industry_Staffing & Outsourcing
    0.0,  # Industry_Stock Exchanges
    0.0,  # Industry_TV Broadcast & Cable Networks
    0.0,  # Industry_Telecommunications Manufacturing
    0.0,  # Industry_Telecommunications Services
    0.0,  # Industry_Transportation Equipment Manufacturing
    0.0,  # Industry_Transportation Management
    0.0,  # Industry_Travel Agencies
    0.0,  # Industry_Trucking
    0.0,  # Industry_Video Games
    0.0,  # Industry_Wholesale
    0.0,  # Sector_Accounting & Legal
    0.0,  # Sector_Aerospace & Defense
    0.0,  # Sector_Agriculture & Forestry
    0.0,  # Sector_Arts, Entertainment & Recreation
    0.0,  # Sector_Biotech & Pharmaceuticals
    0.0,  # Sector_Business Services
    0.0,  # Sector_Construction, Repair & Maintenance
    0.0,  # Sector_Consumer Services
    0.0,  # Sector_Education
    0.0,  # Sector_Finance
    0.0,  # Sector_Government
    1.0,  # Sector_Health Care
    0.0,  # Sector_Information Technology
    0.0,  # Sector_Insurance
    0.0,  # Sector_Manufacturing
    0.0,  # Sector_Media
    0.0,  # Sector_Mining & Metals
    0.0,  # Sector_Non-Profit
    0.0,  # Sector_Oil, Gas, Energy & Utilities
    0.0,  # Sector_Real Estate
    0.0,  # Sector_Retail
    0.0,  # Sector_Telecommunications
    0.0,  # Sector_Transportation & Logistics
    0.0,  # Sector_Travel & Tourism
    0.0,  # Revenue_$1 to $5 million (USD)
    0.0,  # Revenue_$10 to $25 million (USD)
    0.0,  # Revenue_$10+ billion (USD)
    0.0,  # Revenue_$100 to $500 million (USD)
    1.0,  # Revenue_$2 to $5 billion (USD)
    0.0,  # Revenue_$25 to $50 million (USD)
    0.0,  # Revenue_$5 to $10 billion (USD)
    0.0,  # Revenue_$5 to $10 million (USD)
    0.0,  # Revenue_$50 to $100 million (USD)
    0.0,  # Revenue_$500 million to $1 billion (USD)
    0.0,  # Revenue_-1
    0.0,  # Revenue_Less than $1 million (USD)
    0.0,  # Revenue_Unknown / Non-Applicable
    0.0,  # job_state_AZ
    0.0,  # job_state_CA
    0.0,  # job_state_CO
    0.0,  # job_state_CT
    0.0,  # job_state_DC
    0.0,  # job_state_DE
    0.0,  # job_state_FL
    0.0,  # job_state_GA
    0.0,  # job_state_IA
    0.0,  # job_state_ID
    0.0,  # job_state_IL
    0.0,  # job_state_IN
    0.0,  # job_state_KS
    0.0,  # job_state_KY
    0.0,  # job_state_LA
    0.0,  # job_state_MA
    1.0,  # job_state_MD
    0.0,  # job_state_MI
    0.0,  # job_state_MN
    0.0,  # job_state_MO
    0.0,  # job_state_NC
    0.0,  # job_state_NE
    0.0,  # job_state_NJ
    0.0,  # job_state_NM
    0.0,  # job_state_NY
    0.0,  # job_state_OH
    0.0,  # job_state_OR
    0.0,  # job_state_PA
    0.0,  # job_state_RI
    0.0,  # job_state_SC
    0.0,  # job_state_TN
    0.0,  # job_state_TX
    0.0,  # job_state_UT
    0.0,  # job_state_VA
    0.0,  # job_state_WA
    0.0,  # job_state_WI
    0.0,  # job_simp_data engineer
    1.0,  # job_simp_data scientist
    0.0,  # job_simp_director
    0.0,  # job_simp_manager
    0.0,  # job_simp_mle
    0.0,  # job_simp_na
    1.0,  # seniority_na
    0.0,  # seniority_senior
]

assert len(data_in) == len(columns) == 169
