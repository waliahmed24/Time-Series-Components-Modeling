import numpy as np
from scipy.optimize import curve_fit
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from sklearn.metrics import root_mean_squared_error

class Models:
    
    def __init__(self, csv_file):
        # Read time series data from a CSV file
        self.data = pd.read_csv(csv_file)
        self.t = self.data['time'].values 
        self.y = self.data['value'].values

    
    
    def fit_fourier_series(self, n_terms, dominant_freq, amplitude):
        
        # Fourier series function within fit_fourier_series
        def fourier_series(t, *a):
            ret = a[0]  # Constant term
            n_terms = (len(a) - 1) // 2
            for i in range(1, n_terms + 1):
                ret += a[2 * i - 1] * np.cos(2 * np.pi * i * dominant_freq * t) + \
                       a[2 * i] * np.sin(2 * np.pi * i * dominant_freq * t)
            return ret
        
        # Initial guess and bounds for the coefficients
        initial_guess = np.random.rand(2 * n_terms + 1)
        
        # Lambda function to pass the dominant_freq to the curve_fit function
        fourier_func = lambda t, *a: self.fourier_series(t, *a, dominant_freq=dominant_freq)
        
        # Fit the Fourier series to the loaded data
        popt, _ = curve_fit(fourier_func, self.t, self.y, p0=initial_guess)
        
        # Generate predictions for a larger time range
        t_future = np.arange(self.t[0], self.t[-1] + 5, 0.1)  # Extend the time range
        
        # Apply the amplitude scaling factor to the Fourier series
        y_pred = amplitude * self.fourier_series(t_future, *popt, dominant_freq=dominant_freq)
        
        # Calculate the mean squared error (MSE)
        y_pred_mse = amplitude * self.fourier_series(self.t, *popt, dominant_freq=dominant_freq)
        mse = root_mean_squared_error(self.y, y_pred_mse)
        print("MSE of fitted model on train set:", round(mse, 2))
        
        return t_future, y_pred  
