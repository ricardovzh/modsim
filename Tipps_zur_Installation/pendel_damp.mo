model pendel_damp
  Real phi(start=pi/4);
  Real phi_dot;
  parameter Real l=1.0;
  parameter Real d=0.3;
  constant  Real g=9.81;
  constant  Real pi=Modelica.Constants.pi;
equation
  der(phi)=phi_dot;
  der(phi_dot) + d*phi_dot + g*phi/l=0;
  annotation(
    uses(Modelica(version = "3.2.2")),
    experiment(StartTime = 0, StopTime = 1, Tolerance = 1e-6, Interval = 0.002));
end pendel_damp;