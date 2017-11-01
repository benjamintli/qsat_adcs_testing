calib = 'data.csv';
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
scatter (cMagX, cMagY, 'MarkerFaceColor', [1 0 0]);
scatter (cMagY, cMagZ, 'MarkerFaceColor', [0 1 0]);
scatter (cMagX, cMagZ, 'MarkerFaceColor', [0 0 1]);
xL = xlim;
yL = ylim;
line([0 0], yL);  %x-axis
line(xL, [0 0]);  %y-axis
hold on

figure (2);
scatter (uMagX, uMagY, 'MarkerFaceColor','y');
scatter (uMagY, uMagZ, 'MarkerFaceColor','m');
scatter (uMagX, uMagZ, 'MarkerFaceColor','c');
xL = xlim;
yL = ylim;
line([0 0], yL);  %x-axis
line(xL, [0 0]);  %y-axis
hold on


