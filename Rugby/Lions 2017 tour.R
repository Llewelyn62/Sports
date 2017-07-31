#NZ LIONS 2017 TOUR
#Test 11/1.23
x <- seq(from = -50, to = 50, length.out = 17)
y <- c(251,181,81,61,31,21,11,6.5,26,4.25,4.25,4.25,6,10,21,41,41)
plot(x,y,xlab = 'Score differential',ylab = '$ payout per dollar bet', title('TAB odds for NZ-v-Lions Rugby Test 1'),panel.first = grid(), col = 'red')
pY <- 1/y
pY
sum(pY)
plot(x,pY,xlab = 'Score differential',ylab = 'How likely this will be the score difference', title('TAB probability for NZ-v-Lions Rugby Test 1'),panel.first = grid(), col = 'blue', pch = 17)
1/1.23 # p(NZ) win.
1/4.05 #p(Lions) win
1/4.05 + 1/1.23 + 1/26 #total p
