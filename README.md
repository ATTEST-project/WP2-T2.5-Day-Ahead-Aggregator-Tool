# Inputs

## Building parameters
 - Electrical heater - Installed	0 - no, 1 - yes
 - Electrical heater - Maximum power	kW
 - Electrical heater - Efficiency/COP	-
 - Gas heater - Installed	0 - no, 1 - yes
 - Gas heater - Maximum power	kW
 - Gas heater - Efficiency/COP	-
 - PV - Installed	0 - no, 1 - yes
 - PV - Maximum power	kW
 - Storage	- Installed	0 - no, 1 - yes
 - Storage - Maximum power	kW
 - Storage - Maximum SOC	kWh
 - Storage - Mininum SOC	kWh
 - Storage - Initial SOC	kWh
 - Storage - Efficiency	-
 - District heating - Installed	0 - no, 1 - yes
 - District heating - Maximum power	kW
 - Gas - Load	0 - no, 1 - yes
 - Thermal model building	- Resistance	oC /kW
 - Thermal model building - Capacity	kWh/ oC
 - Thermal model building - Initial temperature	oC
 - Thermal model building - Maximum and mininum temperature per hour	oC
 - Energy consumption - Electricity consumption	kWh
 - Energy consumption - Gas consumption	kWh
 - Energy consumption - Heat consumption	kWh

## Electrical networks paramters
 - Branches - Branch connections	-
 - Branches - R	Ω
 - Branches - X	Ω
 - Branches - Branch limits	A
 - Buses - Voltage limits	p.u.
 - Buses - Reference bus number	-
 - Buses - Reference bus voltage	p.u.
 - Buses - Load/building/resource connections	-
 - Buses - System base	MVA

## Gas networks parameters
 - Pipeline - Pipeline connections	-
 - Pipeline - Length	m
 - Pipeline- Diameter	mm
 - Buses - Pressure limit	Bar
 - Buses - Reference bus number	-
 - Buses - Load/building/resource connections	-

## Heat networks parameters
 - Load - Location	-
 - Load - Return temperature	oC
 - Generator - Type	w – electricity , g - gas
 - Generator - Electrical, gas and heat bus connection	-
 - Generator - Supply node temperature	oC
 - Generator - Power limits	kW
 - Generator - Efficiency/COP	-
 - Pipeline - Connections	-
 - Pipeline - Length	m
 - Pipeline - Diameter	mm
 - Pipeline - Heat transfer coefficient	W/ oC
 - Pipeline - Supply pipeline temperature limits	oC
 - Pipeline - Return pipeline temperature limits	oC
 - Pipeline - Pipeline mass flow limits	kg/s
 - Pipeline - Ambient temperature	oC
 - Pipeline - Friction of pipeline	-
 - Buses - Supply bus temperature limits	oC
 - Buses - Return bus temperature limits	oC
 - Buses - Pressure limits	Pa
 - Buses - Load/building/resource connections

## Weather parameters
 - Solar profile	%
 - Outside temperature	oC

## Prices
 - Electricity - Day-ahead energy prices	€/MWh
 - Electricity - Secondary reserve day-ahead energy prices – upward and downward	€/MWh
 - Electricity - Secondary reserve ratios – upward and downward	%
 - Gas - Day-ahead energy prices	€/MWh

# Outputs

 - Electricity - Energy bid  (per hour, per electrical bus)	MWh
 - Electricity - Upward secondary reserve band bid  (per hour, per electrical bus)	MW
 - Electricity - Downward secondary reserve band bid  (per hour, per electrical bus)	MW
 - Gas - Energy bid  (per hour, per gas node)	MWh

# How to Run

Run 
```sh
main.py
```









