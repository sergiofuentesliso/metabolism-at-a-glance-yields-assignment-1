import pytest
_ = 123456789  # just  wrong number, please ignore

# Black box model

# 1. Calculate the specific yield coefficients (C-mol) for all products.

# Add your calculations here ...
Y_se=((10*(46.07*0.5)**-1)/(abs(-20)*(180*(1/6))**-1)) #[(10g_EtOH/L)*((46.07g_EtOH/mol)/2(Cmol))**-1]/[(abs(-20)g_Glu/L)*(180g_EtOH/mol)/6(Cmol)]
Y_se
Y_sx=((2.74-0.02)*(24.6)**-1)/(abs(-20)*(180*(1/6))**-1) #same procedure, different data. In this case we divide by 1 (or do nothing to them) those 24.6 gDW/mol to convert into Cmoles
Y_sx
Y_sg=(1.54*((92.09/3)**-1)/(abs(-20)*(180*(1/6))**-1))
Y_sg
# Assign your solutions to the following variables (replace _ with your solutions)
Y_sx = 0.1658536585365854
Y_se = 0.6511829824180595
Y_sg = 0.07525247040938214

def test_Y_sx():
    assert Y_sx == pytest.approx(0.166, .01)

def test_Y_se():
    assert Y_se == pytest.approx(0.652, .01)

def test_Y_sg():
    assert Y_sg == pytest.approx(0.075, .01)
  

# 2. Calculate the carbon balance.

# Add your calculations here ...
co2_yield_cmol = 1 - Y_se-Y_sg-Y_sx
co2_yield_cmol
# Assign your solution to the following variable (replace _ with your solution)
carbon_balance = 0.10771088863597295 # c-mol-CO2 / c-mol-Glc

def test_carbon_balance():
    assert carbon_balance == pytest.approx(0.106, 0.01)
    

# 3. Assuming that CO2 is the only missing product, calculate how much CO2 was produced in the fermentation.

# Add your calculations here ...
co2=0.10771088863597295*(2/3)*(44) # co2_produced = 0.10771088863597295 (CmolCO2/CmolGlu)*(2/3 cmolGlu/L)*(44 gCO2/CmolCO2)


# Assign your solution to the following variable (replace _ with your solution)
co2_produced = 3.1595193999885396 #g/L

def test_co2_produced():
    assert co2_produced == pytest.approx(3.129, 0.01)
