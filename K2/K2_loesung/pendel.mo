model pendel
  Real phi(start=pi/4);
  Real phi_dot;
  parameter Real l=1.0;
  constant  Real g=9.81;
  constant  Real pi=Modelica.Constants.pi;
equation
  der(phi)=phi_dot;
  der(phi_dot) + g*phi/l=0;
  annotation(
    uses(Modelica(version = "3.2.2")));
end pendel;