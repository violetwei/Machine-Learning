% main program for Q3 part a
function o= partA()
	stepSize = [0.01; 0.05; 0.1; 0.2];
 
	for i = 1:length(stepSize)
		stepSize(i)
		performHillClimbing(strcat('f1 with step ', num2str(stepSize(i)), " :"), @f1, i, stepSize(i));
	end
end

function out = performHillClimbing(name, f, figureNum, stepSize)
	resultF = zeros(100,3);
	timeToConvergeF = zeros(100, 1);
 
	for i = 1:100
		x = rand()*10;
		y = rand()*10;
		[resultF(i, :), timeToConvergeF(i)] = hillClimbing(f, x, y, stepSize);
	end
	
	t = 1:1:100;
	figure(figureNum);
        stem(t, resultF(:,3));
	title(strcat(name, " Final Value"));
	figure(10 * figureNum); 
        stem(t, timeToConvergeF);
 
	title(strcat(name, " Step to convergence"));
	disp(strcat(name, ' The std of final funciton value is ')), disp(std(resultF(:,3)));
	disp(strcat(name, ' The mean of final function value is ')), disp(mean(resultF(:,3)));
	disp(strcat(name, ' The std of the number of steps to convergence is ')), disp(std(timeToConvergeF));
	disp(strcat(name, ' The mean of the number of steps to convergence is ')), disp(mean(timeToConvergeF)); 
end