dataset<-read.csv("C:/ds_project/AirlinesV2BETA.txt",header=TRUE, sep=";")
ids<-unique(dataset$paxid)
coeff<-c(1,1,1,1,1,1)
result_numbers<-c()
for (id in ids[1:1000]){
  print(id)
  id_dataset <- dataset[dataset$paxid==id,]
  flights_number<-length(id_dataset)
  max_flights_number<-max(table(id_dataset$codedest))
  dang_flights_number<-length(id_dataset[id_dataset$codedest=="IRQ"|id_dataset$codedest=="IRN"|id_dataset$codedest=="CHN"|id_dataset$codedest=="PRK"])
  no_agentinfo<-sum(is.na(id_dataset$agentinfo))
  no_status<-sum(is.na(id_dataset$status))
  result_numbers<-c(result_numbers,coeff[1]*flights_number+coeff[2]*max_flights_number+coeff[3]*dang_flights_number+coeff[4]*no_agentinfo+coeff[5]*no_status)
}
plot(ids[1:1000],result_numbers) 
