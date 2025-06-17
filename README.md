# Online Retail Item Popularity Analyzer

This project provides a simple data analysis tool to identify the most popular retail items from the **Online Retail dataset**. It supports global, country-wise, and month-wise popularity analysis and visualization.

## Features

- **Global Popular Items**: Displays the top 10 items sold globally.
- **Country-wise Popular Items**: Identifies the most sold item per country.
- **Month-wise Popular Items**: Highlights the most sold item for each month.
- **Interactive Prediction**: Users can input a country and month to get the most popular item for that combination.
- **Bar Charts**: Visual representation of globally popular items.

## Dataset

The script uses the [Online Retail dataset](https://archive.ics.uci.edu/ml/datasets/online+retail), a transactional data set of a UK-based and registered non-store online retail company.

> Make sure the dataset is downloaded and saved as `OnlineRetail.csv` in the correct path (update the path if needed).

## Requirements

Install the required libraries using pip:

```bash
pip install pandas seaborn matplotlib
