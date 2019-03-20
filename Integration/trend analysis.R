library(dplyr)
library(magrittr)
library(reshape2)

dat <- read.csv("../../HSData/Result/Hospital_FullData_0221.csv")

# Ownership
tbl <- dat %>% 
  mutate(Segment = case_when(Sub.ownership %in% c("Gov-DoD","Gov-VA","Gov-otherFederal") ~ "Federal",
                             TRUE ~ as.character(Sub.ownership))) %>%
  group_by(Year, System_member, Segment) %>%
  summarise(Freq = n()) %>%
  na.omit() %>%
  dcast(Year + Segment ~ System_member, value.var="Freq")


names(tbl)[3:4] <- c("Independent Hospital","Hospital in HS")

tbl2 <- dat %>% 
  mutate(Segment = case_when(Sub.ownership %in% c("Gov-DoD","Gov-VA","Gov-otherFederal") ~ "Federal",
                             Sub.ownership %in% c("Gov-HospitalDistrict","Gov-CityStateCounty") ~ "CityStateCountyHD",
                                   TRUE ~ as.character(Sub.ownership))) %>%
  group_by(Year, System_member, Segment) %>%
  summarise(Freq = n()) %>%
  na.omit() %>%
  dcast(Year ~ System_member + Segment, value.var="Freq")

write.csv(tbl,"tbl.csv",row.names = FALSE)

write.csv(tbl2,"tbl4.csv",row.names = FALSE)

# by bed size
bedtbl <- dat %>%
  group_by(Year, System_member, bed_bucket) %>%
  summarise(Freq = n()) %>%
  na.omit() %>%
  dcast(Year ~ System_member+bed_bucket, value.var="Freq")
write.csv(bedtbl,"bedtbl.csv",row.names = FALSE)
