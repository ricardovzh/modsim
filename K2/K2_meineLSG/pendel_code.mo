model pendel_code
  Real phi(start = pi / 4);
  Real phi_dot;
  parameter Real l = 1.0;
  constant Real g = 9.81;
  constant Real pi = Modelica.Constants.pi;
equation
  der(phi) = phi_dot;
  der(phi_dot) + g * phi / l = 0;
  annotation(
    uses(Modelica(version = "3.2.2")),
    experiment(StartTime = 0, StopTime = 5, Tolerance = 1e-06, Interval = 0.01));
end pendel_code;
