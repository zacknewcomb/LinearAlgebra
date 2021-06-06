''' 
This class is built with the textbook "Optimal State Estimation" by Dr. Dan Simon of Cleveland State University.
'''

import numpy as np

class KalmanFilter:
    
    def __init__(self, StateTransMat: numpy.array, StateToMeasMat: numpy.array, MeasNoiseCovMat: np.array,
                 StateNoiseCovMat: np.array, initialErrorCovMat: np.array, initialState: np.array):
        
        self.StateTransitionMatrix = StateTransMat
        self.StateToMeasurementMatrix = StateToMeasMat
        self.MeasurementNoiseCovarianceMatrix = MeasNoiseCovMat
        self.StateNoiseCovarianceMatrix = StateNoiseCovMat
        self.currentState = initialState
        self.EstimationErrorCovarianceMatrix = initialErrorCovMat
        
    def computeKalmanGain(self):
        # Using Eq (5.15) on Pg 127
        P = self.EstimationErrorCovarianceMatrix
        H = self.StateToMeasurementMatrix
        R = self.MeasurementNoiseCovarianceMatrix
        KalmanGain = P @ np.transpose(H) @ np.inv(R)
        self.KalmanGain = KalmanGain
        
    def computeEstErrorCov(self):
        # Using Eq (5.15) On Pg 127
        I = np.identity(len(self.EstimationErrorCovarianceMatrix))
        K = self.KalmanGain
        H = self.StateToMeasurementMatrix
        Pkminus1 = self.EstimationErrorCovarianceMatrix
        R = self.MeasurementNoiseCovarianceMatrix
        self.EstimationErrorCovarianceMatrix = (I - K @ H) @ Pkminus1 @ np.transpose(I - K @ H) + K @ R @ np.transpose(K)
        
    # Input:
    # np.array y: The new measurement used to compute next state
    def updateState(self, y: np.array):
        prevState = self.currentState
        K = self.KalmanGain
        H = self.StateToMeasurementMatrix
        self.currentState = prevState + K @ (y - H @ prevState)
        