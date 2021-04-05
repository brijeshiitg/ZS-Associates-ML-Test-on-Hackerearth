## Predict the Building Permission Category

#### Problem Description
Nowadays, we are living in a concrete world, tall and small buildings here and there, everywhere. But some of them are constructed without any proper permission or documents, while some of the genuine building get stuck due to permission delay issues, etc. Here's a dataset of building permissions, which consists application date, expiration date, permission granted or not, location, description etc. Based on all these features given you have to predict which category does the building permission fall into. There are typically 5 categories:

1. Single Family / Duplex
2. Commercial
3. Multifamily
4. Institutional
5. Industrial

You have to predict the column "Category".

### Data Description
The columns in the data are described as follows:

| SI.No.| Column Label |Column Description                           |
|---|---|---|
|1|Application/Permit Number|The Tracking number used to refer to this application or permit record in various Seattle DCI tracking systems.|
|2|Permit Type|Type of activity covered by the permit.|
|3|Address|Street address of the work site.|
|4|Description|Brief description of the work that will be done under this permit. This is subject to change prior to issuance of the permit, but generally more stable if an issue date exist. Very long descritpions have been truncated.|
|5|Action Type|Subclassification for type of work being proposed. Valid choice will vary depending on the permit type.|
|6|Work Type|An indicator of the complexity of the project proposed.Easier projects can be issued without plan review; more complex projects generally require plan submittal and review.|
|7|Applicant Name|The name of the person of company listed on the application as the "primary applicant". This may be the property owner, contractor, design professional, or other type of agent.|
|8|Application Date|The date the application was accepted as a complete submittal. If no Application Date exists this means the application is in a very early stage.|
|9|Issue Date|The date the application was issued as a valid permit. If an Application Date exist but no Issue Date exists, this generally means the application is still under reviews.|
|10|Final Date|The date the permit had all its inspection completed. If an Issue Date exists but no Final Date exists, this generally means the permit is still under inspection.|
|11|Expiration Date|The date the appliation is due to expire. Generally, this is the date by which work is supposed to be completed (baring renewals or further extensions). If no Expiration Date exists, this generally means the application has not been issued yet.|
|12|Status|The current status is the application/review/inspection lifecycle. Indicates the last process step that was fully completed.|
|13|Contractor|Contractor(s) who are associated with this permit.|
|14|Permit and Complaint Status URL| Link to view full details and current status information about this permit at Seattle DCI's website.|
|15|Master Use Permit|A Master Use/Land Use Permit is required before some building permits to make decision about site-specif factors of the project, such as environmental impacts of neighborhood desing considerations.|
|16|Latitude|Latitude of the worksite where permit activity occurs. May be misssing for a small number of permits considered "Unaddressable".|
|17|Longitude|Longitude of the worksite where permit activity occurs. May be missing for a small number of permits considered "Unaddressable.|
|18|Location|Mapping coordinates for the permit address.|
|19|Categry|The broad category of use or occupancy for the building where work is proposed. Valid choices are Commercial, Industrial, Institutional, Multifamily, and Single Family/Duplex. Mixed use structures are generally represented as Commercial.|

### Submission
The submission csv has to be submitted in the following format:
|Application/Permit Number, Category|
|---|
|6425384, SINGLE FAMILY / DUPLEX|
|6496502, SINGLE FAMILY / DUPLEX|
|6622347, SINGLE FAMILY / DUPLEX|
|6565685, SINGLE FAMILY / DUPLEX|
|6487370, SINGLE FAMILY / DUPLEX|

### Evaluation
The submission will be evaluated based on F1 Score with 'weighted' average. For more information on this metric, [click here.](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)

### Solution:
To solve this problem you will have to follow following steps:

Step 1: Inspect the data to find out relavant and irrelavant colummns.

Step 2: Consider only relavant column. I have considered : ['Permit Type', 'Action Type', 'Work Type', 'Status', 'Category'].

Step 3: Load the CSV files with relevant fields and treat data['Permit Type', 'Action Type', 'Work Type', 'Status'] as X and data['Category'] as Y.

Step 4: Given data is totally categorical data. So you need to encode it using SKlearn encoders - LabelEncoder for X and OrdinalEncoder for Y. 

Step 5: Play with different types of classifier availabel in SKlearn: [Gaussian Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html), [Categorical Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html), [Multilabel Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression), [Decision Trees](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier), [Random Forests](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier), [Bagging with SVC](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html), [AdaBoost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html), [GradientBoost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html), [Ensemble classifier with voting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html), and [Multilayer Perceptrons](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html), by tunning their hyperparameters.

The code for all of above method is given in this repository.
### Results
|Method|Weighted average F1 Score|
|---|---|
|Gaussian Naive Bayes|68.39367|
|Categorical Naive Bayes|78.81097|
|Multilabel Linear Regression|77.39754|
|Decision Tree Classifier|81.52325|
|Random Forest Classifier|82.27261|
|Bagging with SVC|82.42150|
|AdaBoost Classifier|79.11288|
|GradientBoost Classifier|79.13241|
|Ensemble classifier with voting|72.53558|
|Multilayer Perceptron (MLP) with single Hidden layer and 100 neurons|82.11865|
|MLP with 2 hidden layers (100, 50) with LBFGS solver|81.67706|
|MLP with 3 hidden layers (200,100,50) with ADAM|81.67171|
|MLP with 4 hidden layers (200,100,50,20) with ADAM|82.42976|
|MLP with 5 hidden layers (400,200,100,50,20) with ADAM|81.75947|
|MLP with 6 hidden layers (800,400,200,100,50,20) with ADAM|77.00842|

