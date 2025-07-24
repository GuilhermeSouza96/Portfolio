# Datasets for Regression Analysis Projects

This repository contains the datasets used in the accompanying Jupyter notebooks for linear regression analysis. Below is a description of each dataset.

---

## 1. Hotel Pricing Dataset (`hoteis.csv`)

This dataset contains features related to hotels and is used to build a model for predicting hotel prices.

### Columns

* `Estrelas`: (Integer) The star rating of the hotel, from 1 to 5.
* `ProximidadeTurismo`: (Float) A metric representing the proximity to tourist attractions. A higher value likely indicates a greater distance.
* `Capacidade`: (Integer) The capacity of the room (e.g., number of people).
* `Preco`: (Float) The price of the hotel stay. This is the **target variable** in the analysis.

### Context

This dataset is used in the first part of the notebook to demonstrate and compare simple and multiple linear regression models. The goal is to determine how features like star rating, proximity, and capacity influence the price.

---

## 2. Combined Cycle Power Plant Dataset (`usina.csv`)

This dataset contains data collected from a Combined Cycle Power Plant over 6 years (2006-2011) when the power plant was set to work with a full load.

### Columns

* `AT`: (Float) Ambient Temperature in degrees Celsius.
* `V`: (Float) Exhaust Vacuum in cm Hg.
* `AP`: (Float) Ambient Pressure in millibar.
* `RH`: (Float) Relative Humidity in percent.
* `PE`: (Float) Net hourly electrical energy output in MW. This is the **target variable** in the analysis.

### Context

This dataset is used in the second part of the notebook to build a multiple linear regression model. The analysis includes data splitting (training and testing), model fitting, and performing diagnostics for multicollinearity (using VIF) and residual analysis.

---

## Usage

These datasets are intended for educational and demonstration purposes within the associated Jupyter notebooks. Feel free to use them to practice data analysis and regression modeling techniques.
