# Student Performance Prediction

This project aims to predict the final grade (`G3`) of secondary school students based on various attributes related to their personal, familial, and academic backgrounds. The dataset used for this project is the Student Performance dataset, which includes information on students' demographics, parental background, school-related factors, lifestyle, and academic performance.

## Project Overview

The goal of this project is to build a regression model that can accurately predict the final grade (`G3`) of students. The project involves the following steps:

1. Exploratory Data Analysis (EDA)
2. Data preprocessing
4. Model building and evaluation
5. Model deployment (optional)

## Project Structure

- **dataset**: Contains the dataset used for the project.
- **deploy**: Contains files related to the deployment of the model.
  - **templates**: HTML templates for the Flask web application.
  - **app.py**: Flask application to serve the model.
  - **log_reg_model.pkl**: Pickle file for the trained linear regression model.
  - **log_reg_scaler.pkl**: Pickle file for the feature scaler.
  - **log_reg_scaler_y.pkl**: Pickle file for the target variable scaler.
  - **requirements.txt**: List of required Python packages for the project.
- **ml-reg-models-hyperparameter.ipynb**: A Jupyter Notebook used to train machine learning models with hyperparameters.
- **ml-reg-models.ipynb**: A Jupyter Notebook used to train machine learning models with default parameters.
- **ml-reg.ipynb**: A Jupyter Notebook performing Exploratory Data Analysis (EDA) and Data Preprocessing.
- **ml-regression.pptx**: Summarizing the project workflow, findings, and conclusions.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- Scikit-learn
- Pandas
- Numpy

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rahul-bhutekar/Data-Science.git
cd Projects/machine-learning-regression/deploy
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r deploy/requirements.txt
```

### Running the Application

1. Navigate to the `deploy` folder:

```bash
cd deploy
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Input the required student data into the web form.
- Click "Predict" to get the predicted final grade (G3) for the student.

## Data Description

The dataset contains the following columns:

- `school`: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
- `sex`: Student's sex (binary: 'F' - female or 'M' - male)
- `age`: Student's age (numeric: from 15 to 22)
- `address`: Student's home address type (binary: 'U' - urban or 'R' - rural)
- `famsize`: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
- `Pstatus`: Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
- `Medu`: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)
- `Fedu`: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)
- `Mjob`: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home', 'other')
- `Fjob`: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home', 'other')
- `reason`: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference, 'other')
- `guardian`: Student's guardian (nominal: 'mother', 'father', 'other')
- `traveltime`: Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, 4 - >1 hour)
- `studytime`: Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, 4 - >10 hours)
- `failures`: Number of past class failures (numeric: n if 1<=n<3, else 4)
- `schoolsup`: Extra educational support (binary: yes or no)
- `famsup`: Family educational support (binary: yes or no)
- `paid`: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
- `activities`: Extra-curricular activities (binary: yes or no)
- `nursery`: Attended nursery school (binary: yes or no)
- `higher`: Wants to take higher education (binary: yes or no)
- `internet`: Internet access at home (binary: yes or no)
- `romantic`: With a romantic relationship (binary: yes or no)
- `famrel`: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
- `freetime`: Free time after school (numeric: from 1 - very low to 5 - very high)
- `goout`: Going out with friends (numeric: from 1 - very low to 5 - very high)
- `Dalc`: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
- `Walc`: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
- `health`: Current health status (numeric: from 1 - very bad to 5 - very good)
- `absences`: Number of school absences (numeric: from 0 to 93)
- `G1`: First period grade (numeric: from 0 to 20)
- `G2`: Second period grade (numeric: from 0 to 20)
- `G3`: Final grade (numeric: from 0 to 20, output target)

## Project Demo

You can view a live demo of the project at [Project Demo Website](https://ml-regression-project.onrender.com/).



## Visualizations

The project includes various visualizations to explore the data and understand the relationships between features. Some of the visualizations include:

- Histograms
- Box plots
- Correlation heatmaps
- Scatter plots

## Model Building
We build and evaluate various regression models, including:

1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression
4. Gradient Boosting Regression
5. Support Vector Regressor

We use techniques like cross-validation and hyperparameter tuning to optimize model performance.

## Model Evaluation
We evaluate the models using metrics such as:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## Authors

- Rahul Bhutekar - [Your GitHub Profile](https://github.com/rahul-bhutekar)

## Acknowledgments

- Dataset provided by UCI Machine Learning Repository.
- Special thanks to the authors of the dataset and to the contributors of the Python libraries used in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
