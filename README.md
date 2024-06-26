﻿# GolfWinsPredictor
This Python project implements a highly accurate predictive model using machine learning to analyze data extracted from an SQLite database on PGA Tour player performance. The model predicts the number of victories based on various player statistics. The predictions are visualized through an interactive scatterplot against the actual number of victories.

## Clone the repository:

```bash
git clone https://github.com/yourusername/pga-tour-predictive-model.git
```
## Navigate to the project directory:

``` bash
cd GolfWinsPredictor
```
## Dependencies
- pandas
- numpy
- scikit-learn
- matplotlib
- mplcursors
- make sure to have python installed on your computer 
## Install dependencies:

``` bash
pip install pandas numpy scikit-learn matplotlib mplcursors
```
## Connect to the SQLite database:

- Ensure you have the SQLite database (golf_database.db) accessible.
- Run the Python script:

``` bash
python predictions.py
 ```

## Predictive Model
- The model uses a MLP regression algorithm to predict the number of victories based on various player statistics.
- Missing values in the dataset are imputed using the mean strategy.
## Visualization
- The scatterplot visually represents the relationship between actual wins and predicted wins.
- Each point on the plot corresponds to a PGA Tour player, with player names annotated for clarity.
