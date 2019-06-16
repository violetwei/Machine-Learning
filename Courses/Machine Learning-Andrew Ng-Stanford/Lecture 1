*Lecture 1.1 Introduction - What is machine learning?*

This course teaches various different types of learning algorithm

Machine Learning Definition
Arthur Samuel(1959) 
Machine Learning: Field of study that gives computers the ability to learn without being explicityly programmed.

Tom Mitchell(1998) Well-posed Learning Problem: 
A computer program is said to learn from experience E with respect to some task T and some performance measure P,
if its performance on T, as measured by P, improves with experience E.

Suppose your email program watches which emails you do or do not mark as spam,
and basaed on that learns how to better filter spam. What is the task T in this setting?
Classifiying emails as spam or not spam. -> task T
Watching you label emails as spam or not spam. -> experience E 
The number (or fraction) of emails correctly classified as spam/not spam. -> performance measure P 

Machine learning algorithms:
- Supervised learning
- Unsupervised learning

Others: Reinforcement learning, recommender systems

Also talk about: Practical advice for applying learning algorithms



*Lecture 1.2 Supervised Learning Introduction*

Housing price prediction (Collect datasets)

Supervised Learning  "right answers" given
Regression: Predict continuous valued output (price)

Breast cancer (malignant, benign)
Classification: Discrete valued output (0 or 1)
Age / Tumor Size   [-> Features]
- Clump Thickness    - Uniformity of Cell Size    - Uniformity of Cell Shape  ...

Suppose you're running a company, and you want to develop learning algorithms to address each of two problems.
Problem 1: You have a large inventory of identical items. You want to predict how many of these items will sell over the next 3 months.
Problem 2: You'd like software to examine individual customer accounts, and for each account decide if it has been hacked/compromised.

Should you treat these as classification or as regression problems?
Treat problem 1 as a regression problem, problem 2 as a classification problem.



*Lecture 1.3 Unsupervised Learning Introduction*

Organize computing clusters
Social network analysis
(discover) Market segmentation [Group customers]
Astronomical data analysis

Cocktail party problem algorithm
[W,s,v] = svd((repmat(sum(x.*x,1),size(x,1),1).*x)*x');
Speaker #1   Microphone #1   Output #1
Speaker #2   Microphone #2   Output #2


Of the following examples, which would you address using an Unsupervised learning algorithm?

Given email labeled as spam/not spam, learn a spam filter.   -> Supervised Learning algorithm
Given a set of news articles found on the web, group them into set of articles about the same story.   -> Unsupervised Learning algorithm
Given a database of customer data, automatically discover market segments and group customers into different market segments.  -> Unsupervised Learning algorithm
Given a dataset of patients diagnosed as either having diabetes or not, learn to classify new patients as having diabetes or not.  -> Supervised Learning algorithm
