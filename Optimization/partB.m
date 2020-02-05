% main program for Q3 part b
function o= partB()
	beamWidth = [2; 4; 8; 16];

	for i = 1:length(beamWidth)
		performHillClimbing(strcat('f2 with beam width ', num2str(beamWidth(i)), ' : '), @f2, beamWidth(i), 0.01, i);
	end 
end

function out = performHillClimbing(name, f, beamWidth, stepSize, figureNum)
	resultF = zeros(100,3);
	timeToConvergeF = zeros(100, 1);
 
	for i = 1:100
		x = rand(beamWidth, 1) * 10;
		y = rand(beamWidth, 1) * 10;
		[resultF(i, :), timeToConvergeF(i)] = localBeaming(f, x, y, stepSize);
	end
 
	t = 1:1:100;
	figure(figureNum);
        stem(t,resultF(:,3));
	title(strcat(name, " The final value"));
	figure(10*figureNum); 
        stem(t,timeToConvergeF);
	title(strcat(name, " step to convergence"));
 
	disp(strcat(name, 'The std of the final function value is ')), disp(std(resultF(:,3)));
	disp(strcat(name, 'The mean of the final function value is ')), disp(mean(resultF(:,3)));
	disp(strcat(name, 'The std of the number of steps to convergence is ')), disp(std(timeToConvergeF));
	disp(strcat(name, 'The mean of the number of steps to convergence is ')), disp(mean(timeToConvergeF)); 
end