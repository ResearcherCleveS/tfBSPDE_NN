# $\sf tfBSPDE \ NN$
## $\sf Time \ Fractional \ Black \ Scholes \ Neural \ Network$
[Streamlit app](https://quant-research-project.streamlit.app)

Let $\sf U(S, t)$ be the price option as a function of the stock price $\sf S$ and time $\sf t \in [0, T]$. Let $\sf \sigma$ be the volatility stock and $\sf r$ the risk-free interest rate. Then, the governing classical BSPDE is

## $\sf \frac{\partial U}{\partial t} + \frac{1}{2}\sigma^2S^2\frac{\partial^2U}{\partial S^2}+rS\frac{\partial U}{\partial S}-rU = 0.$

If we consider a non dividend paying stock whose price at time $\sf t$ is given by $S(t)$, then the stock price dynamics under a fractal stochastic process are 

## $\sf dS(t) = rS(t)dt + \sigma SdB_{\alpha}(t).$

Employing Maruyama representation, $\sf dB_{\alpha}(t) = B(t)(dt)^{\frac{\alpha}{2}}$, the stock price dynamics can be represented by

## $\sf  dS(t) = rS(t)dt + \sigma SdB_{\alpha}(t)(dt)^{\frac{\alpha}{2}},$

where $\sf B(t)$ is a standard Brownian motion process. Using stick price defined $\sf (1)$, we arrive at our tfBSPDE for non-dividend paying stocks

## $\sf U_t^\alpha + (rSU_s - rU)\frac{t^{1-\alpha}}{\Gamma(2-\alpha)}+\frac{\Gamma(1+\alpha)}{2}\sigma^2S^2U_{SS} = 0, \ 0<\alpha<1,$

subject to the following initial and boundary conditions

## $\sf U(S, T) = \max(K-S, 0),$
## $\sf U(0, t) = Ke^{-rt},$
## $\sf \lim_{S\rightarrow\infty}U(S, 0) = 0.$
