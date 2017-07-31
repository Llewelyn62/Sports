df <- read.csv("/Users/Llewelyn_home/Dropbox/Computation in Python/Computational-science/Computational_Science/Sport_Analytics/Lions-v-NZ.csv",strip.white = TRUE)
df
##NZ
hist(df$V6,
     breaks = 18,
     main="NZ v Lions",
     xlab = "Score",
     xlim = c(0,60))
#Lions
hist(df$V7,
     breaks = 8,
     xlab = "Score",
     xlim = c(0,60),
     col = 'red',
     add = TRUE)
#NZ
sum(df$V8=='NZ')
#Lions
sum(df$V8=='Lions')
#Draw
sum(df$V8=='Draw')
#Mean NZ
mean(df$V6)
sd(df$V6)
#Mean Lions
mean(df$V7)
sd(df$V7)
