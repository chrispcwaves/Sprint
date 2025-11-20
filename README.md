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



### Sprint 3: Modeling, Evaluation, and Diagnostics

Sprint 3 focused on building predictive models to identify which gym members are most likely to stay active based on their workout behavior and fitness attributes. After completing the EDA in Sprint 2, the goal for this sprint was to train, evaluate, and compare multiple classification models, along with generating the appropriate diagnostics and visualizations.

### Key Objectives Completed

- Implemented two predictive models:

- Logistic Regression (baseline interpretable model)

- Random Forest Classifier (higher-capacity model)

- Created a baseline classifier for comparison

- Performed a train/validation/test split using stratification

- Scaled features appropriately for Logistic Regression

- Evaluated models using accuracy, precision, recall, and AUC

- Generated ROC curves and confusion matrix diagnostics

- Computed feature importance using Random Forest

- Updated the definition of retention_status to use a 60th-percentile engagement threshold

- Saved all modeling figures in the reports/figures/ folder

Project Files Added in Sprint 3
📘 Notebooks

notebooks/sprint3_eda.ipynb
Contains all modeling code, evaluation, ROC curves, confusion matrix, feature importance, and model comparison plots.
Fully reproducible and documented.


📁 Figures (Saved Automatically)

All high-resolution PNG figures are stored in:

reports/figures/
    feature_importance.png
    model_performance_comparison.png
    roc_curves.png
    confusion_matrix_logreg.png



Modeling Summary
Models Trained

Baseline classifier
Predicts the majority class in the training data.

Logistic Regression

Used StandardScaler

Includes class_weight="balanced"

Max iterations increased to 2000

Random Forest Classifier

300 trees

Balanced class weights

Tuned for validation performance

Performance Overview (Validation Set)
Model	Accuracy	Precision	Recall	AUC
Baseline	~0.60	—	—	—
Logistic Regression	~0.98	~0.95	1.00	~0.999
Random Forest	1.00	1.00	1.00	1.00

These results and their interpretations are discussed in detail in the notebook and final report.

How to Reproduce Sprint 3 Results
1. Install dependencies
pip install -r requirements_dev.txt

2. Run the modeling notebook

Open:

notebooks/sprint3_eda.ipynb


All plots will automatically save to:

reports/figures/

3. Run the models manually 

Inside the notebook, all model blocks are standalone—no external dependencies besides the processed dataset.

Dataset Used

Sprint 3 uses the cleaned dataset generated in Sprint 2:

data/processed/gym_members_cleaned.csv


The notebook recalculates:

engagement_score

retention_status (60th percentile threshold method)

This ensures the modeling is self-contained.

Sprint 4 Preparation

Sprint 3 sets up all core modeling components needed for Sprint 4:

