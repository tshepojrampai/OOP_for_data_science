# Class: ErrorCalculator 
class ErrorCalculator:

    def __init__(self, y, y_pred):

        self.y          =   np.array(y)       
        self.y_pred     =   np.array(y_pred)  


    def get_residuals(self):

        residuals = self.y  - self.y_pred
        return residuals

    def get_standardised_residuals(self):

        standardised_residuals = self.get_residuals() / (self.get_residuals()/std())
        return standardised_residuals

    def get_mse(self):

        mse = np.square(np.subtract(self.y, self.y_pred)).mean()
        return mse

    def get_rmse(self):

        rmse = np.sqrt(((self.y_pred - self.y)**2).mean())
        return rmse

    def error_summary(self):
        min_standard = min(self.Standard)
        max_standard = max(self.Standard)
        min_rmse = min(self.rmse)
        max_rmse = max(self.rmse)
        mse_min = min(self.mse)
        mse_max = max(self.mse)
        print(f'standard residual: {min_standard}')
        print(f'standard residual: {max_standard}')
        print(f'min rmse: {min_rmse}')
        print(f'max rmse: {max_rmse}')

#Class: Plotter
class Plotter():
    def __init__(self,y_test,y_pred):
        self.y_test = y_test
        self.ypred = y_pred
    
    def run_calculations(self):
        return self.y_test - self.y_pred
    
    def plot(self):
        plt.hist(self.y_test - self.ypred)
        plt.title('Residuals Plot for predictions')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        return plt.show()

# Class:  histogram plotter
class HistogramPlotter(Plotter):
    def __init__(self, y_test,y_pred):
        Plotter.__init__(self, y_test, y_pred)


class ScatterPlotter(Plotter):
    def __init__(self, y_test, y_pred):
        Plotter.__init__(self, y_test, y_pred)

    def plot(self):
        chart = pd.DataFrame({"y_test": self.y_test, "y_predicted": self.y_pred})
        chart.plot.scatter(x="y_test", y="y_predicted", c="DarkBlue")
        plt.title("Predicted vs Actual values")
        plt.xlabel("Actual values")
        plt.ylabel("Predicted Values")
        return plt.show()
