model pt1_step
  Modelica.Blocks.Continuous.FirstOrder firstOrder1 annotation(
    Placement(visible = true, transformation(origin = {10, 2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant const annotation(
    Placement(visible = true, transformation(origin = {-40, 2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(const.y, firstOrder1.u) annotation(
    Line(points = {{-28, 2}, {-4, 2}, {-4, 2}, {-2, 2}}, color = {0, 0, 127}));

annotation(
    uses(Modelica(version = "3.2.2")),
    experiment(StartTime = 0, StopTime = 1, Tolerance = 1e-6, Interval = 0.002));end pt1_step;