# eda_proyecto
Luego de crear el diseño dut en OpenLane:
En el archivo synth_and_metrics.py cambie el path de OpenLane al suyo.
En una terminal aparte abra el container de OpenLane.
Luego de esto debería poder correr eda_flow.py
El resultado final es el archivo design_space.txt que tiene las métricas para el dut usando los diferentes adders.
## adder.py
Este archivo contiene la base de  datos de adders posibles. El flujo (eda_flow) selecciona uno de estos (por medio del archivo adder_selection) para la siguiente corrida.
## adder_builder.py
Este script genera el archivo built_adder.py que es usado por el dut para los adders, basado en adder_selection (lo extrae de la base de datos).
## py_to_verilog.py
Este script convierte el dut (que en este momento ya contiene el adder seleccionado) a verilog.
## synth_and_metrics.py
Este script toma el dut.v, lo copia en el diseño de OpenLane y lo sintetiza, luego extrae las métricas de área, potencia y delay y las
escribe al archivo metrics_ouput.csv.
## eda_flow.py 
Representa el flujo total, en este caso simplemente prueba todos los adders de la base de datos en el dut. Genera el archivo design_space.txt que tiene las métricas para cada caso en secuencia.
