model A3
  Modelica.Electrical.Analog.Basic.Resistor resistor1(R = 20)  annotation(
    Placement(visible = true, transformation(origin = {-12, 40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor capacitor1(C = 1000e-6, v(start = 0))  annotation(
    Placement(visible = true, transformation(origin = {26, 18}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Inductor inductor1(L = 9e-3, i(start = 0))  annotation(
    Placement(visible = true, transformation(origin = {48, 18}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage1(V = 2, freqHz = 1)  annotation(
    Placement(visible = true, transformation(origin = {-48, 18}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-48, -8}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(capacitor1.p, resistor1.n) annotation(
    Line(points = {{26, 28}, {26, 28}, {26, 40}, {-2, 40}, {-2, 40}}, color = {0, 0, 255}));
  connect(resistor1.n, inductor1.p) annotation(
    Line(points = {{-2, 40}, {48, 40}, {48, 28}, {48, 28}}, color = {0, 0, 255}));
  connect(capacitor1.n, sineVoltage1.n) annotation(
    Line(points = {{26, 8}, {-48, 8}, {-48, 8}, {-48, 8}}, color = {0, 0, 255}));
  connect(inductor1.n, capacitor1.n) annotation(
    Line(points = {{48, 8}, {26, 8}, {26, 8}, {26, 8}}, color = {0, 0, 255}));
  connect(resistor1.p, sineVoltage1.p) annotation(
    Line(points = {{-22, 40}, {-48, 40}, {-48, 28}, {-48, 28}}, color = {0, 0, 255}));
  connect(ground1.p, sineVoltage1.n) annotation(
    Line(points = {{-48, 2}, {-48, 2}, {-48, 8}, {-48, 8}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.2")),
    experiment(StartTime = 0, StopTime = 2, Tolerance = 1e-6, Interval = 0.004));
end A3;
