<h1> NumericalComputation </h1>

NumericalComputation is a Python package for scientific computing

Current Features:
* Computational functions for common linear algebra problems
* Computational functions for solving ODEs
* Computational functions for finding roots of real-valued functions
* Computational functions for integrating single-dimension functions numerically
* Special functions from recent research papers in numerical analysis

*Previous Updates Included*:
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

*Next Updates Will Include*:
* Changes to help remove the dependency on NumPy
* Cleaner, more consistent code in linearAlgebra module

Future features:
* Support for additional common linear aglebra problems
* More ODE related computations
* Fourier Transform Computations
* New algorithms from accepted research papers
* More Custom errors
* More efficient code for already existing functions
