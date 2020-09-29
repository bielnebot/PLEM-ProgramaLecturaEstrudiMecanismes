function dibuixaRecta(x,y,angle,factor)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Dibuixa una recta que passa per (x,y)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if abs(abs(angle)-pi/2) > 0.01  
    m = tan(angle);
    line([x-1*factor x+1*factor],[y-m*factor y+m*factor],"color","k","linewidth",2,"linestyle","--"); hold on;
    plot(x,y,"o","markersize",3,'LineWidth',2,'MarkerEdgeColor','r','MarkerFaceColor',[1 1 1]);
else
    line([x x],[y+3*factor y-3*factor],"color","k","linewidth",2,"linestyle","--"); hold on;
    plot(x,y,"o","markersize",3,'LineWidth',2,'MarkerEdgeColor','r','MarkerFaceColor',[1 1 1]);
end
axis equal
end