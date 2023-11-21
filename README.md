# GolfWinsPredictor
This Python project implements a highly accurate predictive model using machine learning to analyze data extracted from an SQLite database on PGA Tour player performance. The model predicts the number of victories based on various player statistics. The predictions are visualized through an interactive scatterplot.

## Clone the repository:

```bash
git clone https://github.com/yourusername/pga-tour-predictive-model.git
```
## Navigate to the project directory:

``` bash
cd GolfWinsPredictor
```
## Dependencies
Python 3
pandas
numpy
scikit-learn
matplotlib
mplcursors

## Install dependencies:

``` bash
pip install pandas numpy scikit-learn matplotlib mplcursors
```
## Connect to the SQLite database:

Ensure you have the SQLite database (golf_database.db) accessible.
Run the Python script:

``bash
python predictions.py ```

## Predictive Model
The model uses a linear regression algorithm to predict the number of victories based on various player statistics.
Missing values in the dataset are imputed using the mean strategy.
## Visualization
The scatterplot visually represents the relationship between actual wins and predicted wins.
Each point on the plot corresponds to a PGA Tour player, with player names annotated for clarity.
