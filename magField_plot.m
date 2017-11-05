calib = 'dataCalibrated.csv';
uncalib = 'dataUncalibrated.csv'
calibrated = csvread (calib);
uncalibrated = csvread (uncalib);

cMagX = calibrated (:,1);
cMagY = calibrated (:,2);
cMagZ = calibrated (:,3);

uMagX = uncalibrated (:,1);
uMagY = uncalibrated (:,2);
uMagZ = uncalibrated (:,3);

xL = xlim;
yL = ylim;
line([0 0], yL);  %x-axis
line(xL, [0 0]);  %y-axis

figure (1);
hold on
title ('Calibrated Magnetometer Readings');
scatter (cMagX, cMagY, 'MarkerFaceColor', 'r');
scatter (cMagY, cMagZ, 'MarkerFaceColor', 'g');
scatter (cMagX, cMagZ, 'MarkerFaceColor', 'b');
xL = xlim;
yL = ylim;
line([0 0], yL);  %x-axis
line(xL, [0 0]);  %y-axis
axis equal;

figure (2);
hold on
title('Uncalibrated Magnetometer Readings');
scatter (uMagX, uMagY, 'MarkerFaceColor','r');
scatter (uMagY, uMagZ, 'MarkerFaceColor','g');
scatter (uMagX, uMagZ, 'MarkerFaceColor','b');
xL = xlim;
yL = ylim;
line([0 0], yL);  %x-axis
line(xL, [0 0]);  %y-axis
axis equal;


