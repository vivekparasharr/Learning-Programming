
install.packages("ggplot2")

library('ggplot2')

A=c(2,1,4,9)
B=c(3,2,5,10)
C=c(4,1,15,80)
D=c('a','a','b','b')
simple_dataset = data.frame(A,B,C,D)

simple_dataset2=data.frame(simple_dataset$A,simple_dataset$C,simple_dataset$D)
colnames(simple_dataset2) <- c('x','y','shape')



