function punts = generaPuntsCercleEntorn(x,y,R)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Genera punts (concretament n) d'un cercle de centre (x,y) i radi R
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 1000;
angles = linspace(0,2*pi,n);
punts = [];
for i=angles
    punts = [punts; R*cos(i)+x R*sin(i)+y];
end
