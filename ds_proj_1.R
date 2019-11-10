dataset<-read.csv("C:/ds_project/summary.txt",header=TRUE, sep=";")
coeffDima<-c(1,1,1,1,-1,1,1,-1,2,1,2,3)
coeffArtem<-c(1,1,1,1,-1,1,1,2,8,5,4,7)
coeffVanya<-c(1,1,1,1,-1,1,1,5,9,9,8,9)
result_numbers_Dima<-c()
result_numbers_Artem<-c()
result_numbers_Vanya<-c()
'coeffs<-lm(y~quantity+had_meal+premium+forum_premium
           +had_agentinfo+had_baggage+issue_baggage
           +nullsomeinfo+nulltraveldoc+nullbirthdate
           +maxflight+paxdoublingdata,dataset)'
for (paxid in dataset){
  result_numbers_Dima<-c(
   result_numbers_Dima,coeffDima[1]*dataset$quantity+coeffDima[2]*dataset$had_meal
   +coeffDima[3]*dataset$premium+coeffDima[4]*dataset$forum_premium
   +coeffDima[5]*dataset$had_agentinfo+coeffDima[6]*dataset$had_baggage
   +coeffDima[7]*dataset$issue_baggage+coeffDima[8]*dataset$nullsomeinfo
   +coeffDima[9]*dataset$nulltraveldoc+coeffDima[10]*dataset$nullbirthdate
   +coeffDima[11]*dataset$maxflight+coeffDima[12]*dataset$paxdoublingdata)
}
for (paxid in dataset){
  result_numbers_Artem<-c(
    result_numbers_Artem,coeffArtem[1]*dataset$quantity+coeffArtem[2]*dataset$had_meal
    +coeffArtem[3]*dataset$premium+coeffArtem[4]*dataset$forum_premium
    +coeffArtem[5]*dataset$had_agentinfo+coeffArtem[6]*dataset$had_baggage
    +coeffArtem[7]*dataset$issue_baggage+coeffArtem[8]*dataset$nullsomeinfo
    +coeffArtem[9]*dataset$nulltraveldoc+coeffArtem[10]*dataset$nullbirthdate
    +coeffArtem[11]*dataset$maxflight+coeffArtem[12]*dataset$paxdoublingdata)
}
for (paxid in dataset){
  result_numbers_Vanya<-c(
    result_numbers_Vanya,coeffVanya[1]*dataset$quantity+coeffVanya[2]*dataset$had_meal
    +coeffVanya[3]*dataset$premium+coeffVanya[4]*dataset$forum_premium
    +coeffVanya[5]*dataset$had_agentinfo+coeffVanya[6]*dataset$had_baggage
    +coeffVanya[7]*dataset$issue_baggage+coeffVanya[8]*dataset$nullsomeinfo
    +coeffVanya[9]*dataset$nulltraveldoc+coeffVanya[10]*dataset$nullbirthdate
    +coeffVanya[11]*dataset$maxflight+coeffVanya[12]*dataset$paxdoublingdata)
}
num_of_people_D<-table(result_numbers_Dima)
num_of_people_A<-table(result_numbers_Artem)
num_of_people_V<-table(result_numbers_Vanya)
plot(num_of_people_D)

