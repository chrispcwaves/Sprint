##  Sprint 2 

**Project:** Gym Retention Analysis  
**Goal:** Explore patterns that predict which gym members stay active vs. quit.

### Data
- **Source:** [Gym Members Exercise Dataset (Kaggle)](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data)  
- **Raw file:** `data/raw/gym_members_exercise_tracking.csv`  
- **Cleaned file:** `data/processed/gym_members_cleaned.csv`  
- **Target variable:** `retention_status` (1 = Active, 0 = Inactive)  
- **Size:** 973 records × 17 variables  

### Cleaning Summary
- Added `member_id` for unique id
- Standardized column names and removed spaces/parentheses.  
- Created `retention_status` using: ≥ 3 workouts/week and ≥ 1 hour/session → Active (1); else Inactive (0).  
- Final dataset: 973 rows × 17 columns (71% active, 29% inactive).  


### Key EDA Visualizations
All figures saved in `reports/figures/`

| # | Visualization | Filename |
|--|--|--|
| 1️ | Boxplot – Outlier Check | `boxplot_outliers.png` |
| 2️ | Histograms – Age, BMI, Frequency, Duration, Calories | `numeric_distributions.png` |
| 3️ | Scatterplot – Workout Frequency vs Duration by Retention | `scatter_frequency_duration_retention.png` |
| 4️ | Correlation Heatmap | `correlation_matrix.png` |
| 5️| Bar Chart – Retention by Workout Type | `bar_workouttype_retention.png` |

### Insights
- Higher frequency and longer sessions → higher retention.  
- Calories Burned and Workout Frequency are strongly correlated.  
- Strength and HIIT members show better retention than Cardio or Yoga.  
- Dataset has some BMI and Calories outliers, but they appear valid.

### Next Steps:Sprint 3
- Build predictive models (Logistic Regression, Random Forest).  
- Evaluate performance using AUC, F1, Precision/Recall.  
- Perform feature importance analysis to identify key predictors.

### To Reproduce
```bash
# Clean the data
python scripts/clean_data.py  

# Open EDA Notebook
jupyter notebook notebooks/sprint2_eda.ipynb
