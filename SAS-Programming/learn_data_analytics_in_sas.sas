SAS code

Chapter 1:

Surveyselect 
Proc surveyselect data=
Seed=
Method=srs or urs (urs is with replacement)
Samplesize=
Out=
Run;

Means
Proc means data= maxdec=2 fw=10 printalltypes <min max mean sd n nmiss median mode var range qrange q1 q3 clm stderr alpha=.05;
Class gender;
Var satscore;
Title 'xx';
Run;

Examining Your Data with PROC MEANS 
proc format;
value dosef
1="Placebo"
2="100mg"
3="200mg"
4="500mg";
run; 
proc means data=statdata.drug mean var std printalltypes; 
class Disease DrugDose;
var BloodP;
output out=means mean=BloodP_Mean; 
format DrugDose dosef.;
title 'Selected Descriptive Statistics for Drug Data Set'; 
run; title; 

univariate
proc univariate data=statdata.sales;
var Age;
histogram Age / normal (mu=est sigma=est);
probplot Age / normal (mu=est sigma=est);
title1 'Distribution of Age';
run;

Exploring associations with sgplot
Proc sgplot data= </options>;
Refline 1200 / axis=y lineattrs=(color=blue);
Dot hbar vbar categorical-var </options like /datalabel=idnumber>;
Hbox vbox histogram response-var </options like /category=predictor-var connect=mean>;
Scatter x=variable y=variable </options like /group=var markerattrs=(size=10)>;
Series x=variable y=variable </options like /group=var lineattrs=(thickness=2)>;
Needle x=var y=numeric-var </options>;
Reg x=numeric-var y=numeric-var </options>;
Run;

%let macro_var= pred1 pred2 pred3...
Proc sgscatter data=;
Plot response*(&macro_var) / reg;
Run;


Chapter 2:

T tests
Ttest to see if mean of continuous=1200
Proc univariate data= <mu0=1200 alpha=.05>;
Var continuous;
Id id_number;
Histogram conti / normal (mu=est sigma=est);
Inset skew.. kurt.. / position=ne;
Probplot <aka qq-plot, code is same as histogram>;
Run;

Ttest to see if H-alt: group1 (females) have higher (upper) score than group2 (males)
Proc ttest data= Plots(only shownull)=interval h0=0 sides=U;
Class gender;
Var score;
Run;

Anova
Ods graphics on /width=800;
Ods select meanplot lsmeans slicedanova;
Proc glm data= order=internal plots(only)=diagnostics(unpack) or =intplot or =(contourfit);
Class=predictor blocking-factor;
Model res=pred blk-fctr / hovtest=levene;
Means pred /hovtest;
Format var-name format-name;
Lsmeans pred1*pred2 / diff slice=pred1; /*Show effect of pred2 across levels of pred1*/
Lsmeans pred / pdiff=all adjust=tukey;
Lsmeans pred / pdiff=controlu('4') adjust=dunnett;
Lsmeans pred / pdiff=all adjust=t;
Store out=;
Run;

Proc plm
Proc plm restore= plots=all;
Slice pred1*pred2 / sliceby=pred1 adjust=tukey;
Effectplot interaction(sliceby=pred1) /clm;
Effectplot contour (y=pred1 x=pred2);
Effectplot slicefit (x=pred2 sliceby=pred1=250 to 1000 by 250);
Run;


Chapter 3:

Produce correlations and scatter plots - proc corr
/*H0 is that there is NO correlation, p-value < SL means reject H0, so we can say that there is some kind of correlation*/
/*plots=matrix instead of plots=scatter, produces scatter plot matrix instead of individual scatter plots*/
/*histogram in place of ellipse=none, produces histograms across the diagonal of the scatter plot matrix*/

Ods graphics on/ imagemap=on; width=800; /*imagemap=on + id name, enables tooltip*/
Proc corr data= rank nosimple plots(only)=scatter(nvar=all ellipse=none);
Var pred1 pred2 pred3..;
With res;
Id name;
Run;

/^
OUTH= Specifies the output data set with Hoeffding’s D statistics
OUTK= Specifies the output data set with Kendall correlation statistics
OUTP= Specifies the output data set with Pearson correlation statistics
OUTS= Specifies the output data set with Spearman correlation statistics
^/

Linear regression 
h0 - reg model does not fit data better than baseline model
outest=estimates - dataset containing parameter estimates and other summary statistics
clm - conf limit of mean, cli - confidence limit of individual predicted values
p - predict where res is missing
select=aic-bic-aicc-or-sbc can also be used, then we dont have to provide significance levels (NOT SURE ABOUT THIS FOR PROC REG)
sl - significance level
/vif - can be specified in model statement to detect collinearity - from chapter 4
plots(only)=(cp qq residualbypredicted residuals) - request diagnostic plots - from chapter 4

Proc reg data= noprint outest=estimates plots=all or plots(only)=(cp);
model1: model response=&predictors /clm cli p selection=cp rsquare adjrsq best=20;
model2: model response=&predictors /selection=stepwise-forward-or-backward details=steps select=sl slstay=.05 slentry=.05; 
id name age;
run;

/* proc reg doesnt have class or var statement options
selection= specifies selection method, fwd bckwd etc.
select=sl slentry= slstay= - specify selection criteria
selection criterion used in the forward selection method in the REG procedure is sle (slentry) */

Scoring Approach 1
/*Create a dataset with random values that need prediction*/
Data need-pred;
Input pred @@;
Datalines;
9 10 11 12 13
;
Run;
/*Merge the data used to build the model and data which needs prediction, predict in proc reg using /p in model statement*/
Data build-data_plus_need-pred;
Set need-pred build-data;
Run;

Scoring Approach 2
Proc score data=need_pred score=estimates out=scored_data 
type=parms; /*tells sas to use the parameter estimates in the outest=estimates dataset*/
Var pred;
Run;

Proc glm
proc glm data= plots(only)=(contourfit);
model SalePrice=Basement_Area Lot_Area;
store out=multiple;
title "Model with Basement Area and Gross Living Area"; 
run; quit; 

Proc plm
proc plm restore=multiple plots=all;
effectplot contour (y=Basement_Area x=Lot_Area);
effectplot slicefit(x=Lot_Area sliceby=Basement_Area=250 to 1000 by 250); 
run; title; 

Proc reg
ods graphics / imagemap=on;
proc reg data= plots(only)=(cp); 
ALL_REG: model target=&interval / selection=cp rsquare adjrsq best=20;
run; quit; title; 


Proc glmselect
/*proc glmselect automatically creates the _GLSIND macro variable . The macro variable stores the list of effects that are in the model that PROC GLMSELECT selects. You can then reference this macro as &_GLSIND in subsequent statements */ 

ods graphics on;
proc glmselect data= plots=all; 
STEPWISE: model target=&interval / selection=stepwise details=steps select=SL slstay=0.05 slentry=0.05; 
FORWARD: model target=&interval / selection=forward details=steps select=SL slentry=0.05; 
BACKWARD: model target=&interval / selection=backward details=steps select=SL slstay=0.05; 
/*select=aic-bic-aicc-sbc-adjrsq-cp (this is mallows cp) can also be used, then we dont have to provide significance levels*/
run; title; 


Chapter 4:

/*Requesting Specific Diagnostic Plots */
ods graphics / imagemap=on width=800;
proc reg data= plots(only)=(QQ RESIDUALBYPREDICTED RESIDUALS); 
model response=&predictors;
id Name;
run; quit; title; 

/*Looking for Influential Observations */
ods graphics on;
ods output RSTUDENTBYPREDICTED=Rstud
COOKSDPLOT=Cook
DFFITSPLOT=Dffits
DFBETASPANEL=Dfbs;
proc reg data= plots(only label)=
(RSTUDENTBYPREDICTED
COOKSD
DFFITS
DFBETAS); 
SigLimit: model response=&_GLSIND;

Chapter 5:

/*Crosstabulation Tables*/ 
ods graphics / width=500;
proc freq data=statdata.sales;
tables Purchase Gender Income Gender*Purchase Income*Purchase / 
plots=(freqplot) chisq expected cellchi2 nocol nopercent relrisk measures cl;
format Purchase purfmt.;
title1 'Frequency Tables for Sales Data';
run;

/*chisq - Pearson and framers v
cellchi2 - chi sq contribution of each cell
Measures cl - spearman with confidence limits
Relrisk - odds
Nocol nopercent - suppress col and total percent
Expected - expected freq under h0: no association */

/*Binary Logistic Regression Model */
ods graphics / width=700; 
proc logistic data=statdata.sales_inc plots(only)=(effect); 
class Gender (param=ref ref='Male');
model Purchase(event='1')=Gender;
title1 'LOGISTIC MODEL (1):Purchase=Gender'; 
run; 

/*Multiple Logistic Regression Model */
ods graphics / width=700;
proc logistic data=statdata.sales_inc plots(only)=(effect oddsratio); 
class Gender (param=ref ref='Male') IncLevel (param=ref ref='1'); 
units Age=10;
model Purchase(event='1')=Gender Age IncLevel / selection=backward clodds=pl;
title1 'LOGISTIC MODEL (2):Purchase=Gender Age IncLevel'; 
run; 

/*Multiple Logistic Regression Model with Interactions*/ 
proc logistic data=statdata.sales_inc plots(only)=(effect oddsratio); 
class Gender (param=ref ref='Male') IncLevel (param=ref ref='1');
units Age=10;
model Purchase(event='1')=Gender | Age | IncLevel @2 / selection=backward clodds=pl;
title1 'LOGISTIC MODEL (3): Main Effects and 2-Way Interactions';
title2 '/ sel=backward';
run; title; 

/*Fitting a Multiple Logistic Regression Model with All Odds Ratios */
ods select OddsRatiosPL ORPlot;
proc logistic data=statdata.sales_inc plots(only)=(oddsratio); 
class Gender (param=ref ref='Male') IncLevel (param=ref ref='1'); 
units Age=10;
model Purchase(event='1')=Gender | IncLevel Age;
oddsratio Age / cl=pl;
oddsratio Gender / diff=ref at (IncLevel=all) cl=pl; oddsratio IncLevel / diff=ref at (Gender=all) cl=pl;
title1 'LOGISTIC MODEL (3a): Significant Terms and All Odds Ratios';
title2 '/ sel=backward';
run; title; 

/*Generating Predictions Using PROC PLM */
ods select none;
proc logistic data=statdata.ameshousing3; 
class Fireplaces (ref='0') Lot_Shape_2 (ref='Regular') / param=ref; 
model Bonus(event='1')=Basement_Area|Lot_Shape_2 Fireplaces; 
units Basement_Area=100;
store out=isbonus; 
run;

ods select all;
data newhouses;
length Lot_Shape_2 $9;
input Fireplaces Lot_Shape_2 $ Basement_Area;
datalines;
0 Regular 1060 
2 Regular 775 
2 Irregular 1100 
1 Irregular 975 
1 Regular 800 
; 
run; 

proc plm restore=isbonus;
score data=newhouses out=scored_houses / ILINK; 
title 'Predictions using PROC PLM'; 
run; 

proc print data=scored_houses;
run;

/* The SCORE statement in the LOGISTIC procedure returns only predicted probabilities, whereas the SCORE procedure returns only predicted logits. */

/*A. Use the SCORE statement in the LOGISTIC procedure.
B. Augment the training data set with new observations and set their responses to missing.
C. Augment the training data set with new observations and rerun the LOGISTIC procedure. (INCORRECT)
D. Use the saved parameter estimates from the LOGISTIC procedure and score new observations in the SCORE procedure. */

/* both data steps calculate predicted probabilities 
data new;
set scored;
p=1/(1+exp(-event));
run;

data new;
set scored;
odds=exp(event);
p=odds/(1+odds);
run;
*/


Chapter 6:

PROC GLMSELECT to Build a Predictive Model 
ods graphics;
proc glmselect data= plots=all valdata= ; 
class &categorical / param=glm ref=first; 
model target=&categorical &interval / selection=backward select=sbc choose=validate;
store out= ; 
title "Selecting the Best Model using Honest Assessment"; 
run; title; 

/*SELECTION= option specifies the backward selection model of variable selection 
SELECT=SBC indicates that the Schwarz-Bayesian criterion will be used to determine which variables remain in the model 
choose=validate - select best model based on validation data */

Methods of Scoring 
PROC GLMSELECT + SCORE statement
PROC GLMSELECT + store statement -> PROC PLM + score statement
PROC GLMSELECT + store statement -> PROC PLM + code file= statement -> Data step + %include “…” 

Method 1:
proc glmselect data= plots=all valdata= ; 
class &categorical / param=glm ref=first; 
model target=&categorical &interval / selection=backward select=sbc choose=validate;
store out=work.amesstore;
score data=new-data out=scored1;
run; title;
Method 2:
proc plm restore= ;
score data=new-data out=scored2; 
code file="my-file-path/scoring.sas"; 
run; 

Method 3:
data scored3;
set new-data;
%include "my-file-path/scoring.sas"; 
run; 


/*********************** module 2 **********************/

Chapter 7:

Proc sort data=x out=y;
By ins;
Run;

Proc surveyselect noprint data=y samprate=.6667 out=z seed=444 outall;
Strata ins;
Run;

Data work.train(drop=selected selectionprob samplingweight) work.valid(drop=selected selectionprob samplingweight);
Set z;
If selected then output work.train;
Else output work.valid;
Run;


Chapter 8:

Proc logistic
Ods graphics on;
Proc logistic data=work.train plots(only maxpoints=none)=(effect(clband x=(continuous-variables class-variables)) oddsratio(type=horizontalstat));
Class class-variable (param=ref ref='xx') class-variable (param=ref ref='xx');
Model target-variable(event='xx')=predictor-variables / stb closes=pl;
Units continuous-variables=1000 continuous-variables=1000 / default=1;
Oddsratio 'title' class-variable / diff=all cl=pl;
Oddsratio 'title' class-variable / diff=all cl=pl;
Effectplot slicefit(sliceby=dda x=ddabal)/noobs;
Effectplot slicefit(sliceby=dda x=ddaamt)/noobs;
Run;
Title1;

Scoring - 3 ways
method 1:
Proc logistic data= noprint;
Class ...;
Model ...;
Score data=pmlr.new out=;
Run;

method 2:
Proc logistic data= outmodel= noprint;
Class...;
Model...;
Run;
Proc logistic inmodel= noprint;
Score data=pmlr.new out=;
Run;

method 3:
Proc logistic data= noprint;
Class...;
Model...;
Code file="path/file.txt";
Run;
Data work.scored;
Set pmlr.new;
%include "path/file.txt";
Run;

correcting oversampling - 2 ways
%global pi1;
%let pi1=.02;

method 1:
proc logistic data= noprint;
class...;
model...;
socre data=work.new out= priorevent=&pi1;
run;

method 2:
Proc logistic data= noprint;
Class...;
Model...;
Code file="path/file.txt";
Run;
%global rho1;
proc sql noprint; 
select mean(target-variable) into :rho1 from work.train;
quit;
data work.new;
set pmlr.new;
off=log(((1-&pi1)*&rho1)/(&pi1*(1-&rho1)));
run;
Data work.scored;
Set work.new;
%include "path/file.txt";
eta=log(p_ins1/p_ins0)-off;
prob=1/(1+exp(-eta));
Run;


Chapter 9:

/* Create missing indicators */
data work.train_mi(drop=i);
set work.train;
array mi{*} MIAcctAg MIPhone ;
array x{*} acctage phone ;
do i=1 to dim(mi); mi{i}=(x{i}=.);
nummiss+mi{i};
end;
run;
/* Impute missing values with the median */
proc stdize data=work.train_mi reponly method=median
out=work.train_imputed;
var &inputs;
run; 

Collapsing the Levels of a Nominal Input
proc means data=work.train_imputed noprint nway;
class branch;
var ins;
output out=work.level mean=prop;
/* using clusterhistory */
ods output clusterhistory=work.cluster;
proc cluster data=work.level method=ward outtree=work.fortree
plots=(dendrogram(vertical height=rsq));
freq _freq_;
var prop;
id branch;

Replacing Categorical Levels by Using SWOE Coding
/* Rho1 is the proportion of events in the training data set. */
%global rho1;
/*number of observations and events for each level of branch*/
proc means data=work.train_imputed sum nway noprint;
class branch;
var ins;
output out=work.counts sum=events;
run; 
/* The DATA Step creates scoring code to assign SWOE to each branch */
filename brswoe "&PMLRfolder/swoe_branch.sas";
data _null_;
file brswoe;
set work.counts end=last;
logit=log((events + &rho1*24)/(_FREQ_ - events + (1-&rho1)*24));
if _n_=1 then put "select (branch);" ;
put " when ('" branch +(-1) "') branch_swoe = " logit ";" ;
if last then do;
logit=log(&rho1/(1-&rho1));
put " otherwise branch_swoe = " logit ";" / "end;";
end; 
run;
data work.train_imputed_swoe;
set work.train_imputed;
%include brswoe / source2;
run;

Reducing Redundancy by Clustering Variables
ods output clusterquality=work.summary rsquare=work.clusters;
/* proc varclus */
proc varclus data=work.train_imputed_swoe maxeigen=.7 hi;
var &inputs branch_swoe miacctag miphone ;
run;
/* Use the CALL SYMPUT function to create a macro variable:&NVAR = the number of of clusters */
%global nvar;
data _null_;
set work.summary;
call symput('nvar',compress(NumberOfClusters));
run;
/* Variables by Cluster */
proc print data=work.clusters noobs label split='*';
where NumberOfClusters=&nvar;
var Cluster Variable RSquareRatio VariableLabel;
label RSquareRatio="1 - RSquare*Ratio";
run;
/* Variation Explained by Clusters */
proc print data=work.summary label;
run;

Performing Variable Screening
/* Rank of Spearman Correlations and Hoeffding Correlations 
ranksp - Spearman rank*of variables'
scorr - Spearman Correlation'
spvalue - Spearman p-value'
rankho - Hoeffding rank*of variables'
hcorr - Hoeffding Correlation'
hpvalue - Hoeffding p-value*/
ods output spearmancorr=work.spearman hoeffdingcorr=work.hoeffding;
proc corr data=work.train_imputed_swoe spearman hoeffding;
var ins;
with &reduced;
run;
data work.correlations; /* to merge spearman and huffing datasets */
merge work.spearman(rename=(ins=scorr pins=spvalue)) work.hoeffding(rename=(ins=hcorr pins=hpvalue));
by variable;
scorr_abs=abs(scorr);
hcorr_abs=abs(hcorr);
run;
proc rank data=work.correlations out=work.correlations1 descending;
var scorr_abs hcorr_abs;
ranks ranksp rankho;
run;
/* Find values for reference lines */
%global vref href;
proc sql noprint;
select min(ranksp) into :vref
from (select ranksp from work.correlations1 having spvalue > .5);
select min(rankho) into :href
from (select rankho from work.correlations1 having hpvalue > .5);
quit;
/* Scatter Plot of the Ranks of Spearman vs. Hoeffding */
proc sgplot data=work.correlations1;
refline &vref / axis=y;
refline &href / axis=x;
scatter y=ranksp x=rankho / datalabel=variable;
yaxis label="Rank of Spearman";
xaxis label="Rank of Hoeffding";
run;

Creating Empirical Logit Plots
/* BINS dataset contains: 
INS=count of successes in each bin 
_FREQ_=the count of trials in each bin
DDABAL=the avg DDABAL in each bin */
/* creating bins */
proc means data=work.ranks noprint nway;
class bin;
var ins &var;
output out=work.bins sum(ins)=ins mean(&var)=&var;
run;
/* Calculate the empirical logit */
data work.bins;
set work.bins;
elogit=log((ins+(sqrt(_FREQ_ )/2))/( _FREQ_ -ins+(sqrt(_FREQ_ )/2)));
run;
/* Empirical Logit against Binned &var */
proc sgplot data=work.bins;
reg y=elogit x=bin / curvelabel="Linear Relationship?" curvelabelloc=outside lineattrs=(color=ligr);
series y=elogit x=bin;
run;

Selecting Variables Sequentially 
BIC Based Significance Level
%global sl;
proc sql;
select 1-probchi(log(sum(ins ge 0)),1) into :sl
from work.train_imputed_swoe_bins;
quit;
/* Interaction Detection using Forward Selection */
proc logistic data=work.train_imputed_swoe_bins;
class res (param=ref ref='S');
model ins(event='1')= &screened res <"all interactions listed using |"> @2 
/ include=28 clodds=pl selection=forward slentry=&sl;
run;
/* Backward Selection for Variable Annuity Data Set */
proc logistic data=work.train_imputed_swoe_bins;
class res (param=ref ref='S');
model ins(event='1')= &screened res <"signif interactions from fwd selection"> 
/ clodds=pl selection=backward slstay=&sl hier=single fast;
run;
/* create dummy variables for res - this way we wont need class statement in proc for best subset selection */ 
data work.train_imputed_swoe_bins;
set work.train_imputed_swoe_bins;
resr=(res='R');
resu=(res='U');
run;
/* Models Selected by Best Subsets Selection 
In best-subsets selection, model hierarchy is not maintained */ 
proc logistic data=work.train_imputed_swoe_bins;
model ins(event='1')=&screened resr resu <"signif interactions from fwd selection"> 
/ selection=score best=1;
run;


Chapter 10

Measuring Model Performance Based on Commonly-Used Metrics
ods select roccurve scorefitstat;
proc logistic data= ;
model ins(event='1')=&selected;
score data=new-data out=scored priorevent=&pi1 outroc=work.roc fitstat;
run;

data work.roc;
set work.roc;
cutoff=_PROB_;
specif=1-_1MSPEC_;
tp=&pi1*_SENSIT_;
fn=&pi1*(1-_SENSIT_);
tn=(1-&pi1)*specif;
fp=(1-&pi1)*_1MSPEC_;
depth=tp+fp;
pospv=tp/depth;
negpv=tn/(1-depth);
acc=tp+tn;
lift=pospv/&pi1;
keep cutoff tn fp fn tp
_SENSIT_ _1MSPEC_ specif depth
pospv negpv acc lift;
run;

/* Create a lift chart */
proc sgplot data=work.roc;
where 0.005 <= depth <= 0.50;
series y=lift x=depth;
refline 1.0 / axis=y;
yaxis values=(0 to 4 by 1);
run; quit;

Using a Profit Matrix to Measure Model Performance
proc SQL noprint;
select mean(INS) into :rho1 from pmlr.develop;
q

