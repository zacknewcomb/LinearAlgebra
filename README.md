<h1> NumericalComputation </h1>

NumericalComputation is a Python package for scientific computing

Current Features:
* Computational functions for common linear algebra problems
* Computational functions for solving ODEs
* Computational functions for finding roots of real-valued functions
* Computational functions for integrating single-dimension functions numerically
* Computational functions from research papers in numerical analysis

*Previous Updates Included*:
* (6/5/2021)
  * Add kalmanfilter class, used for tracking in radar along with other uses
    * Very basic update of the kalman filter. Future updates will have a better defined kalman filter.
    * Would like to add extended kalman filter and a possibly an a priori and a posteriori
    * Would also like to add time update equations and measurement update equations
* (1/11/2021)
  * Add linearStability to OneDimAnalysis module
* (1/8-9/2021)
  * Restructre the package
  * Create the OneDimAnalysis module and divide the solve module seperately
    * Add the stability and fixedPoint methods, for finding qualitative info on ODEs
  * Improve Secant and Newton method in roots module
* (1/5/2021)
  * Created integration module with numerical integration methods
    * Trapezoid method
    * Midpoint method
* (1/3/2021) 
  * Added Heun Method to solveODE module
  * Added Least Squares Solution method to linearAlgebra module
  * Added custom error messages to linearAlgebra module
  * Modified all solveODE methods to return both the step value and the function value after the step performed by method
