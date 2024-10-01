# Time-Series-Components-Modeling
This repository contains different functions and how they model different components of a time series, such as trend and seasonality. If a time seris has some prediocity such as daily, weekly or monthly seasonaility, we want to be able to find and fit relevant models that explain this seasonal pattern in the training data as well as can generalize to the test data.

## Time Series
A time series is a sequence of data points collected or recorded at successive intervals over a period of time. This type of data is characterized by its chronological order, allowing for the analysis of trends, patterns, and changes over time.

## Motivation
In theory, a time series can be broken down into several components to better understand how the data varies over time. These components include trend, seasonality, cyclicality, and noise (randomness). Below are descriptions of each component. A time series may exhibit all or only some of these components. By modeling each of these components separately, we can improve the explainability of what is happening with the data. In this project, the main focus will be on modeling trend and seasonality, as most of the variation in a time series is often explained by these two components, though this may not always be the case.

#### Trend
The long-term movement or direction in the data over time. It shows the overall increase or decrease in the values, regardless of any short-term fluctuations.

Example: A steady rise in temperature over several decades due to climate change.

#### Seasonailty
Repeating patterns or cycles that occur at regular intervals within a fixed period (e.g., yearly, monthly, weekly). This is often driven by predictable factors like weather, holidays, or specific business cycles.

Example: Retail sales increasing every December due to holiday shopping.

#### Cyclicality
Fluctuations that occur over longer, irregular periods and are often related to economic or business cycles. These patterns don’t have a fixed frequency like seasonality and can be unpredictable.

Example: Economic recessions occurring every few years, but not at regular intervals.

#### Noise
The random or unpredictable variations in the data that cannot be explained by the other components (trend, seasonality, or cyclicality). Noise represents the "unstructured" part of the time series.

Example: Sudden short-term stock market changes due to unexpected news or events.

## Visual Illustration of Components

<img width="500" alt="image" src="https://github.com/user-attachments/assets/8cbcd10d-721b-4772-8355-0188c612fbb0">


