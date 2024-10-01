# Time-Series Components Modeling

This repository contains functions for modeling various components of a time series, such as **trend** and **seasonality**. When a time series exhibits periodicity—whether daily, weekly, or monthly—we aim to find and fit models that can explain these patterns in the training data and generalize to the test data.

## Time Series

A **time series** is a sequence of data points collected or recorded at successive intervals over time. This type of data is ordered chronologically, allowing for the analysis of trends, seasonal patterns, and changes over time.

## Motivation

In theory, a time series can be decomposed into several components to better understand how the data behaves over time. These components include:

- **Trend**
- **Seasonality**
- **Cyclicality**
- **Noise (Randomness)**

By modeling these components separately, we can enhance the interpretability of the time series data. In this project, the main focus will be on modeling **trend** and **seasonality**, as these two components often explain the majority of the variation in a time series. However, this may not always be the case for all datasets.

---

## Time Series Components

### 1. Trend

The **trend** represents the long-term movement or direction in the data over time. It shows whether values are increasing, decreasing, or remaining stable, irrespective of short-term fluctuations.

- **Example**: A steady rise in global temperatures over several decades due to climate change.

### 2. Seasonality

**Seasonality** refers to repeating patterns or cycles that occur at fixed, regular intervals, such as yearly, monthly, or weekly. These patterns are often driven by predictable factors, such as weather changes or holidays.

- **Example**: Retail sales typically peak every December due to holiday shopping.

### 3. Cyclicality

**Cyclicality** represents fluctuations that occur over longer, irregular periods, often related to external factors like economic cycles. Unlike seasonality, cyclicality does not have a fixed frequency.

- **Example**: Economic recessions that happen every few years, but at unpredictable intervals.

### 4. Noise (Randomness)

**Noise** represents random or unpredictable variations in the data that cannot be explained by trend, seasonality, or cyclicality. Noise is considered the "unstructured" part of the time series.

- **Example**: Sudden stock market fluctuations due to unexpected news.

---

## Visual Illustration of Components

<img width="500" alt="image" src="https://github.com/user-attachments/assets/8cbcd10d-721b-4772-8355-0188c612fbb0">

---

