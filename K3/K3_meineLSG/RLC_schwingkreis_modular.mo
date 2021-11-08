model RLC_schwingkreis_modular
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {0, -50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Inductor inductor(L = 9e-3)  annotation(
    Placement(visible = true, transformation(origin = {20, -10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Capacitor capacitor(C = 1000e-6)  annotation(
    Placement(visible = true, transformation(origin = {60, -10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 2, freqHz = 1)  annotation(
    Placement(visible = true, transformation(origin = {-40, -10}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Electrical.Analog.Basic.Resistor resistor(R = 20)  annotation(
    Placement(visible = true, transformation(origin = {-10, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(sineVoltage.p, inductor.n) annotation(
    Line(points = {{-40, -20}, {-40, -40}, {20, -40}, {20, -20}}, color = {0, 0, 255}));
  connect(inductor.n, capacitor.n) annotation(
    Line(points = {{20, -20}, {20, -40}, {60, -40}, {60, -20}}, color = {0, 0, 255}));
  connect(sineVoltage.n, resistor.p) annotation(
    Line(points = {{-40, 0}, {-40, 20}, {-20, 20}}, color = {0, 0, 255}));
  connect(resistor.n, inductor.p) annotation(
    Line(points = {{0, 20}, {20, 20}, {20, 0}}, color = {0, 0, 255}));
  connect(resistor.n, capacitor.p) annotation(
    Line(points = {{0, 20}, {60, 20}, {60, 0}}, color = {0, 0, 255}));

annotation(
    uses(Modelica(version = "3.2.2")));
end RLC_schwingkreis_modular;